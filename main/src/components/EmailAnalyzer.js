import React, { useState } from 'react';
import axios from 'axios';

const EmailAnalyzer = () => {
  const [emailContent, setEmailContent] = useState('');
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const analyzeEmail = async () => {
    if (!emailContent.trim()) {
      setError('❌ Please enter email content.');
      return;
    }

    setLoading(true);
    setError('');
    setResult('');

    console.log("Sending request with content:", emailContent);

    try {
      console.log("Sending request to Flask API...");
      const response = await axios.post('http://127.0.0.1:5000/analyze', {
        content: emailContent,
      });
      console.log("Response received:", response.data);
    
      const aiResult = response.data.result[0];
      setResult({
        label: aiResult.label,
        score: aiResult.score,
      });
    } catch (err) {
      console.error("Error during API request:", err);
      setError('❌ Error analyzing email. Please try again.');
    }
    
  };

  return (
    <div className="p-6 bg-white shadow-md rounded-lg w-full max-w-3xl mx-auto mt-8">
      <h2 className="text-2xl font-bold mb-4 text-gray-700">Email Analyzer</h2>
      <textarea
        className="w-full p-3 border rounded focus:outline-none focus:ring focus:ring-blue-300"
        rows="6"
        placeholder="Paste the email content here..."
        value={emailContent}
        onChange={(e) => setEmailContent(e.target.value)}
      />
      <button
        className="mt-4 bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition"
        onClick={analyzeEmail}
        disabled={loading}
      >
        {loading ? 'Analyzing...' : 'Analyze Email'}
      </button>

      {error && (
        <div className="mt-4 p-3 rounded bg-red-100 text-red-700">
          {error}
        </div>
      )}

      {result && (
        <div
          className={`mt-4 p-3 rounded ${
            result.label === 'Suspicious'
              ? 'bg-red-100 text-red-700'
              : 'bg-green-100 text-green-700'
          }`}
        >
          <strong>Result:</strong> {result.label} <br />
          <strong>Confidence:</strong> {(result.score * 100).toFixed(2)}%
        </div>
      )}
    </div>
  );
};

export default EmailAnalyzer;
