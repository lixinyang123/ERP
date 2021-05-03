
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