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

        // Get Amount
        let amounted = 0
        sale.checkOuts.forEach(ele => {
            amounted += ele.amount;
        });

        let payOrComplete = "";
        if(price > amounted)
            payOrComplete = `<button class="btn btn-info" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" 
                aria-controls="offcanvasRight" onclick="payment('${sale.id}', '${sale.user.name}')">支付</button>`;
        else
            payOrComplete = `<button class="btn btn-success" onclick="completeOrder('${sale.id}')">完成</button>`;

        // Get State
        let isComplete = "alert alert-danger";
        let completeBtn = `
            ${payOrComplete}
            <button class="btn btn-warning" onclick="modifyOrder('${sale.id}')" data-bs-toggle="modal" data-bs-target="#staticBackdrop">编辑</button>
        `;

        if(sale.state != 0){
            completeBtn = "";
            isComplete = "alert alert-success";
        }

        let html = `
            <div class="col-md-4 animate__animated animate__bounceIn">
                <div class="card text-center">
                    <div class="card-header ${isComplete}">
                        ID：${sale.id}
                    </div>
                    <div class="card-body">
                        <h5 class="card-title">状态：${sale.state == 0 ? "未完成" : "已完成"}</h5>
                        ${detail}
                        <p class="card-text">用户：${sale.user.name}</p>
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
    let html = `
        <div class="modal-body">
            <div id="saleOperations" class="row"></div>
        </div>
        <div class="modal-footer">
            <button id="userInfo" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#productSelector" 
                onclick="showUsers()" >选择用户</button>
            <input id="userId" type="hidden" />
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

async function addOperations() {

    let id = guid();

    let html = `
        <div id="${id}" class="saleOperation col-md-4 animate__animated animate__fadeIn">
            <div>
                <div class="mb-3">
                    <label for="exampleFormControlInput1" class="form-label">产品</label>
                    <div class="product" class="row">
                        <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#productSelector" 
                            onclick="showProducts('${id}')" >选择产品</button>
                        <input type="hidden" />
                    </div>
                </div>
                <div class="mb-3">
                    <label for="exampleFormControlTextarea1" class="form-label">数量<span></span></label>
                    <input class="productNum form-control" onchange="countSelling()" type="number" placeholder="进货产品数量" />
                </div>
                <div>
                    <button class="btn btn-danger" onclick="deleteOperation('${id}')">删除</button>
                </div>
            </div>
        </div>
    `;

    document.querySelector("#saleOperations").innerHTML += html;
    countSelling();
}

function selectUser(id, name, notes) {
    document.querySelector("#userId").value = id;
    document.querySelector("#userInfo").innerText = `${name}（${notes}）`;
}

function selectProduct(id, productId, name, num, price, notes) {
    let operation = document.getElementById(id);
    operation.querySelector(".product > input").value = productId;
    operation.querySelector(".product > input").setAttribute("price", price)
    operation.querySelector(".product > button").innerText = `${name}/${notes}（剩余库存：${num}）`;
}

async function modifyOrder(id) {

    let sale = await (await fetch(api + "/sale/find?id=" + id)).json();
    let user = sale.user;

    let html = `
        <div class="modal-body">
            <div id="saleOperations" class="row"></div>
        </div>
        <div class="modal-footer">
            <button id="userInfo" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#productSelector" 
                onclick="showUsers()" disabled >${user.name}（${user.notes}）</button>
            <input id="userId" type="hidden" value="${user.id}"/>
            <input id="selling" type="text" class="form-control" placeholder="售价" disabled>
            <button class="btn btn-success" onclick="addOperations()">新增产品</button>
            <button class="btn btn-primary" onclick="submit('${id}')">保存</button>
        </div>
    `;
    document.querySelector("#modal-body").innerHTML = html;
    document.querySelector("#selling").value = sale.selling;

    document.querySelector("#saleOperations").innerHTML = null;
    sale.saleOperations.forEach(async operation => {

        let id = guid();
        let product = operation.product;

        let html = `
            <div id="${id}" class="saleOperation col-md-4 animate__animated animate__fadeIn">
                <div>
                    <div class="mb-3">
                        <label for="exampleFormControlInput1" class="form-label">产品</label>
                        <div class="product" class="row">
                            <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#productSelector" 
                                onclick="showProducts('${id}')" >${product.name}/${product.notes}（剩余库存：${product.num}）</button>
                            <input type="hidden" value="${product.id}" price="${product.price}" />
                        </div>
                    </div>
                    <div class="mb-3">
                        <label for="exampleFormControlTextarea1" class="form-label">数量<span>（剩余库存：${operation.product.num}）</span></label>
                        <input class="productNum form-control" onchange="countSelling()" type="number" placeholder="进货产品数量" value="${operation.num}" />
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

function deleteOperation(id) {
    document.getElementById(id).remove();
    countSelling();
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

async function payment(id, name) {

    let sale = await (await fetch(api + "/sale/find?id=" + id)).json();

    let amounted = 0
    sale.checkOuts.forEach(ele => {
        amounted += ele.amount;
    });

    let paymentInfo = "";
    if(sale.selling - amounted > 0) {
        paymentInfo = `
            <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label">待付金额</label>
                <input type="text" class="form-control" value="${sale.selling - amounted}" disabled />
            </div>
        `;
    }

    let html = `
        <div class="mb-3">
            <label for="exampleFormControlInput1" class="form-label">支付订单</label>
            <input id="paymentOrderId" type="text" class="form-control" value="${id}" disabled />
        </div>
        <div class="mb-3">
            <label for="exampleFormControlInput1" class="form-label">付款用户</label>
            <input type="text" class="form-control" value="${name}" disabled />
        </div>
        ${paymentInfo}
        <div class="mb-3">
            <label for="exampleFormControlTextarea1" class="form-label">支付金额</label>
            <input id="payment" type="number" class="form-control" placeholder="0" />
        </div>

        <button class="btn btn-primary" onclick="pay('${id}')">提交支付</button>
    `;
    document.querySelector(".offcanvas-body").innerHTML = html;
}

async function pay(id) {
    let amount = document.querySelector("#payment").value;
    if(amount < 0) {
        toast("注意", "支付金额不能为零");
        return;
    } 

    let result = await (await fetch(`${api}/sale/pay?id=${id}&amount=${amount}`)).text();
    toast("发起支付", result);
    await getData();
}

async function submit(id) {

    // Get User
    let user = new User("", 0, "", "");
    user.id = document.querySelector("#userId").value;

    // Get Operation
    let operations = new Array();

    document.querySelectorAll(".saleOperation").forEach(element => {

        let productId = element.querySelector(".product > input").value;
        let num = element.querySelector(".productNum").value;

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

    if(!id) {
        let preAmount = document.querySelector("#preAmount").value;
        if(preAmount)
            checkOuts.push(new CheckOut(preAmount));
    }
    else{
        checkOuts.push(new CheckOut(new CheckOut(0)));
    }

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
        let price = ele.querySelector(".product > input").getAttribute("price");
        let num = ele.querySelector(".productNum").value;
        selling += Number(price) * Number(num);
    });
    document.querySelector("#selling").value = selling;
}

getData();