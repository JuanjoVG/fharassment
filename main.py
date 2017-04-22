import watson_developer_cloud as wdc

from SpeechToText import SpeechToText

tone_analyzer = wdc.ToneAnalyzerV3(
    username='636136e1-9740-4a0e-a327-dab642951f56',
    password='PSSCCRJAdrwe',
    version='2016-05-19')

speechToText = SpeechToText()
text = speechToText.parse_watson('media/juan trabajo.ogg')
tones = tone_analyzer.tone(text=text, tones='emotion', sentences=False)['document_tone']['tone_categories'][0][
    'tones']
print(tones)
# print('The extracted text looks like: \n' + text)

# sorted = sorted(tones, key=lambda k: k['score'], reverse=True)
# print('It sounds ' + sorted[0]['tone_id'])
