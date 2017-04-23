import io

import watson_developer_cloud as wdc
from google.cloud import speech


class SpeechToText:
    en_model = 'en-UK_BroadbandModel'

    speech_to_text = wdc.SpeechToTextV1(
        username='0b627f9e-aaea-4dcd-8826-ba207481cde8',
        password='C0hPWUHiMBjb'
    )

    speech_client = speech.Client()

    def extract_text_from_speech(self, results):
        text = ""
        for analysis in results:
            for alternative in analysis['alternatives']:
                text += alternative['transcript'].capitalize() + '\n'
        return text

    def parse_watson(self, file_path, model='es-ES_NarrowbandModel'):
        with io.open(file_path, 'rb') as audio_file:
            recognition = self.speech_to_text.recognize(audio_file, content_type='audio/ogg', timestamps=False,
                                                        word_confidence=True, continuous=True, model=model)
            text = self.extract_text_from_speech(recognition['results'])
        return text

    def transcript_from_file(self, file_path, model='es-ES'):
        """Transcribe the given audio file."""
        with io.open(file_path, 'rb') as audio_file:
            text = self.transcript_audio(audio_file, model)
            return text

    def transcript_audio(self, audio_file, model='es-ES'):
        content = audio_file.read()
        audio_sample = self.speech_client.sample(
            content=content,
            source_uri=None,
            encoding='LINEAR16',
            sample_rate_hertz=44100)

        alternatives = audio_sample.recognize(model)
        text = ""
        for alternative in alternatives:
            text += alternative.transcript.capitalize() + '\n'
        return text
