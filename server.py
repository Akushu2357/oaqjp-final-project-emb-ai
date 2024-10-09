"""
module providing a function to used in the Application
likes flask, package in this app
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def get_home_page():
    """index home page"""
    return render_template("index.html")

@app.route("/emotionDetector")
def send_analyzer():
    """set routh api to send back result"""
    text_to_analyse = request.args.get('textToAnalyze')

    result = emotion_detector(text_to_analyse)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    displayed = "For the given statement, the system response is "
    for i in ['anger', 'disgust', 'fear', 'joy', 'sadness']:
        displayed += f"\'{i}\': {result[i]}, "
    displayed = displayed[:-2] + f". The dominant emotion is {result['dominant_emotion']}"
    return displayed

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
