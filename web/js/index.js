let api = "http://localhost:5000";

class ProductModel {
    constructor(name, price, num, specifications, notes) {
        this.id = "",
        this.name = name,
        this.price = Number(price),
        this.num = Number(num),
        this.specifications = specifications,
        this.notes = notes;
    }
}

class UserModel {
    constructor(name, tel, address, notes) {
        this.id = "",
        this.name = name,
        this.tel = tel,
        this.address = address,
        this.notes = notes;
    }
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
    let url = "/view/" + name + ".html";

    let response = await fetch(url);

    if(response.status == 200) {
        let data = await response.text()
        document.querySelector("#main").innerHTML = data;
        inject();
        url = "#" + name;
        if(!isBack)
            history.pushState({page: name}, name, url);
        loadingState(false);
    }
    else{
        navigation("notfound");
        loadingState(false);
    }
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
        let resp = await fetch(src);
        eval(await resp.text());
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

function init(){

    //初始化导航
    window.onpopstate = (e)=>{
        navigation(e.state.page, true);
    }

    let href = window.location.href;

    //导航到指定页面
    if(href.includes("#")){
        let page = href.substring(href.indexOf("#")+1);
        navigation(page);
    }
    else{
        navigation("home");
    }
}

init();