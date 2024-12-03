export function solveRungeKutta({ coefficients, init, step, dot }) {
  const { a0, a1, a2, a3, a4 } = coefficients;
  const { x0, y0 } = init;

  const f = (x, y) => a0 + a1 * x + a2 * x ** 2 + a3 * y + a4 * x * y;


  let results = [];
  let x = x0;
  let y = y0;

  while (x <= dot) {
    results.push({ x, y });

    const k1 = step * f(x, y);
    const k2 = step * f(x + step / 2, y + k1 / 2);
    const k3 = step * f(x + step / 2, y + k2 / 2);
    const k4 = step * f(x + step, y + k3);

    y += (k1 + 2 * k2 + 2 * k3 + k4) / 6;
    x += step;
  }

  return results;
}
