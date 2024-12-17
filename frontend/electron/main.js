const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow() {
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    title: "HackerAI",
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    },
  });

  // Carica l'app React su localhost:3000 (o la porta che stai usando)
  mainWindow.loadURL('http://localhost:3000'); // Cambia porta se necessario

  mainWindow.webContents.openDevTools(); // Per debug
}

app.whenReady().then(() => {
  createWindow();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});
