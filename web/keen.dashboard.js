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

$('#myForm').submit(function(e){
    e.preventDefault();
    $.ajax({
        url:'/Car/Edit/17/',
        type:'post',
        data:$('#myForm').serialize(),
        success:function(){
            //whatever you wanna do after the form is successfully submitted
        }
    });
});

$(document).ready(function () {
    drawSplineChart();
});

