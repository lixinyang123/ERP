var currentIndex = 1;
var lastIndex = 0;

function addProduct() {
    let html = `
        <div>
            <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label">名称</label>
                <input id="product-name" type="text" class="form-control" placeholder="输入产品名称">
            </div>
            <div class="mb-3">
                <label for="exampleFormControlTextarea1" class="form-label">价格</label>
                <input id="product-price" type="number" class="form-control" placeholder="0">
            </div>
            <div class="mb-3">
                <label for="exampleFormControlTextarea1" class="form-label">初始库存数量</label>
                <input id="product-num" type="number" class="form-control" placeholder="0">
            </div>
            <div class="mb-3">
                <label for="exampleFormControlTextarea1" class="form-label">规格</label>
                <input id="product-specifications" type="text" class="form-control" placeholder="输入产品规格">
            </div>
            <div class="mb-3">
                <label for="exampleFormControlTextarea1" class="form-label">备注</label>
                <input id="product-notes" type="text" class="form-control" placeholder="输入产品备注信息">
            </div>
            
            <button class="btn btn-primary" onclick="submit()">提交</button>
        </div>
    `;

    document.querySelector(".offcanvas-body").innerHTML = html;
}

async function getData() {
    let results = await (await fetch(api + "/product/index?page=" + currentIndex)).json();
    lastIndex = results.lastIndex;
    
    showPagination();
    showData(results.products)
}

function showData(products) {

    document.querySelector("#products").innerHTML = null;

    products.forEach(product => {
        let html = `
            <div class="col-md-4 animate__animated animate__bounceIn">
                <div class="card">
                    <div class="card-header">
                        ID：${product.id}
                    </div>
                    <div class="card-body">
                        <h5 class="card-title">名称：${product.name}</h5>
                        <hr/>
                        <p class="card-text">库存：${product.num}</p>
                        <p class="card-text">价格：${product.price}</p>
                        <p class="card-text">规格：${product.specifications}</p>
                        <p class="card-text">备注：${product.notes}</p>
                        <button class="btn btn-warning" onclick="modifyProduct('${product.id}')" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight">编辑</button>
                        <button class="btn btn-danger" onclick="deleteProduct('${product.id}')">删除</button>
                    </div>
                </div>
            </div>
        `;

        document.querySelector("#products").innerHTML += html;
    });
}

async function deleteProduct(id) {
    let res = await fetch(api + "/product/delete?id=" + id);
    let result = await res.text();
    toast("删除成功", result);
    await getData();
}

function verify(product) {
    if(!product.name || product.price < 0 || product.num < 0 || !product.specifications || !product.notes)
        return false
    return true
}

async function submit(id) {

    let name = document.querySelector("#product-name").value;
    let price = document.querySelector("#product-price").value;
    let num = document.querySelector("#product-num").value;
    let specifications = document.querySelector("#product-specifications").value;
    let notes = document.querySelector("#product-notes").value;
    
    let product = new Product(name, price, num, specifications, notes);
    
    if(!verify(product)){
        toast("信息不完整", "请完善产品信息");
        return;
    }

    let url = "/product/add";
    if(id) {
        url = "/product/modify";
        product.id = id;
    }
    
    let res = await fetch(api + url, {
        method: "POST",
        body: JSON.stringify(product)
    });
    
    let result = await res.json();
    
    if(!result.successful) {
        toast("保存失败", JSON.stringify(result));
        return
    }
        
    toast("保存成功", JSON.stringify(result));
    getData();
}

async function modifyProduct(id) {

    let res = await fetch(api + "/product/find?id=" + id);
    let product = await res.json()

    let html = `
        <div>
            <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label">名称</label>
                <input id="product-name" type="text" class="form-control" placeholder="输入产品名称" value="${product.name}">
            </div>
            <div class="mb-3">
                <label for="exampleFormControlTextarea1" class="form-label">价格</label>
                <input id="product-price" type="number" class="form-control" placeholder="0" value="${product.price}">
            </div>
            <div class="mb-3">
                <label for="exampleFormControlTextarea1" class="form-label">当前库存数量</label>
                <input id="product-num" type="number" class="form-control" placeholder="0" value="${product.num}">
            </div>
            <div class="mb-3">
                <label for="exampleFormControlTextarea1" class="form-label">规格</label>
                <input id="product-specifications" type="text" class="form-control" placeholder="输入产品规格" value="${product.specifications}">
            </div>
            <div class="mb-3">
                <label for="exampleFormControlTextarea1" class="form-label">备注</label>
                <input id="product-notes" type="text" class="form-control" placeholder="输入产品备注信息" value="${product.notes}">
            </div>
            
            <button class="btn btn-primary" onclick="submit('${id}')">保存</button>
        </div>
    `;

    document.querySelector(".offcanvas-body").innerHTML = html;
}

getData();