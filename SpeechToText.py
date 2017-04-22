from os.path import join, dirname

import watson_developer_cloud as wdc


class SpeechToText:
    en_model = 'en-UK_BroadbandModel'

    speech_to_text = wdc.SpeechToTextV1(
        username='0b627f9e-aaea-4dcd-8826-ba207481cde8',
        password='C0hPWUHiMBjb'
    )

    def extract_text_from_speech(self, results):
        text = ""
        for analysis in results:
            for alternative in analysis['alternatives']:
                text += alternative['transcript'].capitalize() + '\n'
        return text

    def parse_watson(self, file_path, model='es-ES_NarrowbandModel'):
        with open(join(dirname(__file__), file_path), 'rb') as audio_file:
            recognition = self.speech_to_text.recognize(audio_file, content_type='audio/ogg', timestamps=False,
                                                        word_confidence=True, continuous=True, model=model)
            text = self.extract_text_from_speech(recognition['results'])
        return text
