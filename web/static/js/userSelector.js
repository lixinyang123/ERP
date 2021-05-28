var selectorIndex = 1;
var selectorLastIndex = 1;
var selectorNext, selectorPrevious;

async function showUsers() {

    let results = await (await fetch(api + "/user/index?page=" + selectorIndex)).json();
    selectorLastIndex = results.lastIndex;

    selectorNext = () => {
        selectorIndex++;
        if(selectorIndex > selectorLastIndex)
            selectorIndex = selectorLastIndex;
        showUsers();
    };

    selectorPrevious = () => {
        selectorIndex--;
        if(selectorIndex < 1)
            selectorIndex = 1;
        showUsers();
    };

    document.querySelector("#selector-list").innerHTML = null;

    results.users.forEach(user => {
        let html = `
            <div class="col-md-12 animate__animated animate__bounceIn">
                <div class="card">
                    <div class="card-body">
                        <div class="row">
                            <div class="col-md-2"><p>姓名：${user.name}</p></div>
                            <div class="col-md-2"><p>电话：${user.tel}</p></div>
                            <div class="col-md-3"><p>地址：${user.address}</p></div>
                            <div class="col-md-3"><p>备注：${user.notes}</p></div>
                            <div class="col-md-2">
                            <button class="btn btn-success" data-bs-toggle="modal" data-bs-target="#productSelector" 
                                onclick="selectUser('${user.id}', '${user.name}', '${user.notes}')">选择</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;

        document.querySelector("#selector-list").innerHTML += html;
    });

    document.querySelector("#pageInfo").innerText = `第${selectorIndex}页/共${selectorLastIndex}页`;
}