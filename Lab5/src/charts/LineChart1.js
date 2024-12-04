export function dependencyChart1(
  eulerResults,
  eulerModResults,
  rungeKuttaResults,
  rungeKuttaCloseResults
) {
  const ctx = document.getElementById("chart").getContext("2d");

  const eulerData = {
    label: "Метод Эйлера",
    data: eulerResults.map((point) => ({ x: point.x, y: point.y })),
    borderColor: "rgba(255, 99, 71, 0.6)",
    backgroundColor: "rgba(255, 99, 71, 0.2)",
    tension: 0.4,
  };

  const eulerModData = {
    label: "Модифицированный метод Эйлера",
    data: eulerModResults.map((point) => ({ x: point.x, y: point.y })),
    borderColor: "rgba(75, 192, 192, 0.8)",
    backgroundColor: "rgba(75, 192, 192, 0.2)",
    tension: 0.4,
  };

  const rungeKuttaData = {
    label: "Метод Рунге-Кутты (dx = 0.05)",
    data: rungeKuttaResults.map((point) => ({ x: point.x, y: point.y })),
    borderColor: "rgba(255, 159, 64, 0.8)",
    backgroundColor: "rgba(255, 159, 64, 0.2)",
    tension: 0.4,
  };

  const rungeKuttaCloseData = {
    label: "Метод Рунге-Кутты (dx = 0.005)",
    data: rungeKuttaCloseResults.map((point) => ({ x: point.x, y: point.y })),
    borderColor: 'rgba(135, 206, 235, 0.7)',
    backgroundColor: 'rgba(135, 206, 235, 0.2)',
    tension: 0.4,
  };

  // Создаем график
  new Chart(ctx, {
    type: "line",
    data: {
      datasets: [eulerData, eulerModData, rungeKuttaData, rungeKuttaCloseData],
    },
    options: {
      responsive: true,
      scales: {
        x: {
          type: "linear",
          position: "bottom",
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
    },
  });
}
