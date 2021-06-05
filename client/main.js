const { app, BrowserWindow, Menu } = require('electron');
const child_process = require("child_process");
const fs = require("fs");

function getAppPath() {
    let path = app.getAppPath();

    if(path.endsWith(".asar"))
        return path.replace("app.asar", "") + "server";
    return path + "/resources/server";
}

const server = child_process.execFile("./main", {
    cwd: `${getAppPath()}`
}, (err, stdout, stderr) => {
    if(err || stderr) {
        let log = `error: ${err} \n stdout: ${stdout} \n stderr: ${stderr}`;
        fs.writeFileSync("./error.log", log);
    }
});

function createWindow () {
    const mainWindow = new BrowserWindow({
        width: 1300,
        height: 850
    });

    mainWindow.loadFile('static/login.html');
}

function initMenu(){
    const menu = Menu.buildFromTemplate([]);
    Menu.setApplicationMenu(menu);
}

function initApp() {

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

    initMenu();
}

initApp();