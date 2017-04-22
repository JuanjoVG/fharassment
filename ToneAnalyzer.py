import watson_developer_cloud as wdc


class ToneAnalyzer:
    tone_analyzer = wdc.ToneAnalyzerV3(
        username='636136e1-9740-4a0e-a327-dab642951f56',
        password='PSSCCRJAdrwe',
        version='2016-05-19')

    def analyze(self, text):
        tones = \
        self.tone_analyzer.tone(text=text, tones='emotion', sentences=False)['document_tone']['tone_categories'][0][
            'tones']
        return tones
