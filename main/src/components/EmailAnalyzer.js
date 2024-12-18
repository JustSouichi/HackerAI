import React from 'react';

const EmailAnalyzer = () => {
  const launchScreenAnalyzer = async () => {
    console.log("Attempting to launch the Python script...");
    try {
      // Richiama il backend per lanciare il processo Python
      const response = await fetch('http://127.0.0.1:5000/launch-analyzer', { method: 'POST' });
      const data = await response.json();
      console.log("Response from server:", data);
      alert(data.message); // Mostra un alert di successo
    } catch (error) {
      console.error("Failed to launch the analyzer:", error);
      alert("Error: Failed to launch the analyzer.");
    }
  };

  return (
    <div className="p-6 bg-white shadow-md rounded-lg w-full max-w-3xl mx-auto mt-8">
      <h2 className="text-2xl font-bold mb-4 text-gray-700">Email Analyzer</h2>
      <button
        onClick={launchScreenAnalyzer}
        className="mt-4 bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition"
      >
        Click here to launch
      </button>
    </div>
  );
};

export default EmailAnalyzer;
