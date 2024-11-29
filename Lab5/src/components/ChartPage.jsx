import useDataLoader from "../hooks/useDataLoader";

const ChartPage = () => {
  const { data } = useDataLoader("src/data.json");

  return (
    <div>
      <p>{JSON.stringify(data, null, 2)}</p>
    </div>
  );
};

export default ChartPage;
