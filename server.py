"""Flask application for emotion detection using Watson NLP API."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector  # Import Emotion Detector

app = Flask(__name__)  # Initialize Flask application

@app.route("/emotionDetector")
def emotion_detector_endpoint():
    """Endpoint to analyze text and determine dominant emotion."""
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return "No text provided. Please supply text to analyze."

    response = emotion_detector(text_to_analyze)
    if response is None:
        return "Error processing the request. Please try again."

    dominant_emotion = response.pop('dominant_emotion', None)
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    emotions_text = ', '.join(f"'{emotion}': {score}" for emotion, score in response.items())
    return f"For the given statement, the system response is {emotions_text}. \
        The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    """Renders the main index page from a template."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Run the Flask application
