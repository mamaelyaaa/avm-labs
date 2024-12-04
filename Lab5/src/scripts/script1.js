import { parseJSON } from "../jsonParser.js";
import sampleData from "../data.json" with { type: "json" };
import { solveEuler } from "../methods/Euler.js";
import { solveModEuler } from "../methods/ModEuler.js";
import { solveRungeKutta } from "../methods/RungeKutt.js";
import { dependencyChart1 } from "../charts/LineChart1.js";

try {
  const data = parseJSON(JSON.stringify(sampleData));
  const { coefficients, init, step, dot } = data;

  // График 1
  const eulerResults = solveEuler({ coefficients, init, step, dot });
  const eulerModResults = solveModEuler({ coefficients, init, step, dot });
  const rungeKuttaResults = solveRungeKutta({ coefficients, init, step, dot });
  const rungeKuttaCloseResults = solveRungeKutta({
    coefficients,
    init,
    step: step / 10,
    dot,
  });

  dependencyChart1(
    eulerResults,
    eulerModResults,
    rungeKuttaResults,
    rungeKuttaCloseResults
  );
} catch (error) {
  console.error("Ошибка выполнения программы:", error);
}
