import useDataLoader from "./useDataLoader";

const useSolver = (method) => {
  const { data } = useDataLoader("src/assets/data.json");
  const { coefficients, init, step, dot } = data;

  const { a0, a1, a2, a3, a4 } = coefficients;
  const { x0, y0 } = init;
  const { dx } = step;

  let f = (x, y) => {
    return a0 + a1 * x + a2 * x ** 2 + a3 * y + a4 * x * y;
  };

  const solveModEuler = () => {
    const result = [];
    let x = x0;
    let y = y0;

    while (x <= dot) {
      result.push({ x, y });

      const k1 = (dx / 2) * f(x, y);
      const k2 = dx * f(x + dx, y + k1);

      y += (1 / 2) * (k1 + k2);
      x += dx;
    }

    return result;
  };

  const solveRungeKutt = () => {
    const result = [];
    let x = x0;
    let y = y0;

    while (x <= dot) {
      result.push({ x, y });

      const k1 = dx * f(x, y);
      const k2 = dx * f(x + dx / 2, y + k1 / 2);
      const k3 = dx * f(x + dx / 2, y + k2 / 2);
      const k4 = dx * f(x + dx, y + k3);

      y += (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4);
      x += dx;
    }

    return result;
  };

  if (method === 'ME') {
    return solveModEuler()
  } else if (method === 'RK') {
    return solveRungeKutt()
  } 
};

export default useSolver;
