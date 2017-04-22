from os.path import join, dirname

import watson_developer_cloud as wdc

speech_to_text = wdc.SpeechToTextV1(
    username='0b627f9e-aaea-4dcd-8826-ba207481cde8',
    password='C0hPWUHiMBjb'
)

tone_analyzer = wdc.ToneAnalyzerV3(
    username='636136e1-9740-4a0e-a327-dab642951f56',
    password='PSSCCRJAdrwe',
    version='2016-05-19')

es_model = 'es-ES_NarrowbandModel'
en_model = 'en-UK_BroadbandModel'


def extract_text_from_speech(results):
    text = ""
    for analysis in results:
        for alternative in analysis['alternatives']:
            text += alternative['transcript'].capitalize() + '\n'
    return text


with open(join(dirname(__file__), 'media/juan trabajo.ogg'), 'rb') as audio_file:
    recognition = speech_to_text.recognize(audio_file, content_type='audio/ogg', timestamps=False,
                                           word_confidence=True, continuous=True, model=es_model)
    text = extract_text_from_speech(recognition['results'])
    print('The extracted text looks like: \n' + text)

    tones = tone_analyzer.tone(text=text, tones='emotion', sentences=False)['document_tone']['tone_categories'][0][
        'tones']
    sorted = sorted(tones, key=lambda k: k['score'], reverse=True)
    print('It sounds ' + sorted[0]['tone_id'])
