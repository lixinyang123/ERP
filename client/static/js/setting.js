function setAdminPwd() {
    let password = document.querySelector("#password").value;
    let confirePwd = document.querySelector("#confirePwd").value;
    let question = document.querySelector("#question").value;

    if(!password || !confirePwd || !question) {
        toast("注意", "信息不完善");
        return;
    }

    if(escape(password).indexOf("%u") !=-1) {
        toast("注意", "密码不可以包含汉字");
        return;
    }

    if(password.length < 5 || password.length > 20) {
        toast("注意", "密码长度要在 5-20 之间");
        return;
    }
    
    if(password != confirePwd) {
        toast("注意", "两次输入密码不同");
        return;
    }

    localStorage.setItem("question", question);
    localStorage.setItem("password", CryptoJS.SHA256(password));
    toast("通知", "密码设置成功");
    getSettings();
}

function showReseter() {
    let html = `
        <div class="mb-3">
            <label for="exampleFormControlInput1" class="form-label">原密码</label>
            <input id="currentPwd" type="password" class="form-control" placeholder="输入原密码"/>
        </div>
        <div class="mb-3">
            <label for="exampleFormControlInput1" class="form-label">确认密码</label>
            <input id="confireCurrentPwd" type="password" class="form-control" placeholder="确认原密码"/>
        </div>
        <div class="mb-3 text-center">
            <button class="btn btn-danger" onclick="resetPwd()">重置密码</button>
        </div>
    `;
    document.querySelector(".offcanvas-body").innerHTML = html;
}

function resetPwd() {
    let currentPwd = document.querySelector("#currentPwd").value;
    let confireCurrentPwd = document.querySelector("#confireCurrentPwd").value;

    if(!currentPwd || !confireCurrentPwd) {
        toast("注意", "信息不完整");
        return;
    }

    if(currentPwd != confireCurrentPwd) {
        toast("注意", "两次输入密码不同");
        return;
    }

    if(CryptoJS.SHA256(currentPwd) != localStorage.getItem("password")) {
        toast("注意", "原密码错误");
        return;
    }

    localStorage.removeItem("question");
    localStorage.removeItem("password");
    toast("密码重置成功", "请访问设置重新设置密码");

    getSettings();
}

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
    if(localStorage.getItem("password"))
        document.querySelector("#pwdSetter").innerHTML = `
            <div class="mb-3 text-center">
                <button class="btn btn-danger" onclick="showReseter()" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight">重置密码</button>
            </div><hr/>
        `;
    else
        document.querySelector("#pwdSetter").innerHTML = `
            <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label">输入密码</label>
                <input id="password" type="password" class="form-control" placeholder="设置管理员密码"/>
            </div>
            <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label">确认密码</label>
                <input id="confirePwd" type="password" class="form-control" placeholder="确认管理员密码"/>
            </div>
            <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label">密保问题</label>
                <input id="question" type="text" class="form-control" placeholder="设置密保问题"/>
            </div>
            <div class="mb-3 text-center">
                <button class="btn btn-success" onclick="setAdminPwd()">设置密码</button>
            </div>
            <hr/>
        `;
    
    let productWarning = localStorage.getItem("productWarning");
    if(!productWarning) {
        productWarning = 10;
        localStorage.setItem("productWarning", productWarning);
    }
    document.querySelector("#productWarning").value = productWarning;
}