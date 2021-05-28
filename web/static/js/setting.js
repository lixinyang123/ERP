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
    toast("保存成功", "主题保存成功");
}

function setProductWarning() {
    let warningNum = document.querySelector("#productWarning").value;

    if(!warningNum || isNaN(warningNum)) {
        toast("保存失败", "库存警告不合法");
        return;
    }

    localStorage.setItem("productWarning", warningNum);
    toast("保存成功", "库存警告保存成功");
}

function getSettings() {
    let productWarning = localStorage.getItem("productWarning");
    if(!productWarning) {
        productWarning = 10;
        localStorage.setItem("productWarning", productWarning);
    }
    document.querySelector("#productWarning").value = productWarning;
}