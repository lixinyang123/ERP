class Product {
    constructor(name, price, num, specifications, notes) {
        this.id = "",
        this.name = name,
        this.price = Number(price),
        this.num = Number(num),
        this.specifications = specifications,
        this.notes = notes
    }
}

class User {
    constructor(name, tel, address, notes) {
        this.id = "",
        this.name = name,
        this.tel = tel,
        this.address = address,
        this.notes = notes
    }
}

class ProductOperation {
    constructor(product, salePrice, num) {
        this.id = "",
        this.product = product,
        this.salePrice = salePrice,
        this.num = num
    }
}

class PurchaseOrder {
    constructor(productOperations) {
        this.id = "",
        this.time = "",
        this.state = "",
        this.purchaseOperations = productOperations
    }
}

class SaleOrder {
    constructor(user, selling, productOperations, checkOuts) {
        this.id = "",
        this.time = "",
        this.state = "",
        this.user = user,
        this.selling = selling,
        this.saleOperations = productOperations,
        this.checkOuts = checkOuts
    }
}

class CheckOut {
    constructor(amount) {
        this.id = "",
        this.time = "",
        this.amount = amount
    }
}
