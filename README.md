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



## 📁 Model Setup

EchoTales utilizes the **Dia model** from **Nari Labs**. The model will be loaded dynamically when you run the application.

---

## ▶️ Running the App

1. Clone or download the repository.
2. Install the required dependencies.
3. Navigate to the project folder in your terminal.
4. Run the following command:

```bash
python app.py


📘 How to Use the Application
Text Input: Enter the text you want to be narrated in the provided text box.

Generate Narration: Click the "Generate Narration" button. This will split the text into sentences, process them in batches, and generate audio for each sentence.

Adjust Speed: After the narration is generated, adjust the speed using the WPM (Words Per Minute) slider.

Listen to Audio: You can play the generated audio directly from the interface.

📝 Example Workflow
Input Text:

"EchoTales brings stories to life. It helps create amazing narrations with just a few clicks."

Generated Output:

The application will generate a narration with the default WPM.

You can adjust the speed using the slider.

Final Audio:

The app generates a .wav file of the narration.

You can listen to it directly through the interface.

⚙️ Customization Options
WPM Slider: Allows you to fine-tune the speed of the narration.

Speed Factor: Displays how much the speed has changed after adjustments.

Device Info: Shows whether the app is running on CPU or GPU for performance insights.

🧰 Troubleshooting
No Audio Generated: Ensure that your input text is not empty, and the application is running correctly.

Audio Too Fast or Slow: Adjust the WPM slider and verify the speed factor.

Model Loading Error: Make sure you have an active internet connection, as the model loads from a pre-trained server.

📄 License
This project is licensed under the MIT License – see the LICENSE file for details.
