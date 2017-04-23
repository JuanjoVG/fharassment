function drawSplineChart() {
    var chart = c3.generate({
        bindto: '#chart',
        data: {
            json: [
                {name: 'www.site1.com', upload: 200, download: 200, total: 400},
                {name: 'www.site2.com', upload: 100, download: 300, total: 400},
                {name: 'www.site3.com', upload: 300, download: 200, total: 500},
                {name: 'www.site4.com', upload: 400, download: 100, total: 500},
            ],
            keys: {
//                x: 'name', // it's possible to specify 'x' when category axis
                value: ['upload', 'download'],
            },
            type: "spline"
        },
        axis: {
            x: {
//                type: 'category'
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
