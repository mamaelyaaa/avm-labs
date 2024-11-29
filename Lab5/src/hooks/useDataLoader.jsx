import { useState, useEffect } from 'react';

const useDataLoader = (filePath) => {
    const [data, setData] = useState(null);

    useEffect(() => {
        fetch(filePath)
            .then(response => response.json())
            .then(jsonData => setData(jsonData));
    }, [filePath]);

    return { data };
};

export default useDataLoader;
