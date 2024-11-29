import { useEffect } from "react";

const useSolver = (data, method) => {
  const [result, setResult] = useState([]);

  useEffect(() => {
    const { coefficients, init, step, dot } = data;
    const { a0, a1, a2, a3, a4 } = coefficients;
    const { x0, y0 } = init;
    const { dx } = step;

    const f = (x, y) => a0 + a1 * x + a2 * x ** 2 + a3 * y + a4 * x * y;

    const solveModEuler = () => {
      const results = [];
      let x = x0;
      let y = y0;

      while (x <= dot) {
        results.push({ x, y });

        const k1 = (dx / 2) * f(x, y);
        const k2 = dx * f(x + dx, y + k1);

        y += (1 / 2) * (k1 + k2);
        x += dx;
      }

      return results;
    };

    const solveRungeKutt = () => {
      const results = [];
      let x = x0;
      let y = y0;

      while (x <= dot) {
        results.push({ x, y });

        const k1 = dx * f(x, y);
        const k2 = dx * f(x + dx / 2, y + k1 / 2);
        const k3 = dx * f(x + dx / 2, y + k2 / 2);
        const k4 = dx * f(x + dx, y + k3);

        y += (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4);
        x += dx;
      }

      return results;
    };
    if (method === "ME") {
      setResult(solveModEuler());
    } else if (method === "RK") {
      setResult(solveRungeKutt());
    }
  }, [data, method]);
  return { result }
};

export default useSolver;
