import { parseJSON } from "../jsonParser.js";
import sampleData from "../data.json" with { type: "json" };
import { solveRungeKutta } from "../methods/RungeKutt.js";
import { calculateErrorDependence } from "./calculateErrorDependence.js";
import { errorPointsChart } from "../charts/errorPointsChart.js";

try {
  const data = parseJSON(JSON.stringify(sampleData));
  const { coefficients, init, step, dot } = data;

  const steps = [step, step / 2, step / 4, step / 6, step / 8]; // Шаги уменьшения
  const rungeKuttaCloseResults = solveRungeKutta({
    coefficients,
    init,
    step: step / 10,
    dot,
  });

  const findValueAtDot = (results, dot) =>
    results.find((point) => Math.abs(point.x - dot) < 1e-6).y;

  const referenceValue = findValueAtDot(rungeKuttaCloseResults, dot); // Эталонное значение
  const errorData = calculateErrorDependence({
    coefficients,
    init,
    dot,
    steps,
    referenceValue,
  });
//   console.log("Ошибки", errorData)

  errorPointsChart(errorData); // Построение графика
} catch (error) {
  console.error("Ошибка выполнения программы:", error);
}
