var currentIndex = 1;
var lastIndex = 0;

function addOrder() {
    let html = `
        <div class="modal-body">
            <div id="purchaseOperations" class="row"></div>
        </div>
        <div class="modal-footer">
            <button class="btn btn-success" onclick="addOperations()">新增产品</button>
            <button class="btn btn-primary" onclick="submit()">保存</button>
        </div>
    `;
    document.querySelector("#modal-body").innerHTML = html;
    addOperations();
}

async function getData() {
    let res = await fetch(api + "/purchase/index?page=" + currentIndex);
    let results = await res.json();

    lastIndex = results.lastIndex;
    showPagination();
    showData(results.purchases)
}

function showData(purchases) {

    document.querySelector("#purchases").innerHTML = null;

    purchases.forEach(purchase => {
        let price = 0
        let detail = ""
        purchase.purchaseOperations.forEach(ele => {
            detail += `<p class="card-text"><strong>${ele.product.name}</strong> * ${ele.num}</p>`;
            price += ele.product.price * ele.num;
        });

        let html = `
            <div class="col-md-4 animate__animated animate__bounceIn">
                <div class="card text-center">
                    <div class="card-header">
                        ID：${purchase.id}
                    </div>
                    <div class="card-body">
                        <h5 class="card-title">订单产品</h5>
                        ${detail}
                        <p class="card-text">总价：${price}</p>
                        <button class="btn btn-success">完成</button>
                        <button class="btn btn-warning" onclick="modifyOrder('${purchase.id}')" data-bs-toggle="modal" data-bs-target="#staticBackdrop">编辑</button>
                        <button class="btn btn-danger" onclick="deleteOrder('${purchase.id}')">删除</button>
                    </div>
                    <div class="card-footer text-muted">
                        ${purchase.time.substring(0,19)}
                    </div>
                </div>
            </div>
        `;

        document.querySelector("#purchases").innerHTML += html;
    });
}

async function deleteOrder(id) {
    let res = await fetch(api + "/purchase/delete?id=" + id);
    let result = await res.json();
    console.log(result);
    await getData();
}

async function addOperations() {

    let id = guid();

    let res = await fetch(api + "/product/index?page=1");
    let results = await res.json();

    let options = "";
    results.products.forEach(product => {
        options += `<option value="${product.id}">${product.name}</option>`;
    });

    let html = `
        <div id="${id}" class="col-md-4 purchaseOperation animate__animated animate__fadeIn">
            <div>
                <div class="mb-3">
                    <input id="purchase-id" type="hidden" value="" />
                    <label for="exampleFormControlInput1" class="form-label">产品</label>
                    <select id="purchase-product" class="form-select" aria-label="Default select example">
                        <option selected value="">选择产品</option>
                        ${options}
                    </select>
                </div>
                <div class="mb-3">
                    <label for="exampleFormControlTextarea1" class="form-label">数量</label>
                    <input id="purchase-num" type="number" class="form-control" placeholder="进货产品数量">
                </div>
                <div>
                    <button class="btn btn-danger" onclick="deleteOperation('${id}')">删除</button>
                </div>
            </div>
        </div>
    `;

    document.querySelector("#purchaseOperations").innerHTML += html
}

function verifyOperation(operation) {
    if(!operation.product || !operation.num)
        return false;
    return true;
}

function verifyOrder(order) {
    if(order.purchaseOperations.length > 0)
        return true;
    return false;
}

async function submit(id) {

    let operations = new Array();

    document.querySelectorAll(".purchaseOperation").forEach(element => {

        let productId = element.querySelector("#purchase-product").value;
        let num = element.querySelector("#purchase-num").value;

        let product = new Product("", 0, 0, "", "");
        product.id = productId;

        let operation = new PurchaseOperation(product, num);
        if(!verifyOperation(operation))
            return;
        
        if(id) 
            operation.id = element.querySelector("#purchase-id").value;

        operations.push(operation);
    });

    let order = new PurchaseOrder(operations);

    if(!verifyOrder(order)) {
        toast("信息不完整", "请完善订单信息");
        return;
    }

    let url = "/purchase/add";
    if(id) {
        url = "/purchase/modify";
        order.id = id;
    }

    console.warn(order);

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

async function modifyOrder(id) {

    let html = `
        <div class="modal-body">
            <div id="purchaseOperations" class="row"></div>
        </div>
        <div class="modal-footer">
            <button class="btn btn-success" onclick="addOperations()">新增产品</button>
            <button class="btn btn-primary" onclick="submit('${id}')">保存</button>
        </div>
    `;
    document.querySelector("#modal-body").innerHTML = html;

    document.querySelector("#purchaseOperations").innerHTML = null;
    let res = await fetch(api + "/purchase/find?id=" + id);
    let purchase = await res.json()

    purchase.purchaseOperations.forEach(async operation => {

        let id = guid();

        let res = await fetch(api + "/product/index?page=1");
        let results = await res.json();    

        let options = "";
        results.products.forEach(async product => {
            if(operation.product.id == product.id)
                options += `<option selected value="${product.id}">${product.name}</option>`;
            else
                options += `<option value="${product.id}">${product.name}</option>`;
        });

        let html = `
            <div id="${id}" class="col-md-4 purchaseOperation animate__animated animate__fadeIn">
                <div>
                    <div class="mb-3">
                        <input id="purchase-id" type="hidden" value="${operation.id}" />
                        <label for="exampleFormControlInput1" class="form-label">产品</label>
                        <select id="purchase-product" class="form-select" aria-label="Default select example">
                            <option value="">选择产品</option>
                            ${options}
                        </select>
                    </div>
                    <div class="mb-3">
                        <label for="exampleFormControlTextarea1" class="form-label">数量</label>
                        <input id="purchase-num" type="number" class="form-control" placeholder="进货产品数量" value="${operation.num}">
                    </div>
                    <div>
                        <button class="btn btn-danger" onclick="deleteOperation('${id}')">删除</button>
                    </div>
                </div>
            </div>
        `;
        document.querySelector("#purchaseOperations").innerHTML += html;
    });
}

function deleteOperation(id) {
    document.getElementById(id).remove();
}

getData();