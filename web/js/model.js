class Product {
    constructor(name, price, num, specifications, notes) {
        this.id = "",
        this.name = name,
        this.price = Number(price),
        this.num = Number(num),
        this.specifications = specifications,
        this.notes = notes;
    }
}

class User {
    constructor(name, tel, address, notes) {
        this.id = "",
        this.name = name,
        this.tel = tel,
        this.address = address,
        this.notes = notes;
    }
}

class PurchaseOrder {
    constructor(purchaseOperations) {
        this.id = "",
        this.time = "",
        this.state = "",
        this.purchaseOperations = purchaseOperations;
    }
}

class PurchaseOperation {
    constructor(product, num) {
        this.id = "",
        this.product = product,
        this.num = num
    }
}
