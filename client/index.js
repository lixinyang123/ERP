const { app, BrowserWindow } = require('electron');
const child_process = require("child_process");
const fs = require("fs");

const server = child_process.execFile("./main", { 
    cwd: "./resources/server"
}, (err, stdout, stderr) => {
    if(err || stderr) {
        let log = `error: ${err} \n stdout: ${stdout} \n stderr: ${stderr}`;
        fs.writeFileSync("./error.log", log);
    }
});

function createWindow () {
    const mainWindow = new BrowserWindow({
        width: 1200,
        height: 800
    });

    mainWindow.loadFile('static/index.html');
}

app.whenReady().then(() => {
    createWindow();

    app.on('activate', function () {
        if (BrowserWindow.getAllWindows().length === 0) 
            createWindow();
    });
});

app.on('window-all-closed', () => {
    server.kill();
    if (process.platform !== 'darwin') 
        app.quit();
});