import { solveRungeKutta } from "../methods/RungeKutt.js";

export function calculateErrorDependence({
  coefficients,
  init,
  dot,
  steps,
  referenceValue,
}) {  
  const intervalLength = Math.abs(init.x0 - dot); // Длина интервала интегрирования
  const errors = [];

  steps.forEach((step) => {
    const totalPoints = Math.ceil(intervalLength / step); // Количество точек
    const rungeKuttaResults = solveRungeKutta({
      coefficients,
      init,
      step,
      dot,
    });

    const valueAtDot = rungeKuttaResults.find(
      (point) => Math.abs(point.x - dot) < 1e-6
    ).y;

    const absoluteError = Math.abs(valueAtDot - referenceValue);

    errors.push({ totalPoints, absoluteError });
  });
  console.log(errors);
  return errors;
}
