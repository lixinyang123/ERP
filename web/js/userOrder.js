
async function getData() {
    let results = await (await fetch(api + "/sale/findByUserWithState?id=" + "95727902-e88e-480f-b6f7-c0089ec4dc17")).json();
    showData(results)
}

function showData(sales) {

    document.querySelector("#sales").innerHTML = null;

    sales.forEach(sale => {

        // Get Detail
        let detail = "";
        sale.saleOperations.forEach(ele => {
            detail += `<p class="card-text"><strong>${ele.product.name}</strong> * ${ele.num}</p>`;
        });

        // Get Amount
        let amounted = 0;
        sale.checkOuts.forEach(ele => {
            amounted += ele.amount;
        });

        let payOrComplete = "";
        if(sale.selling > amounted)
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
                        <p class="card-text">总价：${sale.selling}</p>
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

getData();