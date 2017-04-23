import json
import re

from flask import Flask, request, abort

from SpeechToText import SpeechToText

app = Flask(__name__)
speech_to_text = SpeechToText()


def parse_whats_app_chat(whats_app_file):
    regex = r"(\d{1,2}\/\d{1,2}\/\d{2}),\s(\d{2}\:\d{2})\s-\s([^:]*)\:\s([^\n]+)"
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
            info[author]["messages"].append({"text":  message, "time": timestamp})
            info[author]["transcript"] += message+"\n"

    return info


@app.route("/recognize", methods=["POST"])
def hello():
    recognition_type = request.args.get("type")
    if recognition_type:
        if recognition_type == "text":
            whats_app_file = request.data.decode("utf-8")
            return json.dumps(parse_whats_app_chat(whats_app_file), indent=2)
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
