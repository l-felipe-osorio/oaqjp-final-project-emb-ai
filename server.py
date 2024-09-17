from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("\emotionDetector")
def emotion_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    return "For the given statement, the system response is {}, {}, {}, {}, and {}. The dominant emotion is {}".format(response['anger'], response['disgust'], response['fear'], response['joy'], response['dominant_emotion'])

@app.route("/")
def render_index_page():
    return render_template('index.html')