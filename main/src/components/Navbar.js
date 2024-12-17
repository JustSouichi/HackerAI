import React from 'react';

const Navbar = () => {
  const closeApp = () => window.close();
  const minimizeApp = () => window.electron.send('minimize-window');

  return (
    <nav className="bg-gray-800 p-4 flex justify-between items-center">
      <h1 className="text-white text-2xl font-bold">HackerAI</h1>
      <div>
        <button
          onClick={minimizeApp}
          className="text-white px-4 py-1 hover:bg-gray-700 rounded"
        >
          Minimize
        </button>
        <button
          onClick={closeApp}
          className="text-white px-4 py-1 ml-2 hover:bg-red-700 rounded"
        >
          Close
        </button>
      </div>
    </nav>
  );
};

export default Navbar;
