import json
import re

import flask
from flask import Flask, request, abort

from HarassmentDetector import HarassmentDetector
from SpeechToText import SpeechToText
from ToneAnalyzer import ToneAnalyzer

app = Flask(__name__)
speech_to_text = SpeechToText()
tone_analyzer = ToneAnalyzer()


def parse_whats_app_chat(whats_app_file):
    regex = r"(\d{1,2}\/\d{1,2}\/\d{2}),\s(\d{1,2}\:\d{2})\s-\s([^:]*)\:\s([^\n]+)"
    matches = re.finditer(regex, whats_app_file, re.DOTALL)

    info = {}
    for match in matches:
        if len(match.groups()) == 4:
            groups = match.groups()
            timestamp = groups[0] + " " + groups[1]
            author = groups[2]
            message = groups[3]
            if author not in info.keys():
                info[author] = {"messages": [], "transcript": ""}
            info[author]["messages"].append({"text": message, "time": timestamp})
            info[author]["transcript"] += message + "\n"

    return info


def analyze_sentiments(parsed_text):
    tone_scores = {}
    for author in parsed_text.keys():
        tone_scores[author] = tone_analyzer.analyze(parsed_text[author]["transcript"])
    return tone_scores


def detect_harassment(sentiments_by_author):
    scores = get_scores(sentiments_by_author)
    hd = HarassmentDetector()
    hd.init()
    result = hd.detect(scores)
    return result


def get_scores(sentiments_by_author):
    scores = []
    print(sentiments_by_author)
    for a in sentiments_by_author:
        sentiments = sentiments_by_author[a]
        for s in sentiments:
            scores.append(sentiments[s])
    return scores


def get_harassment_response(harassment):
    return harassment.tolist()

@app.route("/recognize", methods=["POST"])
def hello():
    recognition_type = request.args.get("type")
    if recognition_type:
        if recognition_type == "text":
            whats_app_file = request.data.decode("utf-8")
            parsed_text = parse_whats_app_chat(whats_app_file)
            tone_scores = analyze_sentiments(parsed_text)
            harassment = detect_harassment(tone_scores)
            response = get_harassment_response(harassment)
            return json.dumps(response, indent=2)
        # elif recognition_type == "audio":
        else:
            uploaded_files = flask.request.files.getlist("file[]")
            print(uploaded_files)
            audio_file = request.files['audio']
            transcription = speech_to_text.transcript_audio(audio_file.stream)
            return transcription
            # else:
            #     abort(400)
    else:
        abort(400)


if __name__ == "__main__":
    app.run(debug=True)
