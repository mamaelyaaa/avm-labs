export function barChart(absoluteErrors) {
  const ctx = document.getElementById("errorChart").getContext("2d");

  const data = {
    labels: ["Э", "МЭ", "РК"],
    datasets: [
      {
        label: "Абсолютная ошибка",
        data: [
          absoluteErrors.Euler,
          absoluteErrors.EulerMod,
          absoluteErrors.RungeKutta,
        ],
        backgroundColor: [
          "rgba(255, 99, 132, 0.2)",
          "rgba(54, 162, 235, 0.2)",
          "rgba(75, 192, 192, 0.2)",
        ],
        borderColor: [
          "rgba(255, 99, 132, 1)",
          "rgba(54, 162, 235, 1)",
          "rgba(75, 192, 192, 1)",
        ],
        borderWidth: 1,
      },
    ],
  };

  // Конфигурация графика
  const options = {
    responsive: true,
    scales: {
      y: {
        beginAtZero: true,
        title: {
          display: true,
          text: "Абсолютная ошибка",
        },
      },
      x: {
        title: {
          display: true,
          text: "Методы",
        },
      },
    },
  };

  // Создаем график
  new Chart(ctx, {
    type: "bar",
    data: data,
    options: options,
  });
}
