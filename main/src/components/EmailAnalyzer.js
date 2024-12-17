import React, { useState } from 'react';

const EmailAnalyzer = () => {
  const [emailContent, setEmailContent] = useState('');
  const [result, setResult] = useState(null);

  const analyzeEmail = () => {
    // Simulazione analisi semplice
    if (!emailContent.trim()) {
      setResult({ status: 'error', message: 'No content provided!' });
      return;
    }

    // Logica fittizia: controlla parole chiave sospette
    const suspiciousWords = ['urgent', 'password', 'click here', 'phishing'];
    const containsSuspicious = suspiciousWords.some((word) =>
      emailContent.toLowerCase().includes(word)
    );

    if (containsSuspicious) {
      setResult({ status: 'danger', message: '🚨 Suspicious content detected!' });
    } else {
      setResult({ status: 'safe', message: '✅ Email looks safe.' });
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
      >
        Analyze Email
      </button>

      {result && (
        <div
          className={`mt-4 p-3 rounded ${
            result.status === 'danger'
              ? 'bg-red-100 text-red-700'
              : 'bg-green-100 text-green-700'
          }`}
        >
          {result.message}
        </div>
      )}
    </div>
  );
};

export default EmailAnalyzer;
