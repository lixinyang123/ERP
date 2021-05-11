function verify(user) {
    if(!user.name || !user.tel || !user.address || !user.notes)
        return false
    return true
}

function submit() {
    let name = document.querySelector("#user-name").value;
    let tel = document.querySelector("#user-tel").value;
    let address = document.querySelector("#user-address").value;
    let notes = document.querySelector("#user-notes").value;

    let user = new ProductModel(name, tel, address, notes);
    
    console.warn(user);
    
    if(!verify(user)){
        toast("信息不完整");
        return;
    }
    
    toast("提交成功");
}

document.querySelector("#submit").onclick = submit;