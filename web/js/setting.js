function switchTheme() {
    let isDark = localStorage.getItem("isDark");
    if(!isDark) {
        DarkReader.setFetchMethod(window.fetch);
        DarkReader.enable();
        localStorage.setItem("isDark", "true");
    }
    else{
        DarkReader.disable();
        localStorage.removeItem("isDark");
    }
}

function initSettings() {
    if(localStorage.getItem("isDark")) {
        DarkReader.setFetchMethod(window.fetch);
        DarkReader.enable();
    }
}

initSettings();