import useDataLoader from "../hooks/useDataLoader";

const Home = () => {
  const { data } = useDataLoader("src/assets/data.json");

  return (
    <div>
      <p>{JSON.stringify(data, null, 2)}</p>
    </div>
  );
};

export default Home;
