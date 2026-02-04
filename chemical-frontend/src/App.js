import React, { useState } from 'react';
import axios from 'axios';
import { Bar } from 'react-chartjs-2';
import { 
  Chart as ChartJS, 
  CategoryScale, 
  LinearScale, 
  BarElement, 
  Title, 
  Tooltip, 
  Legend 
} from 'chart.js';

// Register Chart.js components for React-Chartjs-2
ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

function App() {
  const [file, setFile] = useState(null);
  const [data, setData] = useState(null);
  const [summary, setSummary] = useState(null);
  const [distribution, setDistribution] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) return alert("Please select the sample CSV file first!");

    const formData = new FormData();
    formData.append('file', file);

    try {
      // API call to your Django backend
      const response = await axios.post('http://127.0.0.1:8000/api/upload/', formData);
      
      // Store API response data in state
      setData(response.data.data);
      setSummary(response.data.summary);
      setDistribution(response.data.distribution);
      alert("File Processed Successfully!");
    } catch (error) {
      console.error("Error uploading file:", error);
      alert("Upload failed. Make sure your Django server is running.");
    }
  };

  // Prepare chart data for Chart.js
  const chartData = distribution ? {
    labels: Object.keys(distribution),
    datasets: [{
      label: 'Equipment Count',
      data: Object.values(distribution),
      backgroundColor: 'rgba(54, 162, 235, 0.6)',
      borderColor: 'rgba(54, 162, 235, 1)',
      borderWidth: 1,
    }]
  } : null;

  return (
    <div style={{ padding: '30px', fontFamily: 'Segoe UI, Tahoma, Geneva, Verdana, sans-serif' }}>
      <h1 style={{ color: '#2c3e50' }}>Chemical Equipment Parameter Visualizer</h1>
      
      {/* 1. CSV Upload Section */}
      <div style={{ margin: '20px 0', padding: '20px', border: '1px solid #ddd', borderRadius: '8px' }}>
        <h3>Upload Equipment CSV</h3>
        <input type="file" accept=".csv" onChange={handleFileChange} />
        <button onClick={handleUpload} style={{ marginLeft: '10px', padding: '5px 15px', cursor: 'pointer' }}>
          Upload & Analyze
        </button>
      </div>

      {/* 2. Summary Statistics Section */}
      {summary && (
        <div style={{ display: 'flex', gap: '20px', marginBottom: '30px' }}>
          <div style={{ flex: 1, padding: '15px', background: '#f8f9fa', borderRadius: '8px' }}>
            <h3>Data Summary</h3>
            <p><strong>Total Equipment:</strong> {summary.total_rows}</p>
            <p><strong>Avg Flowrate:</strong> {summary.mean_flowrate.toFixed(2)}</p>
            <p><strong>Avg Pressure:</strong> {summary.mean_pressure.toFixed(2)}</p>
            <p><strong>Avg Temp:</strong> {summary.mean_temp.toFixed(2)}</p>
          </div>

          {/* 3. Visualization Section */}
          <div style={{ flex: 1, maxHeight: '300px' }}>
            <h3>Type Distribution</h3>
            {chartData && <Bar data={chartData} options={{ maintainAspectRatio: false }} />}
          </div>
        </div>
      )}

      {/* 4. Data Table Section */}
      {data && (
        <div style={{ marginTop: '20px' }}>
          <h3>Equipment Records</h3>
          <table border="1" cellPadding="10" style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
            <thead>
              <tr style={{ backgroundColor: '#34495e', color: 'white' }}>
                <th>Equipment Name</th>
                <th>Type</th>
                <th>Flowrate</th>
                <th>Pressure</th>
                <th>Temperature</th>
              </tr>
            </thead>
            <tbody>
              {data.map((item, index) => (
                <tr key={index}>
                  <td>{item['Equipment Name']}</td>
                  <td>{item.Type}</td>
                  <td>{item.Flowrate}</td>
                  <td>{item.Pressure}</td>
                  <td>{item.Temperature}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default App;