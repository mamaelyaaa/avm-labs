import React, { useEffect, useRef } from 'react';
import { Chart } from 'chart.js';

const ChartComponent = ({ results }) => {
    const chartRef = useRef(null);

    useEffect(() => {
        if (!results || results.length === 0) return;

        const ctx = chartRef.current.getContext('2d');

        new Chart(ctx, {
            type: 'line',
            data: {
                labels: results.map((point) => point.x), // Время
                datasets: [
                    {
                        label: 'y(t)',
                        data: results.map((point) => point.y), // Значения функции
                        borderColor: 'rgb(75, 192, 192)',
                        tension: 0.1,
                    },
                ],
            },
        });
    }, [results]);

    return <canvas ref={chartRef} />;
};

export default ChartComponent;
