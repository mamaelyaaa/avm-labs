export function errorPointsChart(errorData) {
  const ctx = document.getElementById("errorPointsChart").getContext("2d");

  new Chart(ctx, {
    type: "line",
    data: {
      labels: errorData.map((data) => data.totalPoints),
      datasets: [
        {
          label: "Абсолютная ошибка",
          data: errorData.map((data) => data.absoluteError),
          borderColor: "rgba(75, 192, 192, 0.8)",
          backgroundColor: "rgba(75, 192, 192, 0.2)",
          tension: 0.4,
        },
      ],
    },
    options: {
      responsive: true,
      scales: {
        x: {
          title: {
            display: true,
            text: "Количество точек интегрирования",
          },
          ticks: {
            color: "#6B7280",
          },
        },
        y: {
          title: {
            display: true,
            text: "Абсолютная ошибка",
          },
          ticks: {
            color: "#6B7280",
            callback: function (value) {
              return value.toExponential(2); // Вывод в экспоненциальной нотации
            },
          },
        },
      },
    },
  });
}
