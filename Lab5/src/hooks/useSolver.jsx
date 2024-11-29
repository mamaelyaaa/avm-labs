import useDataLoader from './hooks/useDataLoader';

const useSolver = () => {
  const { data } = useDataLoader('src/assets/data.json');
  const { coefficients, init, step } = data;

  const { a0, a1, a2, a3, a4} = coefficients;
  const { x0, y0 } = init;

  const solveModEuler = () => {
    return
  } 
};

export default useSolver;
