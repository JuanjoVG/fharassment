import json
import re

from flask import Flask, request, abort

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


def is_there_being_harassment(sentiments_by_author):
    pass


@app.route("/recognize", methods=["POST"])
def hello():
    recognition_type = request.args.get("type")
    if recognition_type:
        if recognition_type == "text":
            whats_app_file = request.data.decode("utf-8")
            parsed_text = parse_whats_app_chat(whats_app_file)
            tone_scores = analyze_sentiments(parsed_text)
            # if is_there_being_harassment(tone_scores):
            #     return "Looks like " + author + " is being harassed"
            # else:
            #     return "I can't conclude anything"
            return json.dumps(tone_scores, indent=2)
        elif recognition_type == "audio":
            audio_file = request.files
            speech_to_text.parse_google()
            return "audio"
        else:
            abort(400)
    else:
        abort(400)


if __name__ == "__main__":
    app.run()
