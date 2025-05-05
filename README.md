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
```
# 📁 Model Setup

**EchoTales** utilizes the **Dia model** from **Nari Labs**. The model is dynamically loaded when you run the application.

---

# ▶️ Running the App

1. Clone or download the repository.
2. Install the required dependencies.
3.Run the Notebook

## 📘 How to Use the Application

**Text Input:**  
Enter the text you want to be narrated in the provided text box.

**Generate Narration:**  
Click the "Generate Narration" button. This splits the text into sentences, processes them in batches, and generates audio for each.

**Adjust Speed:**  
Use the WPM slider to control narration pace.

**Listen to Audio:**  
Play the generated audio directly from the interface.

---

## 📝 Example Workflow

**Input Text:**

> "EchoTales brings stories to life. It helps create amazing narrations with just a few clicks."

**Generated Output:**

- The narration is generated at the default WPM.
- Speed can be adjusted using the slider.

**Final Audio:**

- A `.wav` file is produced.
- Playback is available in the app.

---

## ⚙️ Customization Options

- **WPM Slider:** Fine-tune the narration speed.
- **Speed Factor:** Displays how much the narration speed has been altered.
- **Device Info:** Shows whether the app is running on CPU or GPU.

---

## 🧰 Troubleshooting

- **No Audio Generated:** Make sure your input text is not empty and the app is running correctly.
- **Audio Too Fast or Slow:** Adjust the WPM slider and verify the speed factor.
- **Model Loading Error:** Check your internet connection; the model is downloaded dynamically.

---

## 📄 License

This project is licensed under the **MIT License** – see the `LICENSE` file for details.
