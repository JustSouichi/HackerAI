import React from 'react';
import Navbar from './components/Navbar';
import EmailAnalyzer from './components/EmailAnalyzer';

function App() {
  return (
    <div className="h-screen bg-gray-100">
      <Navbar />
      <EmailAnalyzer />
    </div>
  );
}

export default App;
