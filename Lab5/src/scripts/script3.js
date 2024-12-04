import { parseJSON } from "../jsonParser.js";
import sampleData from "../data.json" with { type: "json" };
import { solveEuler } from "../methods/Euler.js";
import { solveModEuler } from "../methods/ModEuler.js";
import { solveRungeKutta } from "../methods/RungeKutt.js";
import { barChart } from "../charts/BarChart.js";

try {
  const data = parseJSON(JSON.stringify(sampleData));
  const { coefficients, init, step, dot } = data;

  // График 2
  const eulerResults = solveEuler({ coefficients, init, step, dot });
  const eulerModResults = solveModEuler({ coefficients, init, step, dot });

  const rungeKuttaResults = solveRungeKutta({ coefficients, init, step, dot });
  const rungeKuttaCloseResults = solveRungeKutta({
    coefficients,
    init,
    step: step / 10,
    dot,
  });

  const findValueAtDot = (results, dot) =>
    results.find((point) => Math.abs(point.x - dot) < 1e-6).y;

  const referenceValue = findValueAtDot(rungeKuttaCloseResults, dot); // Эталонное значение
  const eulerValue = findValueAtDot(eulerResults, dot);
  const eulerModValue = findValueAtDot(eulerModResults, dot);
  const rungeKuttaValue = findValueAtDot(rungeKuttaResults, dot);

  const absoluteErrors = {
    Euler: Math.abs(eulerValue - referenceValue),
    EulerMod: Math.abs(eulerModValue - referenceValue),
    RungeKutta: Math.abs(rungeKuttaValue - referenceValue),
  };

  console.log("Абсолютные ошибки:", absoluteErrors);

  barChart(absoluteErrors);
} catch (error) {
  console.error("Ошибка выполнения программы:", error);
}
