var currentIndex = 1;
var lastIndex = 0;

function addUser() {
    let html = `
        <div>
            <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label">姓名</label>
                <input id="user-name" type="text" class="form-control" placeholder="输入用户姓名">
            </div>
            <div class="mb-3">
                <label for="exampleFormControlTextarea1" class="form-label">电话</label>
                <input id="user-tel" type="tel" class="form-control" placeholder="用户电话号码">
            </div>
            <div class="mb-3">
                <label for="exampleFormControlTextarea1" class="form-label">地址</label>
                <input id="user-address" type="text" class="form-control" placeholder="输入用户地址信息">
            </div>
            <div class="mb-3">
                <label for="exampleFormControlTextarea1" class="form-label">备注</label>
                <input id="user-notes" type="text" class="form-control" placeholder="输入用户备注信息">
            </div>
            
            <button class="btn btn-primary" onclick="submit()">保存</button>
        </div>
    `;

    document.querySelector(".offcanvas-body").innerHTML = html;
}

async function getData() {
    let results = await (await fetch(api + "/user/index?page=" + currentIndex)).json();
    lastIndex = results.lastIndex;

    showPagination();
    await showData(results.users)
}

function showData(users) {

    document.querySelector("#users").innerHTML = null;

    users.forEach(async user => {

        let sales = await (await fetch(api + "/sale/findByUserWithState?id=" + user.id)).json();
        
        let price = 0, amounted = 0

        sales.forEach(sale => {
            price += sale.selling;

            // Get Amount
            sale.checkOuts.forEach(ele => {
                amounted += ele.amount;
            });
        });

        let html = `
            <div class="col-md-12 animate__animated animate__bounceIn">
                <div class="card">
                    <div class="card-body">
                        <div class="row">
                            <div class="col-md-2"><p>姓名：${user.name}</p></div>
                            <div class="col-md-2"><p>电话：${user.tel}</p></div>
                            <div class="col-md-2"><p>地址：${user.address}</p></div>
                            <div class="col-md-1"><p>备注：${user.notes}</p></div>
                            <div class="col-md-3"><p>未完成订单：${sales.length}（待付：${price - amounted}）</p></div>
                            <div class="col-md-2">
                                <button class="btn btn-danger" onclick="deleteUser('${user.id}')">删除</button>
                                <button class="btn btn-warning" onclick="modifyUser('${user.id}')" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight">编辑</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;

        document.querySelector("#users").innerHTML += html;
    });
}

async function deleteUser(id) {
    let res = await fetch(api + "/user/delete?id=" + id);
    let result = await res.text();
    toast("删除成功", result);
    await getData();
}

function verify(user) {
    if(!user.name || !user.tel || !user.address || !user.notes)
        return false
    return true
}

async function submit(id) {
    
    let name = document.querySelector("#user-name").value;
    let tel = document.querySelector("#user-tel").value;
    let address = document.querySelector("#user-address").value;
    let notes = document.querySelector("#user-notes").value;

    let user = new User(name, tel, address, notes);
        
    if(!verify(user)){
        toast("信息不完整", "请完善用户信息");
        return;
    }

    let url = "/user/add";
    if(id) {
        url = "/user/modify";
        user.id = id;
    }

    let res = await fetch(api + url, {
        method: "POST",
        body: JSON.stringify(user)
    });
    
    let result = await res.json();
    
    if(!result.successful) {
        toast("保存失败", JSON.stringify(result));
        return
    }
        
    toast("保存成功", JSON.stringify(result));
    getData();
}

async function modifyUser(id) {

    let res = await fetch(api + "/user/find?id=" + id);
    let user = await res.json()

    let html = `
        <div>
            <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label">姓名</label>
                <input id="user-name" type="text" class="form-control" placeholder="输入用户姓名" value="${user.name}">
            </div>
            <div class="mb-3">
                <label for="exampleFormControlTextarea1" class="form-label">电话</label>
                <input id="user-tel" type="tel" class="form-control" placeholder="用户电话号码" value="${user.tel}">
            </div>
            <div class="mb-3">
                <label for="exampleFormControlTextarea1" class="form-label">地址</label>
                <input id="user-address" type="text" class="form-control" placeholder="输入用户地址信息" value="${user.address}">
            </div>
            <div class="mb-3">
                <label for="exampleFormControlTextarea1" class="form-label">备注</label>
                <input id="user-notes" type="text" class="form-control" placeholder="输入用户备注信息" value="${user.notes}">
            </div>
            
            <button class="btn btn-primary" onclick="submit('${user.id}')">保存</button>
        </div>
    `;

    document.querySelector(".offcanvas-body").innerHTML = html;
}

getData();