-- 产品表
CREATE TABLE products (
    -- ID
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    -- ProductID
    productid CHAR(36) NOT NULL ,
    -- 名称
    name VARCHAR(10) NOT NULL ,
    -- 进价
    price FLOAT NOT NULL ,
    -- 库存数量
    num INTEGER NOT NULL ,
    -- 规格
    specifications VARCHAR(10) NOT NULL ,
    -- 备注
    notes VARCHAR(50)
);


-- 用户表
CREATE TABLE users (
    -- ID
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    -- UserID
    userid CHAR(36) NOT NULL ,
    -- 姓名
    name VARCHAR(10) NOT NULL ,
    -- 电话
    tel INTEGER NOT NULL ,
    -- 地址
    address VARCHAR(50) NOT NULL ,
    -- 备注
    notes VARCHAR(50)
);


-- 采购订单
CREATE TABLE purchaseOrders (
    -- ID
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    -- PurchaseOrderID
    purchaseorderid CHAR(36) NOT NULL ,
    -- 时间
    time DATETIME NOT NULL ,
    -- 状态（订单完成状态）
    state BOOLEAN NOT NULL 
);


-- 进库操作
CREATE TABLE purchaseOperations (
    -- ID
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    -- PurchaseOperationID
    purchaseoperationid CHAR(36) NOT NULL ,
    -- 订单ID
    purchaseOrderId CHAR(36) NOT NULL ,
    -- 商品ID
    productId CHAR(36) NOT NULL ,
    -- 售价
    salePrice FLOAT NOT NULL ,
    -- 操作数量
    num INTEGER NOT NULL ,
    -- 外键
    FOREIGN KEY (purchaseOrderId) REFERENCES purchaseOrders(id) ,
    FOREIGN KEY (productId) REFERENCES products(id)
);


-- 出售订单
CREATE TABLE saleOrders (
    -- ID
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    -- SaleOrderID
    saleorderid CHAR(36) NOT NULL ,
    -- 时间
    time DATETIME NOT NULL ,
    -- 状态（订单完成状态）
    state BOOLEAN NOT NULL ,
    -- 用户ID
    userId CHAR(36) NOT NULL ,
    -- 售价
    selling FLOAT NOT NULL ,
    -- 外键
    FOREIGN KEY (userId) REFERENCES users(id) 
);


-- 出库操作
CREATE TABLE saleOperations (
    -- ID
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    -- SaleOperationID
    saleoperationid CHAR(36) NOT NULL ,
    -- 订单ID
    saleOrderId CHAR(36) NOT NULL ,
    -- 商品ID
    productId CHAR(36) NOT NULL ,
    -- 售价
    salePrice FLOAT NOT NULL ,
    -- 操作数量
    num INTEGER NOT NULL ,
    -- 外键
    FOREIGN KEY (saleOrderId) REFERENCES saleOrders(id) ,
    FOREIGN KEY (productId) REFERENCES products(id)
);


-- 结账记录
CREATE TABLE checkOuts (
    -- ID
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    -- CheckOutID
    checkoutid CHAR(36) NOT NULL ,
    -- 订单ID
    saleOrderId CHAR(36) NOT NULL ,
    -- 时间
    time DATETIME NOT NULL ,
    -- 付款金额
    amount FLOAT NOT NULL ,
    -- 外键
    FOREIGN KEY (saleOrderId) REFERENCES saleOrders(id) 
);