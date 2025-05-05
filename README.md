# 🎙️ EchoTales: The Voice of Stories

**EchoTales** is a Text-to-Speech (TTS) application designed to bring stories to life with lifelike narration. Using the **Dia model from Nari Labs**, EchoTales generates high-quality audio narrations from input text and allows users to adjust the narration speed based on **words per minute (WPM)**. Whether you're creating voiceovers for a story, audiobook, or any narrative, EchoTales offers a simple, interactive way to generate and adjust narration.

---

## ✨ Features

- **Narration Generation**: Converts any text into audio using the state-of-the-art Dia model.
- **Speed Adjustment**: Easily adjust the words per minute (WPM) of the narration to fit your needs.
- **Audio Quality Enhancement**: Applied filters to ensure clear, crisp, and consistent narration.
- **Temporary Audio Handling**: Efficient management of temporary audio files during processing.
- **Device Information**: Displays device status (CPU or GPU) for transparency.

---

## 🛠️ Requirements

- **Python** 3.8 or higher

### Required Libraries:

- `gradio`
- `soundfile`
- `torch`
- `numpy`
- `ffmpeg-python`
- `re` (standard library)

Install all dependencies using:

```bash
pip install gradio soundfile torch numpy ffmpeg-python

# 📁 Model Setup

**EchoTales** utilizes the **Dia model** from **Nari Labs**. The model is dynamically loaded when you run the application.

---

# ▶️ Running the App

1. Clone or download the repository.
2. Install the required dependencies.
3. Navigate to the project folder in your terminal.
4. Run the app using:

```bash
python app.py
