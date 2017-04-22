function drawSplineChart() {
    var chart = c3.generate({
        bindto: '#chart',
        data: {
            columns: [
                ['data1', 30, 200, 100, 400, 150, 250],
                ['data2', 130, 100, 140, 200, 150, 50]
            ],
            type: 'spline'
        }
    });
}

$(document).ready(function () {
    drawSplineChart();
});

