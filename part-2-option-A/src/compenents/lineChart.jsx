// LineChart.js
import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Tooltip, Legend } from 'chart.js';
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Tooltip, Legend);

const LineChart = ({ commands, name, id }) => {
  const [chartData, setChartData] = useState({
    labels: [],
    datasets: [{
      label: 'Wheels Command Values',
      data: [],
      borderColor: 'rgba(255, 255, 255, 1)',
      backgroundColor: 'rgba(0, 0, 0, 1)',
      tension: 0,
      pointRadius: 0,
    }],
  });

  const options = {
    responsive: true,
    scales: {
        x: {
            ticks: { display: false }, // Hide x-axis labels
      },
      y: {
        min: 0,
        max: 255,
        display: true,
        grid: { display: true, color: 'gray' }, // Show grid and set it to gray
      },
    },
    plugins: {
      legend: { display: false },
      tooltip: { enabled: false },
    },
    elements: {
      line: { borderWidth: 2 },
    },
    maintainAspectRatio: false,
  };

  useEffect(() => {
    const interval = setInterval(() => {
      if (commands.length > 0 && commands[0]) { // Ensure commands[0] exists
        const newCommand = commands[0];

        const parsed = newCommand.split('_').slice(1);
        if (parsed[id] !== undefined) { // Ensure parsed[id] exists
          setChartData(prevData => {
            const updatedParsed = [...prevData.datasets[0].data, parsed[id]].slice(-3);
            const newLabels = Array.from({ length: updatedParsed.length }, (_, i) => `Point ${i + 1}`);

            // Determine line colors based on values
            const color = parsed[id] > 128 ? 'rgba(0, 255, 0, 1)' : (parsed[id] < 128 ? 'rgba(255, 0, 0, 1)' : 'rgba(255, 255, 255, 1)');

            return {
              labels: newLabels,
              datasets: [{
                ...prevData.datasets[0],
                data: updatedParsed.map(Number),
                borderColor: color,
              }],
            };
          });
        }
      }
    }, 40);

    return () => clearInterval(interval);
  }, [commands, id]);

  return <div className='line-graph-container' style={{backgroundColor: 'black', height: '13.5vw', width: '18vw' }}>
  <div className='line-graph-title'> ∗{name}</div>
  <div className='line-graph-body'>
    <div className='line-graph'><Line data={chartData} options={options} /></div>
    <div className='line-graph-value'>{chartData.datasets[0].data.slice(-1)[0] || 0}</div>
  </div>
</div>
};

export default LineChart;