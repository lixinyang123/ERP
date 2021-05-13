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
    //addOperations();
}