from SpeechToText import SpeechToText
from ToneAnalyzer import ToneAnalyzer

speechToText = SpeechToText()
text = speechToText.transcript_from_file('media/sergiomalo.wav')

toneAnalyzer = ToneAnalyzer()
tones_score = toneAnalyzer.analyze(text)

print(tones_score)
# print('The extracted text looks like: \n' + text)

# sorted = sorted(tones, key=lambda k: k['score'], reverse=True)
# print('It sounds ' + sorted[0]['tone_id'])
