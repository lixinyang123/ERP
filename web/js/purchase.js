var currentIndex = 1;
var lastIndex = 0;

function addPurchase() {
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
