var selectorIndex = 1;
var selectorLastIndex = 1;
var selectorNext, selectorPrevious;

async function showProducts(id) {

    let results = await (await fetch(api + "/product/index?page=" + selectorIndex)).json();
    selectorLastIndex = results.lastIndex;

    selectorNext = () => {
        selectorIndex++;
        if(selectorIndex > selectorLastIndex)
            selectorIndex = selectorLastIndex;
        showProducts(id);
    };

    selectorPrevious = () => {
        selectorIndex--;
        if(selectorIndex < 1)
            selectorIndex = 1;
        showProducts(id);
    }

    document.querySelector("#selector-list").innerHTML = null;

    results.products.forEach(product => {
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
                        <button class="btn btn-success" data-bs-toggle="modal" data-bs-target="#productSelector" 
                            onclick="selectProduct('${id}', '${product.id}', '${product.name}', '${product.num}', '${product.price}', '${product.notes}')">选择</button>
                    </div>
                </div>
            </div>
        `;

        document.querySelector("#selector-list").innerHTML += html;
    });

    document.querySelector("#pageInfo").innerText = `第${selectorIndex}页/共${selectorLastIndex}页`;
}