var currentIndex = 1;
var lastIndex = 0;

async function getData() {
    let res = await fetch(api + "/sale/index?page=" + currentIndex);
    let results = await res.json();

    lastIndex = results.lastIndex;
    showPagination();
    //showData(results.purchases)
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
            <select class="form-select" aria-label="Default select example">
                <option selected value="">选择用户</option>
                ${userOptions}
            </select>
            <input id="selling" type="text" class="form-control" placeholder="售价">
            <button class="btn btn-success" onclick="addOperations()">新增产品</button>
            <button class="btn btn-primary" onclick="submit()">保存</button>
        </div>
    `;
    document.querySelector("#modal-body").innerHTML = html;
    addOperations();
}

async function addOperations() {

    let id = guid();

    let products = await (await fetch(api + "/product/index?page=1")).json()

    let productOptions = "";
    products.products.forEach(product => {
        productOptions += `<option value="${product.id}" price="${product.price}">${product.name}</option>`;
    });

    let html = `
        <div id="${id}" class="operation col-md-4 saleOperation animate__animated animate__fadeIn">
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

function countSelling() {

    let selling = 0;

    document.querySelectorAll(".operation").forEach(ele => {

        let productId = ele.querySelector("select").value;
        let num = ele.querySelector("input").value;

        ele.querySelectorAll("option").forEach(option => {
            if(productId == option.value)
                selling += Number(option.getAttribute("price")) * num;
        });
    });

    document.querySelector("#selling").value = selling;
}