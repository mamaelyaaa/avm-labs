export function dependencyChart(eulerResults, rungeKuttaResults) {
    const ctx = document.getElementById("chart").getContext("2d");
  
    const eulerData = {
      label: "Метод Эйлера",
      data: eulerResults.map((point) => ({ x: point.x, y: point.y })),
      borderColor: "blue",
      fill: false,
    };
  
    const rungeKuttaData = {
      label: "Метод Рунге-Кутты",
      data: rungeKuttaResults.map((point) => ({ x: point.x, y: point.y })),
      borderColor: "red",
      fill: false,
    };
  
    new Chart(ctx, {
      type: "line",
      data: {
        datasets: [eulerData, rungeKuttaData],
      },
      options: {
        scales: {
          x: {
            type: "linear",
            position: "bottom",
          },
        },
      },
    });
  }
  