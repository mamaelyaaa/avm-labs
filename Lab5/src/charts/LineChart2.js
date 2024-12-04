export function dependencyChart2(
  rungeKuttaInitResults,
  rungeKuttaCloseResults,
  rungeKutta2Results,
  rungeKutta4Results,
  rungeKutta6Results,
  rungeKutta8Results
) {
  const ctx = document.getElementById("chart").getContext("2d");

  const rungeKuttaInitData = {
    label: "Метод Рунге-Кутты (dx = 0.05)",
    data: rungeKuttaInitResults.map((point) => ({ x: point.x, y: point.y })),
    borderColor: "rgba(255, 159, 64, 0.8)",
    backgroundColor: "rgba(255, 159, 64, 0.2)",
    tension: 0.4,
  };

  const rungeKuttaCloseData = {
    label: "Метод Рунге-Кутты (dx = 0.005)",
    data: rungeKuttaCloseResults.map((point) => ({ x: point.x, y: point.y })),
    borderColor: "rgba(135, 206, 235, 0.7)",
    backgroundColor: "rgba(135, 206, 235, 0.2)",
    tension: 0.4,
  };

  const rungeKutta2Data = {
    label: "Метод Рунге-Кутты (dx = 0.025)",
    data: rungeKutta2Results.map((point) => ({ x: point.x, y: point.y })),
    borderColor: 'rgba(0, 128, 0, 0.5)',
    backgroundColor: 'rgba(0, 128, 0, 0.2)',
    tension: 0.4,
  };

  const rungeKutta4Data = {
    label: "Метод Рунге-Кутты (dx = 0.0125)",
    data: rungeKutta4Results.map((point) => ({ x: point.x, y: point.y })),
    borderColor: 'rgba(255, 99, 71, 0.6)',
    backgroundColor: 'rgba(255, 99, 71, 0.2)',
    tension: 0.4,
  };

  const rungeKutta6Data = {
    label: "Метод Рунге-Кутты (dx = 0.0083)",
    data: rungeKutta6Results.map((point) => ({ x: point.x, y: point.y })),
    borderColor: 'rgba(75, 192, 192, 0.6)',
    backgroundColor: 'rgba(75, 192, 192, 0.2)',
    tension: 0.4,
  };

  const rungeKutta8Data = {
    label: "Метод Рунге-Кутты (dx = 0.00625)",
    data: rungeKutta8Results.map((point) => ({ x: point.x, y: point.y })),
    borderColor: 'rgba(0, 0, 192, 0.6)',
    backgroundColor: 'rgba(0, 0, 192, 0.2)',
    tension: 0.4,
  };

  const chart = new Chart(ctx, {
    type: "line",
    data: {
      datasets: [rungeKuttaInitData, rungeKuttaCloseData, rungeKutta2Data, rungeKutta4Data, rungeKutta6Data, rungeKutta8Data],
    },
    options: {
      responsive: true,
      scales: {
        x: {
          type: "linear",
          position: "bottom",

          // Включить для понимания
          max: -1.8,

          ticks: {
            color: "#6B7280",
            callback: function (value) {
              return value.toFixed(2); // Отображаем значения с точностью до 2 знаков после запятой
            },
          },
        },
        y: {
          type: "linear",
          position: "bottom",
          min: -0.46,
          max: -0.28,
          ticks: {
            color: "#6B7280",
            callback: function (value) {
              return value.toFixed(4);
            },
          },
        },
      },
      plugins: {
        zoom: {
          // pan: {
          //   enabled: true, // Включить панорамирование
          //   mode: 'x', // Панорамирование по оси X
          //   modifierKey: null, // Уберите для перемещения без зажатия клавиш
          // },
          zoom: {
            wheel: {
              enabled: true, // Включить масштабирование колесиком мыши
            },
            mode: 'xy', // Масштабирование по оси X
          },
        },
      },
    },
  });

  document.getElementById("changeScale").addEventListener("click", () => {
    chart.options.scales.x.min = -1.91;
    chart.options.scales.x.max = -1.89;

    chart.options.scales.y.min = -0.335;
    chart.options.scales.y.max = -0.345;
    chart.update();
  });
}
