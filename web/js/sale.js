var currentIndex = 1;
var lastIndex = 0;

async function getData() {
    let res = await fetch(api + "/sale/index?page=" + currentIndex);
    let results = await res.json();

    lastIndex = results.lastIndex;
    showPagination();
    showData(results.sales)
}

function showData(sales) {

    document.querySelector("#sales").innerHTML = null;

    sales.forEach(sale => {

        // Get Price
        let price = 0
        let detail = ""
        sale.saleOperations.forEach(ele => {
            detail += `<p class="card-text"><strong>${ele.product.name}</strong> * ${ele.num}</p>`;
            price += ele.product.price * ele.num;
        });

        // Get State
        let isComplete = "alert alert-danger";
        let completeBtn = `
            <button class="btn btn-success" onclick="completeOrder('${sale.id}')">完成</button>
            <button class="btn btn-warning" onclick="modifyOrder('${sale.id}')" data-bs-toggle="modal" data-bs-target="#staticBackdrop">编辑</button>
        `;

        if(sale.state != 0){
            completeBtn = "";
            isComplete = "alert alert-success";
        }

        // Get Amount
        let amounted = 0
        sale.checkOuts.forEach(ele => {
            amounted += ele.amount;
        });

        let html = `
            <div class="col-md-4 animate__animated animate__bounceIn">
                <div class="card text-center">
                    <div class="card-header ${isComplete}">
                        ID：${sale.id}
                    </div>
                    <div class="card-body">
                        <h5 class="card-title">状态：${sale.state == 0 ? "未完成" : "已完成"}</h5>
                        ${detail}
                        <p class="card-text">已付：${amounted}</p>
                        <p class="card-text">总价：${price}</p>
                        ${completeBtn}
                        <button class="btn btn-danger" onclick="deleteOrder('${sale.id}')">删除</button>
                    </div>
                    <div class="card-footer text-muted">
                        ${sale.time.substring(0,19)}
                    </div>
                </div>
            </div>
        `;

        document.querySelector("#sales").innerHTML += html;
    });
}

async function addOrder() {

    let users = await (await fetch(api + "/user/index?page=1")).json();

    let userOptions = "";
    users.users.forEach(user => {
        userOptions += `<option value="${user.id}">${user.name}</option>`;
    });

    let html = `
        <div class="modal-body">
            <div id="saleOperations" class="row"></div>
        </div>
        <div class="modal-footer">
            <select id="user" class="form-select" aria-label="Default select example">
                <option selected value="">选择用户</option>
                ${userOptions}
            </select>
            <input id="selling" type="text" class="form-control" placeholder="售价">
            <input id="preAmount" type="text" class="form-control" placeholder="预付金额">
            <button class="btn btn-success" onclick="addOperations()">新增产品</button>
            <button class="btn btn-primary" onclick="submit()">保存</button>
        </div>
    `;
    document.querySelector("#modal-body").innerHTML = html;
    addOperations();
}

async function completeOrder(id) {
    let res = await fetch(api + "/sale/complete?id=" + id);
    let result = await res.text();
    toast("订单已完成", result);
    await getData();
}

async function deleteOrder(id) {
    let res = await fetch(api + "/sale/delete?id=" + id);
    let result = await res.text();
    toast("删除成功", result);
    await getData();
}

async function modifyOrder(id) {

    let users = await (await fetch(api + "/user/index?page=1")).json();
    let sale = await (await fetch(api + "/sale/find?id=" + id)).json();

    let userOptions = "";
    users.users.forEach(user => {
        console.log(sale.user.id + "===" + user.id);

        if(sale.user.id == user.id)
            userOptions += `<option selected value="${user.id}">${user.name}</option>`;
        else
            userOptions += `<option value="${user.id}">${user.name}</option>`;
    });

    let html = `
        <div class="modal-body">
            <div id="saleOperations" class="row"></div>
        </div>
        <div class="modal-footer">
            <select id="user" class="form-select" aria-label="Default select example">
                <option selected value="">选择用户</option>
                ${userOptions}
            </select>
            <input id="selling" type="text" class="form-control" placeholder="售价">
            <input id="preAmount" type="text" class="form-control" placeholder="已付金额">
            <button class="btn btn-success" onclick="addOperations()">新增产品</button>
            <button class="btn btn-primary" onclick="submit('${id}')">保存</button>
        </div>
    `;
    document.querySelector("#modal-body").innerHTML = html;

    document.querySelector("#selling").value = sale.selling;

    let amounted = 0
    sale.checkOuts.forEach(ele => {
        amounted += ele.amount;
    });
    document.querySelector("#preAmount").value = amounted;

    document.querySelector("#saleOperations").innerHTML = null;

    sale.saleOperations.forEach(async operation => {

        let id = guid();

        let results = await (await fetch(api + "/product/index?page=1")).json();

        let options = "";
        results.products.forEach(async product => {
            if(operation.product.id == product.id)
                options += `<option selected value="${product.id}">${product.name}</option>`;
            else
                options += `<option value="${product.id}">${product.name}</option>`;
        });

        let html = `
            <div id="${id}" class="saleOperation col-md-4 animate__animated animate__fadeIn">
                <div>
                    <div class="mb-3">
                        <label for="exampleFormControlInput1" class="form-label">产品</label>
                        <select class="form-select" aria-label="Default select example">
                            <option value="">选择产品</option>
                            ${options}
                        </select>
                    </div>
                    <div class="mb-3">
                        <label for="exampleFormControlTextarea1" class="form-label">数量</label>
                        <input type="number" class="form-control" placeholder="进货产品数量" value="${operation.num}">
                    </div>
                    <div>
                        <button class="btn btn-danger" onclick="deleteOperation('${id}')">删除</button>
                    </div>
                </div>
            </div>
        `;
        document.querySelector("#saleOperations").innerHTML += html;
    });
}

async function addOperations() {

    let id = guid();

    let products = await (await fetch(api + "/product/index?page=1")).json()

    let productOptions = "";
    products.products.forEach(product => {
        productOptions += `<option value="${product.id}" price="${product.price}">${product.name}</option>`;
    });

    let html = `
        <div id="${id}" class="saleOperation col-md-4 animate__animated animate__fadeIn">
            <div>
                <div class="mb-3">
                    <label for="exampleFormControlInput1" class="form-label">产品</label>
                    <select onchange="countSelling()" class="form-select" aria-label="Default select example">
                        <option selected value="">选择产品</option>
                        ${productOptions}
                    </select>
                </div>
                <div class="mb-3">
                    <label for="exampleFormControlTextarea1" class="form-label">数量</label>
                    <input onchange="countSelling()" type="number" class="form-control" placeholder="进货产品数量">
                </div>
                <div>
                    <button class="btn btn-danger" onclick="deleteOperation('${id}')">删除</button>
                </div>
            </div>
        </div>
    `;

    document.querySelector("#saleOperations").innerHTML += html
}

function deleteOperation(id) {
    document.getElementById(id).remove();
}

function verifyOperation(operation) {
    if(!operation.product || !operation.num)
        return false;
    return true;
}

function verifyOrder(order) {
    if(order.saleOperations.length > 0 && order.checkOuts.length > 0 && order.selling && order.user)
        return true;
    return false;
}

async function submit(id) {

    // Get User
    let user = new User("", 0, "", "");
    user.id = document.querySelector("#user").value;

    // Get Operation
    let operations = new Array();

    document.querySelectorAll(".saleOperation").forEach(element => {

        let productId = element.querySelector("select").value;
        let num = element.querySelector("input").value;

        let product = new Product("", 0, 0, "", "");
        product.id = productId;

        let operation = new ProductOperation(product, num);
        if(!verifyOperation(operation))
            return;

        operations.push(operation);
    });

    // Get Selling
    let selling = document.querySelector("#selling").value

    // Get Checkout
    let checkOuts = new Array();
    let preAmount = document.querySelector("#preAmount").value;
    if(preAmount)
        checkOuts.push(new CheckOut(preAmount));

    let order = new SaleOrder(user, selling, operations, checkOuts);

    if(!verifyOrder(order)) {
        toast("信息不完整", "请完善订单信息");
        return;
    }

    let url = "/sale/add";
    if(id) {
        url = "/sale/modify";
        order.id = id;
    }

    let res = await fetch(api + url, {
        method: "POST",
        body: JSON.stringify(order)
    });
    
    let result = await res.json();
    
    if(!result.successful) {
        toast("保存失败", JSON.stringify(result));
        return
    }
        
    toast("保存成功", JSON.stringify(result));

    // 关闭模态框
    document.querySelector(".modal-header button").click();
    getData();
}

function countSelling() {

    let selling = 0;

    document.querySelectorAll(".saleOperation").forEach(ele => {

        let productId = ele.querySelector("select").value;
        let num = ele.querySelector("input").value;

        ele.querySelectorAll("option").forEach(option => {
            if(productId == option.value)
                selling += Number(option.getAttribute("price")) * num;
        });
    });

    document.querySelector("#selling").value = selling;
}

getData();