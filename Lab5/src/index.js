import { parseJSON } from "./jsonParser.js";
import sampleData from './data.json' with { type: "json" };;
import { solveModEuler } from "./methods/ME.js";
import { solveRungeKutta } from "./methods/RK.js";
import { dependencyChart } from "./charts/depChart.js";

try {
    const data = parseJSON(JSON.stringify(sampleData));
    console.log(data);
    
    const eulerResults = solveModEuler(data);
    const rungeKuttaResults = solveRungeKutta(data);
  
    dependencyChart(eulerResults, rungeKuttaResults);
  } catch (error) {
    console.error("Ошибка выполнения программы:", error);
}