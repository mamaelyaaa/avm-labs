import { parseJSON } from "../jsonParser.js";
import sampleData from "../data.json" with { type: "json" };
import { solveRungeKutta } from "../methods/RungeKutt.js";
import { dependencyChart2 } from "../charts/LineChart2.js";

try {
  const data = parseJSON(JSON.stringify(sampleData));
  const { coefficients, init, step, dot } = data;

  // График 2
  const rungeKuttaInitResults = solveRungeKutta({
    coefficients,
    init,
    step,
    dot,
  });
  console.log(
    "Метод Рунге-Кутты\n",
    rungeKuttaInitResults[14].y,
    "\nШаг", step
  );
  const rungeKuttaCloseResults = solveRungeKutta({
    coefficients,
    init,
    step: step / 10,
    dot,
  });
  console.log(
    "Метод Рунге-Кутты\n",
    rungeKuttaCloseResults[140].y,
    "\nШаг", step / 10
  );
  const rungeKutta2Results = solveRungeKutta({
    coefficients,
    init,
    step: step / 2,
    dot,
  });
  console.log(
    "Метод Рунге-Кутты\n",
    rungeKutta2Results[28].y,
    "\nШаг", step / 2
  );
  const rungeKutta4Results = solveRungeKutta({
    coefficients,
    init,
    step: step / 4,
    dot,
  });
  console.log(
    "Метод Рунге-Кутты\n",
    rungeKutta4Results[56].y,
    "\nШаг", step / 4
  );
  const rungeKutta6Results = solveRungeKutta({
    coefficients,
    init,
    step: step / 6,
    dot,
  });
  console.log(
    "Метод Рунге-Кутты\n",
    rungeKutta6Results[84].y,
    "\nШаг", step / 6
  );
  const rungeKutta8Results = solveRungeKutta({
    coefficients,
    init,
    step: step / 8,
    dot,
  });
  console.log(
    "Метод Рунге-Кутты\n",
    rungeKutta8Results[112].y,
    "\nШаг", step / 8
  );

  dependencyChart2(
    rungeKuttaInitResults,
    rungeKuttaCloseResults,
    rungeKutta2Results,
    rungeKutta4Results,
    rungeKutta6Results,
    rungeKutta8Results
  );
} catch (error) {
  console.error("Ошибка выполнения программы:", error);
}
