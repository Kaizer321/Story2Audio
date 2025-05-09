import gradio as gr
import grpc
import text_to_speech_pb2
import text_to_speech_pb2_grpc
import torch
import soundfile as sf
import json
import os

def check_device():
    return "cuda" if torch.cuda.is_available() else "cpu"

def generate_narration(text_input):
    try:
        channel = grpc.insecure_channel('localhost:50051')
        stub = text_to_speech_pb2_grpc.TextToSpeechStub(channel)

        request = text_to_speech_pb2.NarrationRequest(text_input=text_input)
        response = stub.GenerateNarration(request)

        audio_array, sr = sf.read(response.audio_file)
        wpm = response.wpm

        output_data = {
            "audio_file": response.audio_file,
            "text": response.text,
            "wpm": wpm
        }

        json_file_path = "generated_output.json"

        with open(json_file_path, "w") as json_file:
            json.dump(output_data, json_file)

        return json_file_path, f"Generated text:\n{response.text}"

    except Exception as e:
        return None, f"Error: {str(e)}"

with gr.Blocks(title="🎙 EchoTales: The Voice of Stories") as app:
    gr.Markdown("# 🎙 EchoTales: The Voice of Stories")
    
    with gr.Row():
        with gr.Column():
            text_input = gr.TextArea(label="Enter your story text here:", lines=10)
            generate_btn = gr.Button("Generate Narration")
            audio_output = gr.Audio(label="Generated Narration", interactive=False)
            generated_text_state = gr.State()
            device_info = gr.Textbox(label="Device", value=f"Running on: {check_device()}", interactive=False)
            
            wpm_output = gr.Textbox(label="Words Per Minute", interactive=False)
            
            generate_btn.click(
                fn=generate_narration,
                inputs=text_input,
                outputs=[audio_output, generated_text_state],
            )

if __name__ == "__main__":
    public_link = app.launch(share=True)
    print(f"Gradio app is running at: {public_link}")
