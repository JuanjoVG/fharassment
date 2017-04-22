import json
from os.path import join, dirname

import watson_developer_cloud as wdc

speech_to_text = wdc.SpeechToTextV1(
    username='0b627f9e-aaea-4dcd-8826-ba207481cde8',
    password='C0hPWUHiMBjb'
)

es_model = 'es-ES_NarrowbandModel'
en_model = 'en-UK_BroadbandModel'

with open(join(dirname(__file__), 'media/juan trabajo.ogg'), 'rb') as audio_file:
    data = json.dumps(
        speech_to_text.recognize(audio_file, content_type='audio/ogg', timestamps=False, word_confidence=True,
                                 continuous=True, model=es_model), indent=2)
    print(data)