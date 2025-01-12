import os
from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])  # Allow GET requests for this route
def emotion_detector_route():
    text_to_analyze = request.args.get('textToAnalyze')  # Retrieve the textToAnalyze parameter from the GET request

    if text_to_analyze:
        result = emotion_detector(text_to_analyze)  # Perform emotion detection
        # Return the result as a simple string or formatted HTML, depending on your needs
        result_text = f"Emotion Detection Results: {result}"
        return result_text
    return "No text provided for analysis", 400  # Return an error if no text is provided

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Get the port from the environment variables
    app.run(host="0.0.0.0", port=port)        # Bind to 0.0.0.0 and the correct port