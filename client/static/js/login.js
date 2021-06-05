function login() {
    let password = document.querySelector("#password").value;
    let remeberPwd = document.querySelector("#remeberPwd").checked;

    if(CryptoJS.SHA256(password) != localStorage.getItem("password")) {
        document.querySelector("#pwdError").innerText = "密码错误";
        setTimeout(() => {
            document.querySelector("#pwdError").innerText = "";
        }, 2000);
        return;
    }

    if(remeberPwd == true)
        localStorage.setItem("remeberPwd", true);
    else
        localStorage.removeItem("remeberPwd");
    
    location.href = "./index.html";
}

function showQuestion() {
    document.querySelector("#forget > i").innerText = "提示：" + localStorage.getItem("question");
    setTimeout(() => {
        document.querySelector("#forget > i").innerText = "";
    }, 2000);
}

function init() {
    // 初始化主题
    if(localStorage.getItem("isDark")) {
        DarkReader.setFetchMethod(window.fetch);
        DarkReader.enable();
    }

    if(!localStorage.getItem("password") || localStorage.getItem("remeberPwd"))
        location.href = "./index.html";
}

init();