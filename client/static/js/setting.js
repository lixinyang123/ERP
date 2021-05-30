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

function changeColor(color) {
    localStorage.setItem("themeColor", color);
    setThemeColor(color);
    toast("保存成功", "主题色设置成功");
}

function setThemeColor(color) {
    document.querySelectorAll(".themeColor").forEach(ele => {
        ele.style.color = color;
    });

    let paras = location.href.substring(location.href.indexOf("#"), location.href.length).split("/");
    if(paras.length == 1) {
        document.querySelectorAll(`.nav li a`).forEach(ele => {        
            if(ele.classList.contains(`${paras[0].replace("#","")}`)) {
                ele.style.backgroundColor = color;
                ele.style.color = "white";
            }
            else {
                ele.style.backgroundColor = "";
            }
        });
    }
}

function getSettings() {
    let productWarning = localStorage.getItem("productWarning");
    if(!productWarning) {
        productWarning = 10;
        localStorage.setItem("productWarning", productWarning);
    }
    document.querySelector("#productWarning").value = productWarning;
}