import React, { useEffect, useState } from 'react';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Tooltip, Legend } from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, BarElement, Tooltip, Legend);

const BarChart = ({ commands, id }) => {
  const [chartData, setChartData] = useState({
    labels: ['Command'],
    datasets: [
      {
        label: 'Value',
        data: [0], // Initialize with a 0 value
        backgroundColor: 'rgba(0, 123, 255, 0.7)', // Set the bar color
      },
    ],
  });

  const options = {
    responsive: true,
    scales: {
      y: {
        min: -127,
        max: 127,
        ticks: {
          display: false, // Remove y-axis labels
        },
        grid: {
          display: false, // Remove y-axis grid lines
        },
      },
      x: {
        ticks: {
          display: false, // Remove x-axis labels
        },
        grid: {
          display: false, // Remove x-axis grid lines
        },
      },
    },
    plugins: {
      legend: { display: false }, // Remove the legend
      tooltip: { enabled: false }, // Disable tooltips
    },
    maintainAspectRatio: false,
    elements: {
      bar: {
        barThickness: 50, // Adjust the bar width as needed
      },
    },
  };

  useEffect(() => {
    if (commands.length > 0) {
      const newCommand = commands[0]; // Get the latest command
  
      // Extract the value (assuming the commands are formatted like 'A_128_128_...')
      const parsed = newCommand.split('_').slice(1);
      const parsedValue = parsed[id];
  
      // Map 0-127 to -128 to -1, and 128-255 to 0 to 127
      const mappedValue = parsedValue < 128 ? parsedValue - 128 : parsedValue - 128;
  
      // Update the chart data
      setChartData({
        labels: ['Command'],
        datasets: [
          {
            label: 'Value',
            data: [mappedValue],
            backgroundColor: mappedValue > 0 ? 'rgba(0, 255, 0, 1)' : (mappedValue < 0 ? 'rgba(255, 0, 0, 1)' : 'rgba(255, 255, 255, 1)')
          },
        ],
      });
    }
  }, [commands, id]);

  return (
    <div style={{color:'white', height: '23vw', width: '4vw', backgroundColor: 'black' }}>
      <Bar data={chartData} options={options} />
    </div>
  );
};

export default BarChart;