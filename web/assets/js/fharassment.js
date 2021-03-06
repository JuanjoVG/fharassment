var startdata = [
    {date: '2016-05-16', anger: 0.9, disgust: 0.4, fear: 0.01, joy: 0.1, sadness: 0.3, tensor: [1, 0, 0]},
    {date: '2016-05-17', anger: 0.8, disgust: 0.4, fear: 0.01, joy: 0.1, sadness: 0.3, tensor: [0, 0, 1]},
    {date: '2016-05-18', anger: 0.34, disgust: 0.2, fear: 0.01, joy: 0.1, sadness: 0.3, tensor: [1, 0, 0]},
    {date: '2016-05-19', anger: 0.24, disgust: 0.5, fear: 0.6, joy: 0.01, sadness: 0.2, tensor: [1, 0, 0]},
    {date: '2016-05-20', anger: 0.21, disgust: 0.2, fear: 0.01, joy: 0.4, sadness: 0.01, tensor: [1, 0, 0]},
    {date: '2016-05-21', anger: 0.2, disgust: 0.2, fear: 0.01, joy: 0.02, sadness: 0.7, tensor: [1, 0, 0]},
    {date: '2016-05-22', anger: 0.1, disgust: 0.2, fear: 0.01, joy: 0.89, sadness: 0.3, tensor: [1, 0, 0]}
];

var response = [
    {date: '2016-05-16', anger: 0.9, disgust: 0.4, fear: 0.01, joy: 0.1, sadness: 0.3, tensor: [1, 0, 0]},
    {date: '2016-05-17', anger: 0.8, disgust: 0.4, fear: 0.01, joy: 0.1, sadness: 0.3, tensor: [0, 0, 1]},
    {date: '2016-05-18', anger: 0.34, disgust: 0.2, fear: 0.01, joy: 0.1, sadness: 0.3, tensor: [1, 0, 0]}
];

var chart = "";

var dataA, dataB;

function drawSplineChart() {
    var a = {
        data: {
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
    };
    a.bindto = '#chart1';
    a.data.json = dataA;
    var chart = c3.generate(a);
    var a2 = a;
    a2.bindto = '#chart2';
    a2.data.json = dataB;
    var chart2 = c3.generate(a2);
}

$('#myForm').submit(function(e){
    e.preventDefault();
    $.ajax({
        url: 'http://ab95aeee.ngrok.io/dummy',
        type:'post',
        dataType: 'text',
        data:$('#myForm').serialize(),
        success:function(data){
            var parse = JSON.parse(data);
            dataA = parse[0].values;
            dataB = parse[1].values;
            drawSplineChart();
        }
    });
});


$(document).ready(function () {
    // drawSplineChart();
});
