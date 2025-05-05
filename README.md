🎙️ EchoTales: The Voice of Stories
EchoTales is a Text-to-Speech (TTS) application designed to bring stories to life with lifelike narration. Using the Dia model from Nari Labs, EchoTales generates high-quality audio narrations from input text and allows users to adjust the narration speed based on words per minute (WPM). Whether you're creating voiceovers for a story, audiobook, or any narrative, EchoTales offers a simple, interactive way to generate and adjust narration.

Features
Narration Generation: Converts any text into audio using the state-of-the-art Dia model.

Speed Adjustment: Easily adjust the words per minute (WPM) of the narration to fit your needs.

Audio Quality Enhancement: Applied filters to ensure clear, crisp, and consistent narration.

Temporary Audio Handling: Efficient management of temporary audio files during processing.

Device Information: Displays device status (CPU or GPU) for transparency.

How It Works
Enter Text: Input your story or text into the text area on the app interface.

Generate Narration: Press the "Generate Narration" button to create the audio version of the input text.

Adjust Speed: Adjust the narration speed using the WPM slider. The app recalculates the speed factor and reprocesses the audio.

Listen to Audio: After narration is generated, you can listen to the audio through the interface.

Speed Factor Display: The application displays the current WPM and speed factor to ensure the output matches your expectations.

Installation and Setup
To run EchoTales on your machine, follow the instructions below:

Requirements
Python 3.8 or higher

Required libraries:

gradio

soundfile

torch

numpy

ffmpeg-python

re (for sentence splitting)

You can install the required libraries using pip:

bash
Copy
Edit
pip install gradio soundfile torch numpy ffmpeg-python
Model Setup
EchoTales utilizes the Dia model from Nari Labs. The model will be loaded dynamically when you run the application.

Running the App
Clone or download the repository.

Install the required dependencies as listed above.

Navigate to the project folder in your terminal.

Run the following command:

bash
Copy
Edit
python app.py
This will launch the web interface in your browser.

How to Use the Application
Text Input: Enter the text you want to be narrated in the provided text box.

Generate Narration: Click the "Generate Narration" button. This will split the text into sentences, process them in batches, and generate audio for each sentence.

Adjust Speed: After the narration is generated, you can adjust the speed by modifying the WPM (Words Per Minute) with the slider.

Listen to Audio: You can play the generated audio directly from the interface.

Example Workflow
Input Text:

"EchoTales brings stories to life. It helps create amazing narrations with just a few clicks."

Generated Output: The application will generate a narration with the default WPM, and you can adjust the speed using the slider.

Final Audio: The app generates a .wav file of the narration, and you can listen to it directly through the interface.

Customization Options
WPM Slider: Allows you to fine-tune the speed of the narration.

Speed Factor: Displays how much the speed has changed after adjustments.

Device Info: Shows if the app is running on CPU or GPU for performance insights.

Troubleshooting
No Audio Generated: Ensure that your input text is not empty, and the application is running correctly.

Audio Too Fast or Slow: Adjust the WPM slider and ensure the speed factor is set correctly.

Model Loading Error: Ensure you have an active internet connection, as the model will be loaded from a pre-trained server.

License
This project is licensed under the MIT License - see the LICENSE file for details.# Story2Audio
