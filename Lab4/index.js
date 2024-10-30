// anychart.onDocumentReady(function () {

//     // create a data set on our data
//     var dataSet = anychart.data.set(getData());

//     // map data for the first series,
//     // take x from the zero column and value from the first column
//     var firstSeriesData = dataSet.mapAs({ x: 0, value: 1 });

//     // map data for the second series,
//     // take x from the zero column and value from the second column
//     var secondSeriesData = dataSet.mapAs({ x: 0, value: 2 });

//     // map data for the third series,
//     // take x from the zero column and value from the third column
//     var thirdSeriesData = dataSet.mapAs({ x: 0, value: 3 });

//     // map data for the fourth series,
//     // take x from the zero column and value from the fourth column
//     var fourthSeriesData = dataSet.mapAs({ x: 0, value: 4 });

//     // create a line chart
//     var chart = anychart.line();

//     // turn on the line chart animation
//     chart.animation(true);

//     // configure the chart title text settings
//     chart.title('Acceptance of same-sex relationships in the US over the last 2 decades');

//     // set the y axis title
//     chart.yAxis().title('% of people who accept same-sex relationships');

//     // turn on the crosshair
//     chart.crosshair().enabled(true).yLabel(false).yStroke(null);

//     // create the first series with the mapped data
//     var firstSeries = chart.line(firstSeriesData);
//     firstSeries
//         .name('18-34')
//         .stroke('3 #f49595')
//         .tooltip()
//         .format('Age group 18-34 : {%value}%');

//     // create the second series with the mapped data
//     var secondSeries = chart.line(secondSeriesData);
//     secondSeries
//         .name('35-49')
//         .stroke('3 #f9eb97')
//         .tooltip()
//         .format('Age group 35-49 : {%value}%');

//     // create the third series with the mapped data
//     var thirdSeries = chart.line(thirdSeriesData);
//     thirdSeries
//         .name('50-64')
//         .stroke('3 #a8d9f6')
//         .tooltip()
//         .format('Age group 50-64 : {%value}%');

//     // create the fourth series with the mapped data
//     var fourthSeries = chart.line(fourthSeriesData);
//     fourthSeries
//         .name('65+')
//         .stroke('3 #e2bbfd')
//         .tooltip()
//         .format('Age group 65+ : {%value}%');

//     // turn the legend on
//     chart.legend().enabled(true);

//     // set the container id for the line chart
//     chart.container('container');

//     // draw the line chart
//     chart.draw();

// });

function getData() {
    const fileInput = document.getElementById('fileInput');
    const fileContent = document.getElementById('fileContent');

    // Добавляем обработчик события на изменение файла
    fileInput.addEventListener('change', (event) => {
        const file = event.target.files[0]; // Получаем выбранный файл
        
        if (file) {
            const reader = new FileReader();

            // Настраиваем, что делать после загрузки файла
            reader.onload = function(e) {
                fileContent.textContent = e.target.result; // Отображаем содержимое файла
            };

            // Читаем файл как текст
            reader.readAsText(file);
        } else {
            fileContent.textContent = 'No file selected';
        }
    });
}
