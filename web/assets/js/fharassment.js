function drawSplineChart() {
    var chart = c3.generate({
        bindto: '#chart',
        data: {
            json: [
                {date: '2016-05-16', anger: 0.9, disgust: 0.4, fear: 0.01, joy: 0.1, sadness: 0.3},
                {date: '2016-05-17', anger: 0.8, disgust: 0.4, fear: 0.01, joy: 0.1, sadness: 0.3},
                {date: '2016-05-18', anger: 0.34, disgust: 0.2, fear: 0.01, joy: 0.1, sadness: 0.3},
                {date: '2016-05-19', anger: 0.24, disgust: 0.5, fear: 0.6, joy: 0.01, sadness: 0.2},
                {date: '2016-05-20', anger: 0.21, disgust: 0.2, fear: 0.01, joy: 0.4, sadness: 0.01},
                {date: '2016-05-21', anger: 0.2, disgust: 0.2, fear: 0.01, joy: 0.02, sadness: 0.7},
                {date: '2016-05-22', anger: 0.1, disgust: 0.2, fear: 0.01, joy: 0.89, sadness: 0.3}
            ],
            keys: {
                x: 'date',
                value: ['anger', 'disgust', 'fear', 'joy', 'sadness']
            },
            type: "spline"
        },
        axis: {
            x: {
                type: 'timeseries',
                tick: {
                    format: function (x) {
                        return x.getDay()+'/'+x.getMonth()+'/'+x.getFullYear();
                    }
                }
            }
        }
    });
}

$('#myForm').submit(function(e){
    e.preventDefault();
    $.ajax({
        url: 'http://f74e6a99.ngrok.io:5000/recognize',
        type:'post',
        data:$('#myForm').serialize(),
        success:function(data){
            data = {
                      "document_tone": {
                        "tone_categories": [
                          {
                            "tones": [
                              {
                                "score": 0.637592,
                                "tone_id": "anger",
                                "tone_name": "Anger"
                              },
                              {
                                "score": 0.458892,
                                "tone_id": "disgust",
                                "tone_name": "Disgust"
                              },
                              {
                                "score": 0.498639,
                                "tone_id": "fear",
                                "tone_name": "Fear"
                              },
                              {
                                "score": 0.534475,
                                "tone_id": "joy",
                                "tone_name": "Joy"
                              },
                              {
                                "score": 0.205761,
                                "tone_id": "sadness",
                                "tone_name": "Sadness"
                              }
                            ],
                            "category_id": "emotion_tone",
                            "category_name": "Emotion Tone"
                          },
                          {
                            "tones": [
                              {
                                "score": 0.182791,
                                "tone_id": "analytical",
                                "tone_name": "Analytical"
                              },
                              {
                                "score": 0.619851,
                                "tone_id": "confident",
                                "tone_name": "Confident"
                              },
                              {
                                "score": 0,
                                "tone_id": "tentative",
                                "tone_name": "Tentative"
                              }
                            ],
                            "category_id": "language_tone",
                            "category_name": "Language Tone"
                          },
                          {
                            "tones": [
                              {
                                "score": 0.165912,
                                "tone_id": "openness_big5",
                                "tone_name": "Openness"
                              },
                              {
                                "score": 0.002341,
                                "tone_id": "conscientiousness_big5",
                                "tone_name": "Conscientiousness"
                              },
                              {
                                "score": 0.603771,
                                "tone_id": "extraversion_big5",
                                "tone_name": "Extraversion"
                              },
                              {
                                "score": 0.009166,
                                "tone_id": "agreeableness_big5",
                                "tone_name": "Agreeableness"
                              },
                              {
                                "score": 0.036585,
                                "tone_id": "emotional_range_big5",
                                "tone_name": "Emotional Range"
                              }
                            ],
                            "category_id": "social_tone",
                            "category_name": "Social Tone"
                          }
                        ]
                      }
                    }
        }
    });
});

$(document).ready(function () {
    drawSplineChart();
});
