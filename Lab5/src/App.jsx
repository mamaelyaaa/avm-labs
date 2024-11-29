import { BrowserRouter, Routes, Route } from 'react-router-dom';
import HomePage from './components/Home';
import ChartPage from './components/ChartPage';

const App = () => {
  // const results = useSolver('ME');
  
  // return (
    // <ChartComponent results={results}></ChartComponent>
  // )

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/charts" element={<ChartPage />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;
