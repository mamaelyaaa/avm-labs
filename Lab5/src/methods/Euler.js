export function solveEuler({ coefficients, init, step, dot }) {
  const { a0, a1, a2, a3, a4 } = coefficients;
  const { x0, y0 } = init;

  const f = (x, y) => a0 + a1 * x + a2 * x ** 2 + a3 * y + a4 * x * y;

  let results = [];
  let x = x0;
  let y = y0;

  while (x <= dot + 0.5) {
    results.push({ x, y });

    y += step * f(x, y);
    x += step;
  }

  return results;
}
