import useDataLoader from './hooks/useDataLoader';

const App = () => {
  const { data } = useDataLoader('src/assets/data.json');
  const { coefficients, init, step } = data;

  const { a0, a1, a2, a3, a4} = coefficients;
  const { x0, y0 } = init;

  
  return (
    <div>
      <p>{JSON.stringify(data, null, 2)}</p>
    </div>
  )
};

export default App;
