import json
import re

import flask
from flask import Flask, request, abort
from flask_cors import CORS

from HarassmentDetector import HarassmentDetector
from SpeechToText import SpeechToText
from ToneAnalyzer import ToneAnalyzer

app = Flask(__name__)
CORS(app)
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
    for a in sentiments_by_author:
        sentiments = sentiments_by_author[a]
        for s in sentiments:
            scores.append(sentiments[s])
    return scores


def get_harassment_response(harassment):
    return harassment.tolist()


def get_days(parsed_text):
    days = []
    for user in parsed_text.keys():
        for pt in parsed_text[user]["messages"]:
            days.append(pt["time"].split(" ")[0])

    return list(set(days))


def filter_by_day(parsed_text, d):
    new_paresd_text = {}
    for user in parsed_text.keys():
        new_paresd_text[user] = {"transcript": ""}
        for pt in parsed_text[user]["messages"]:
            if pt["time"].split(" ")[0] == d:
                new_paresd_text[user]["transcript"] += pt['text'] + "\n"

    return new_paresd_text


@app.route("/recognize", methods=["POST"])
def hello():
    recognition_type = request.args.get("type")
    if recognition_type:
        if recognition_type == "text":
            whats_app_file = request.data.decode("utf-8")
            parsed_text = parse_whats_app_chat(whats_app_file)

            days = get_days(parsed_text)

            response = []
            for user in parsed_text.keys():
                response.append({"id": user, 'values': []})

            for d in days:
                parsed_text_day = filter_by_day(parsed_text, d)
                tone_scores = analyze_sentiments(parsed_text_day)
                harassment = detect_harassment(tone_scores)

                print(tone_scores)
                print(get_harassment_response(harassment))

                new_obj = tone_scores[response[0]["id"]]
                new_obj['date'] = d
                new_obj['tensor'] = get_harassment_response(harassment)
                response[0]['values'].append(new_obj)

                new_obj = {}
                new_obj = tone_scores[response[1]["id"]]
                new_obj['date'] = d
                new_obj['tensor'] = get_harassment_response(harassment)
                response[1]['values'].append(new_obj)

            # response = get_harassment_response(harassment)
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


@app.route("/dummy", methods=["POST"])
def bye():
    startdata = [
        {'id': "sergio", 'values':[
            {'date': '2016-05-16', 'anger': 0.9, 'disgust': 0.4, 'fear': 0.01, 'joy': 0.1, 'sadness': 0.3, 'tensor': [1, 0, 0]},
            {'date': '2016-05-17', 'anger': 0.8, 'disgust': 0.4, 'fear': 0.01, 'joy': 0.1, 'sadness': 0.3, 'tensor': [0, 0, 1]},
            {'date': '2016-05-18', 'anger': 0.34, 'disgust': 0.2, 'fear': 0.01, 'joy': 0.1, 'sadness': 0.3, 'tensor': [1, 0, 0]},
            {'date': '2016-05-19', 'anger': 0.24, 'disgust': 0.5, 'fear': 0.6, 'joy': 0.01, 'sadness': 0.2, 'tensor': [1, 0, 0]},
            {'date': '2016-05-20', 'anger': 0.21, 'disgust': 0.2, 'fear': 0.01, 'joy': 0.4, 'sadness': 0.01, 'tensor': [1, 0, 0]},
            {'date': '2016-05-21', 'anger': 0.2, 'disgust': 0.2, 'fear': 0.01, 'joy': 0.02, 'sadness': 0.7, 'tensor': [1, 0, 0]},
            {'date': '2016-05-22', 'anger': 0.1, 'disgust': 0.2, 'fear': 0.01, 'joy': 0.89, 'sadness': 0.3, 'tensor': [1, 0, 0]}
        ]},
        {'id': "juanjo", 'values': [
            {'date': '2016-05-16', 'anger': 0.9, 'disgust': 0.4, 'fear': 0.01, 'joy': 0.1, 'sadness': 0.3,
             'tensor': [1, 0, 0]},
            {'date': '2016-05-17', 'anger': 0.8, 'disgust': 0.4, 'fear': 0.01, 'joy': 0.1, 'sadness': 0.3,
             'tensor': [0, 0, 1]},
            {'date': '2016-05-18', 'anger': 0.34, 'disgust': 0.2, 'fear': 0.01, 'joy': 0.1, 'sadness': 0.3,
             'tensor': [1, 0, 0]},
            {'date': '2016-05-19', 'anger': 0.24, 'disgust': 0.5, 'fear': 0.6, 'joy': 0.01, 'sadness': 0.2,
             'tensor': [1, 0, 0]},
            {'date': '2016-05-20', 'anger': 0.21, 'disgust': 0.2, 'fear': 0.01, 'joy': 0.4, 'sadness': 0.01,
             'tensor': [1, 0, 0]},
            {'date': '2016-05-21', 'anger': 0.2, 'disgust': 0.2, 'fear': 0.01, 'joy': 0.02, 'sadness': 0.7,
             'tensor': [1, 0, 0]},
            {'date': '2016-05-22', 'anger': 0.1, 'disgust': 0.2, 'fear': 0.01, 'joy': 0.89, 'sadness': 0.3,
             'tensor': [1, 0, 0]}
        ]}
    ]
    return json.dumps(startdata, indent=2)
    abort(400);


if __name__ == "__main__":
    app.run()
