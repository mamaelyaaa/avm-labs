anychart.onDocumentLoad(function () {
    let dataSet = anychart.data.set(getData());
    let chart = anychart.scatter(dataSet);

    chart.title("Экспериментальные точки");

    chart.yAxis().title('y');
    chart.xAxis().title('x');

    chart.animation(true);
    chart.container("container");
    chart.draw();
});

function getData() {
    return [
        [ -3.3, -24.78 ],
        [ -2.85, -21.03 ],
        [ -2.4, -17.76 ],
        [ -1.95, -14.94 ],
        [ -1.5, -12.45 ],
        [ -1.05, -10.41 ],
        [ -0.6, -8.58 ],
        [ -0.15, -7.02 ],
        [ 0.3, -5.69 ],
        [ 0.75, -4.63 ],
        [ 1.2, -3.58 ],
        [ 1.65, -2.67 ]
    ]
}