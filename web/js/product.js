var currentIndex = 1;
var lastIndex = 0;

async function getData() {
    let res = await fetch(api + "/product/index?page=" + currentIndex);
    let results = await res.json();

    lastIndex = results.lastIndex;
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
                        <button class="btn btn-warning">编辑</button>
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
    let result = await res.json();
    console.log(result);
    await getData();
}

function showPagination(lastIndex) {

}

function verify(product) {
    if(!product.name || !product.price || !product.num || !product.specifications || !product.notes)
        return false
    return true
}

async function submit() {

    let name = document.querySelector("#product-name").value;
    let price = document.querySelector("#product-price").value;
    let num = document.querySelector("#product-num").value;
    let specifications = document.querySelector("#product-specifications").value;
    let notes = document.querySelector("#product-notes").value;
    
    let product = new ProductModel(name, price, num, specifications, notes);
    
    if(!verify(product)){
        toast("信息不完整", "请完善产品信息");
        return;
    }
    
    let res = await fetch(api + "/product/add", {
        method: "POST",
        body: JSON.stringify(product)
    });
    
    let result = await res.json();
    
    if(!result.successful) {
        toast("提交失败", JSON.stringify(result));
        return
    }
        
    toast("提交成功", JSON.stringify(result));
    getData();
}

function temp() {
    console.log(123);
}

getData();
console.log(123);