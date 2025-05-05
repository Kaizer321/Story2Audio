# 🎙️ EchoTales: The Voice of Stories

**EchoTales** is a Text-to-Speech (TTS) application designed to bring stories to life with lifelike narration. Using the Dia model from Nari Labs, EchoTales generates high-quality audio narrations from input text and allows users to adjust the narration speed based on words per minute (WPM). Whether you're creating voiceovers for a story, audiobook, or any narrative, EchoTales offers a simple, interactive way to generate and adjust narration.

---

## 🚀 Features

- **Narration Generation**: Converts any text into audio using the state-of-the-art Dia model.
- **Speed Adjustment**: Easily adjust the words per minute (WPM) of the narration to fit your needs.
- **Audio Quality Enhancement**: Applied filters ensure clear, crisp, and consistent narration.
- **Temporary Audio Handling**: Efficient management of temporary audio files during processing.
- **Device Information**: Displays device status (CPU or GPU) for transparency.

---

## 🔧 How It Works

1. **Enter Text**: Input your story or text into the text area on the app interface.
2. **Generate Narration**: Press the "Generate Narration" button to create the audio version of the input text.
3. **Adjust Speed**: Use the WPM slider to adjust narration speed; the app recalculates the speed factor accordingly.
4. **Listen to Audio**: Play the generated audio directly through the interface.
5. **Speed Factor Display**: View the current WPM and speed factor to fine-tune the output.

---

## 🛠 Installation and Setup

### ✅ Requirements

- Python 3.8 or higher

**Required libraries:**

- `gradio`
- `soundfile`
- `torch`
- `numpy`
- `ffmpeg-python`
- `re` (used for sentence splitting)

### 📦 Install Dependencies

```bash
pip install gradio soundfile torch numpy ffmpeg-python
``` bash



