import useDataLoader from "./useDataLoader";

const solveModEuler = () => {
  const { data } = useDataLoader("src/data.json");
  const { coefficients, init, step, dot } = data;
  const { a0, a1, a2, a3, a4 } = coefficients;
  const { x0, y0 } = init;

  let f = (x, y) => a0 + a1 * x + a2 * x ** 2 + a3 * y + a4 * x * y;
  console.log(f(x0, y0));

  const results = [];
  let x = x0;
  let y = y0;

  while (x <= dot) {
    results.push({ x, y });

    const k1 = (step / 2) * f(x, y);
    const k2 = step * f(x + step, y + k1);

    y += (1 / 2) * (k1 + k2);
    x += step;
  }
  return results;
};

export default solveModEuler;
