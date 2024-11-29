import solveModEuler from "./hooks/useSolveME";

const App = () => {
  const points = solveModEuler();
  console.log(points);

  // const { data } = useDataLoader("src/data.json");
  // console.log(data);

  // const { coefficients, init, step, dot } = data;

  // const { a0, a1, a2, a3, a4 } = coefficients;
  // const { x0, y0 } = init;
  // const { dx } = step;

  // const ME = solveModEuler(data);
  // const results = useSolver(data, 'ME');
  // console.log(results);

  // return (
  // <ChartComponent results={results}></ChartComponent>
  // )
};

export default App;
