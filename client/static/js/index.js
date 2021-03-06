let api = "http://localhost:5000";

function logout() {
    localStorage.removeItem("remeberPwd");
    location.href='./login.html';
}

function guid() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g,function(c) {
        var r = Math.random()*16|0, v = c == 'x' ? r : (r&0x3|0x8);
        return v.toString(16);
    });
}

async function navigation(name,isBack = false){

    window.scrollTo(0,0);
    loadingState(true);
    document.querySelector("#main").innerHTML = "";
    let url = "./view/" + name.split("/")[0] + ".html";

    let response = await fetch(url);

    if(response.status == 200) {
        let data = await response.text()
        document.querySelector("#main").innerHTML = data;
        inject();
        url = "#" + name;
        if(!isBack)
            history.pushState({page: name}, name, url);
        loadingState(false);
        showNavState();
    }
    else{
        navigation("notfound");
        loadingState(false);
    }
}

function showNavState() {
    let themeColor = localStorage.getItem("themeColor");
    if(!themeColor)
        themeColor = "blue";
    setThemeColor(themeColor);
}

function loadingState(flag){
    let loadingPage = document.querySelector("#loading");
    if(flag){
        loadingPage.removeAttribute("hidden");
    }
    else{
        loadingPage.setAttribute("hidden","hidden");
    }
}

function inject(){
    document.querySelectorAll("#main > script").forEach(async(element) => {
        let src = element.getAttribute("src");

        let script = document.createElement("script");
        script.type = "text\/javascript";
        script.src = src;
        document.querySelector("#main").appendChild(script);

        element.remove();
    });
}

function toast(title, content) {

    let toastId = guid();
    
    let html = `
        <div id="${toastId}" class="toast show mb-2 animate__animated animate__fadeIn" role="alert" aria-live="assertive" aria-atomic="true">
            <div class="toast-header">
                <strong class="mr-auto">${title}</strong>
                <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close" onclick="closeToast('${toastId}')"></button>
            </div>
            <div class="toast-body">
                ${content}
            </div>
        </div>
    `;
    document.querySelector("#toastArea").innerHTML += html;

    setTimeout(closeToast, 5000, toastId);
}

function closeToast(toastId) {
    let toast = document.getElementById(toastId);
    if(toast)
        toast.remove();
}

function showPagination() {
    let list = document.querySelector(".pagination");

    let isFirst = "";
    if(currentIndex <= 1)
        isFirst = "disabled"
    
    list.innerHTML = `
        <li class="page-item ${isFirst}">
            <button class="page-link" onclick="previousPage()">?????????</button>
        </li>
    `;

    let startIndex = currentIndex - 2 <= 1 ? 1 : currentIndex - 2;
    let endIndex = startIndex + 5 < lastIndex ? startIndex + 5 : lastIndex;

    for(let i = startIndex; i <= endIndex; i++){

        let html = `
            <li class="page-item"><button class="page-link" onclick="jumpToIndex('${i}')">${i}</button></li>
        `;

        if(i == currentIndex){
            html = `
                <li class="page-item active" aria-current="page">
                    <button class="page-link disabled">${i}</button>
                </li>
            `;
        }

        list.innerHTML += html;
    }

    let isLast = "";
    if(currentIndex >= lastIndex)
        isLast = "disabled"

    list.innerHTML += `
        <li class="page-item ${isLast}">
            <button class="page-link" onclick="nextPage()">?????????</button>
        </li>
    `;
}

function nextPage() {
    currentIndex++;
    getData();
}

function previousPage() {
    currentIndex--;
    getData();
}

function jumpToIndex(index) {
    currentIndex = index;
    getData();
}

function init(){
    //???????????????
    window.onpopstate = (e)=>{
        navigation(e.state.page, true);
    }

    let href = window.location.href;
    //?????????????????????
    if(href.includes("#")){
        let page = href.substring(href.indexOf("#")+1);
        navigation(page);
    }
    else{
        navigation("home");
    }

    // ???????????????
    if(localStorage.getItem("isDark")) {
        DarkReader.setFetchMethod(window.fetch);
        DarkReader.enable();
    }
}

init();