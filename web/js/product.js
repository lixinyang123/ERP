function verify(product) {
    if(!product.name || !product.price || !product.num || !product.specifications || !product.notes)
        return false
    return true
}

function submit() {
    let name = document.querySelector("#product-name").value;
    let price = document.querySelector("#product-price").value;
    let num = document.querySelector("#product-num").value;
    let specifications = document.querySelector("#product-specifications").value;
    let notes = document.querySelector("#product-notes").value;

    let product = new ProductModel(name, price, num, specifications, notes);
    
    console.warn(product);
    
    if(!verify(product)){
        toast("信息不完整");
        return;
    }
    
    toast("提交成功");
}

document.querySelector("#submit").onclick = submit;