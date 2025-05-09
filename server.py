import grpc
import text_to_speech_pb2
import text_to_speech_pb2_grpc
import soundfile as sf
from dia.model import Dia
import torch
import numpy as np
import os
import random
import re
import shutil
import logging
from concurrent import futures
from pathlib import Path

# Configuration
DEFAULT_WPM = 175
AUDIO_DIR = "audio_parts"
COMBINED_AUDIO = "output_combined.wav"
FILTERED_AUDIO = "output_combined_filtered.wav"
MODEL_NAME = "nari-labs/Dia-1.6B"
SAMPLE_RATE = 44100
MAX_WORKERS = 10
SILENCE_DURATION = 0.5  # seconds between sentences

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AudioGenerator:
    def __init__(self):
        self.device = self._check_device()
        self.model = self._load_model()

    @staticmethod
    def _check_device():
        return "cuda" if torch.cuda.is_available() else "cpu"

    def _load_model(self):
        try:
            logger.info(f"Loading model: {MODEL_NAME} on {self.device}")
            model = Dia.from_pretrained(MODEL_NAME).to(self.device)
            logger.info("Model loaded successfully")
            return model
        except Exception as e:
            logger.error(f"Model loading failed: {str(e)}")
            raise RuntimeError(f"Failed to load model: {str(e)}")

    def generate_audio(self, text, seed=42):
        try:
            # Set all seeds for reproducibility
            torch.manual_seed(seed)
            np.random.seed(seed)
            random.seed(seed)
            if torch.cuda.is_available():
                torch.cuda.manual_seed_all(seed)

            logger.info(f"Generating audio for text: {text[:50]}...")
            return self.model.generate(text)
        except Exception as e:
            logger.error(f"Audio generation failed: {str(e)}")
            raise RuntimeError(f"Audio generation failed: {str(e)}")

class AudioProcessor:
    @staticmethod
    def ensure_directory(directory):
        Path(directory).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def clean_directory(directory):
        if Path(directory).exists():
            shutil.rmtree(directory)
        Path(directory).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def save_audio(audio, file_path, sample_rate=SAMPLE_RATE):
        try:
            # Ensure the directory exists
            Path(os.path.dirname(file_path)).mkdir(parents=True, exist_ok=True)
            sf.write(file_path, audio, sample_rate)
            logger.info(f"Audio saved to {file_path}")
            return file_path
        except Exception as e:
            logger.error(f"Failed to save audio: {str(e)}")
            raise RuntimeError(f"Failed to save audio file: {str(e)}")

    @staticmethod
    def generate_silence(duration, sample_rate=SAMPLE_RATE):
        return np.zeros(int(duration * sample_rate), dtype=np.float32)

    @staticmethod
    def split_sentences(text):
        # Split text into sentences using regex
        sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text.strip()) if s.strip()]
        logger.info(f"Split text into {len(sentences)} sentences")
        return sentences

    @staticmethod
    def batch_sentences(sentences, batch_size=4):
        # Group sentences into batches
        batches = [sentences[i:i + batch_size] for i in range(0, len(sentences), batch_size)]
        logger.info(f"Created {len(batches)} batches from {len(sentences)} sentences")
        return batches

    @staticmethod
    def apply_audio_filters(input_path, output_path, speed_factor=1.0):
        try:
            # Ensure the input file exists
            if not os.path.exists(input_path):
                raise FileNotFoundError(f"Input audio file not found: {input_path}")
                
            filter_complex = (
                f"atempo={speed_factor},"
                f"equalizer=f=1000:t=q:w=1:g=-5,"
                f"equalizer=f=2000:t=q:w=1:g=-5,"
                f"equalizer=f=5000:t=q:w=1:g=-5,"
                f"dynaudnorm,"
                f"loudnorm=I=-16:TP=-1.5:LRA=11"
            )
            
            # Ensure the output directory exists
            Path(os.path.dirname(output_path)).mkdir(parents=True, exist_ok=True)
            
            command = f"ffmpeg -y -i {input_path} -af \"{filter_complex}\" {output_path}"
            logger.info(f"Running ffmpeg command: {command}")
            
            exit_code = os.system(command)
            if exit_code != 0:
                raise RuntimeError(f"ffmpeg command failed with exit code {exit_code}")
                
            logger.info(f"Filtered audio saved to {output_path}")
            return output_path
        except Exception as e:
            logger.error(f"Audio filtering failed: {str(e)}")
            raise RuntimeError(f"Audio filter application failed: {str(e)}")

class TextToSpeechServicer(text_to_speech_pb2_grpc.TextToSpeechServicer):
    def __init__(self):
        self.audio_generator = AudioGenerator()
        self.audio_processor = AudioProcessor()

    def GenerateNarration(self, request, context):
        try:
            text_input = request.text_input.strip()
            if not text_input:
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                context.set_details("Input text cannot be empty")
                return text_to_speech_pb2.NarrationResponse()

            # Prepare directory for audio parts
            self.audio_processor.clean_directory(AUDIO_DIR)
            
            # Process text
            sentences = self.audio_processor.split_sentences(text_input)
            batches = self.audio_processor.batch_sentences(sentences)

            # Generate audio for each batch in parallel
            with futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
                batch_futures = []
                for i, batch in enumerate(batches):
                    future = executor.submit(
                        self._process_batch,
                        batch_index=i,
                        sentences=batch,
                        seed=42
                    )
                    batch_futures.append(future)

                # Wait for all batches to complete
                futures.wait(batch_futures)
                part_files = [f.result() for f in batch_futures]

            # Combine all audio parts
            final_audio = np.array([], dtype=np.float32)
            for file in sorted(part_files, key=lambda x: int(re.search(r'batch_(\d+)\.wav', x).group(1))):
                audio_part, _ = sf.read(file)
                final_audio = np.concatenate(
                    (final_audio, audio_part, self.audio_processor.generate_silence(SILENCE_DURATION))
                )  # Fixed missing closing parenthesis
            
            # Save combined audio and apply filters
            self.audio_processor.save_audio(final_audio, COMBINED_AUDIO)
            filtered_audio_path = self.audio_processor.apply_audio_filters(COMBINED_AUDIO, FILTERED_AUDIO)

            # Calculate words per minute
            duration_seconds = len(final_audio) / SAMPLE_RATE
            wpm = self._calculate_wpm(text_input, duration_seconds)

            logger.info(f"Narration completed: {len(sentences)} sentences, {len(final_audio)/SAMPLE_RATE:.2f} seconds, {wpm:.1f} WPM")
            
            return text_to_speech_pb2.NarrationResponse(
                audio_file=filtered_audio_path,
                text=text_input,
                wpm=wpm
            )

        except Exception as e:
            logger.error(f"Error in GenerateNarration: {str(e)}")
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Internal server error: {str(e)}")
            return text_to_speech_pb2.NarrationResponse()

    def _process_batch(self, batch_index, sentences, seed):
        """Process a batch of sentences and return the path to the saved audio file"""
        try:
            logger.info(f"Processing batch {batch_index} with {len(sentences)} sentences")
            batch_audio = np.array([], dtype=np.float32)
            
            for sentence in sentences:
                audio = self.audio_generator.generate_audio(sentence, seed)
                batch_audio = np.concatenate(
                    (batch_audio, audio, self.audio_processor.generate_silence(SILENCE_DURATION))
                )
                
            file_path = os.path.join(AUDIO_DIR, f"batch_{batch_index}.wav")
            self.audio_processor.save_audio(batch_audio, file_path)
            return file_path
        except Exception as e:
            logger.error(f"Error processing batch {batch_index}: {str(e)}")
            raise

    @staticmethod
    def _calculate_wpm(text, duration_seconds):
        """Calculate words per minute rate"""
        word_count = len(text.split())
        if duration_seconds <= 0:
            logger.warning("Duration is zero or negative, using default WPM")
            return DEFAULT_WPM
        wpm = (word_count / duration_seconds) * 60
        logger.info(f"Word count: {word_count}, duration: {duration_seconds:.2f}s, WPM: {wpm:.1f}")
        return wpm

def serve():
    """Start the gRPC server"""
    # Create directories if they don't exist
    Path(AUDIO_DIR).mkdir(parents=True, exist_ok=True)
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=MAX_WORKERS))
    text_to_speech_pb2_grpc.add_TextToSpeechServicer_to_server(
        TextToSpeechServicer(), server)
    server.add_insecure_port('[::]:50051')
    
    logger.info("Starting Text-to-Speech server on port 50051")
    try:
        server.start()
        logger.info("Server started. Waiting for requests...")
        server.wait_for_termination()
    except KeyboardInterrupt:
        logger.info("Shutting down server due to keyboard interrupt...")
    except Exception as e:
        logger.error(f"Server error: {str(e)}")
    finally:
        logger.info("Stopping server...")
        server.stop(0)
        logger.info("Server stopped")

if __name__ == "__main__":
    serve()