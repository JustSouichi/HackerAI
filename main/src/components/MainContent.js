import React from 'react';

const MainContent = () => {
  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-100">
      <h2 className="text-3xl font-bold text-gray-800 mb-4">Welcome to HackerAI</h2>
      <p className="text-gray-600 mb-8">
        Your AI-powered email phishing detection tool.
      </p>
      <button
        onClick={() => alert("Let's detect phishing emails!")}
        className="bg-blue-500 text-white px-6 py-2 rounded hover:bg-blue-700 transition"
      >
        Get Started
      </button>
    </div>
  );
};

export default MainContent;
