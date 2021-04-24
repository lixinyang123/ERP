-- 产品操作

    -- 查询产品
    SELECT * FROM products LIMIT 0,10;

    SELECT * FROM products WHERE id = 1;

    -- 新增产品
    INSERT INTO products (price, num, specifications, notes) VALUES (10, 10, "10*10", "备注");

    -- 删除产品
    DELETE FROM products WHERE id = 1;

    -- 更新产品
    UPDATE products SET price = 20, num = 20, specifications = "20*20", notes = "备注2" WHERE id = 1;


-- 用户操作

    -- 查询用户
    SELECT * FROM users LIMIT 0,10;

    SELECT * FROM users WHERE id = 1;

    -- 新增用户
    INSERT INTO users (id, name, tel, address, notes) VALUES ("lllxy", 15637606156, "洛阳", "备注");

    -- 删除用户
    DELETE FROM users WHERE id = 1;

    -- 更新用户
    UPDATE users SET name = "ccczg", tel = 13683767894, address = "郑州", notes = "备注2" WHERE id = 1;


-- 采购订单操作

    -- 查询订单
    SELECT * FROM purchaseOrders LIMIT 0,10;

    SELECT * FROM purchaseOrders, purchaseOperations ON purchaseOrders.id = purchaseOperations.purchaseOrderId LIMIT 0,10;

    SELECT * FROM purchaseOrders LEFT JOIN purchaseOperations ON purchaseOrders.id = purchaseOperations.purchaseOrderId LIMIT 0,10;

    SELECT * FROM purchaseOrders WHERE id = 1;

    -- 新增采购订单
    INSERT INTO purchaseOrders (id, time, state) VALUES ("2021-4-19 06:48:51", false);

    -- 删除采购订单
    DELETE FROM purchaseOrders WHERE id = 1;

    -- 更新采购订单
    UPDATE purchaseOrders SET time = "2020-10-6 06:30:51", state = true WHERE id = 1;


-- 进库操作

    -- 查询进库操作
    SELECT * FROM purchaseOperations LIMIT 0,10;

    SELECT * FROM purchaseOperations WHERE id = 1;

    -- 新增进库操作
    INSERT INTO purchaseOperations (id, purchaseOrderId, productId, num) VALUES (1, 1, 10);

    -- 删除进库操作
    DELETE FROM purchaseOperations WHERE id = 1;

    -- 更新进库操作
    UPDATE purchaseOperations SET purchaseOrderId = 2, productId = 2, num = 20 WHERE id = 1;


-- 出售订单操作

    -- 查询订单
    SELECT * FROM saleOrders LIMIT 0,10;

    SELECT * FROM saleOrders, saleOperations ON saleOrders.id = saleOperations.saleOrderId LIMIT 0,10;

    SELECT * FROM saleOrders LEFT JOIN saleOperations ON saleOrders.id = saleOperations.saleOrderId LIMIT 0,10;

    SELECT * FROM saleOrders WHERE id = 1;

    -- 新增出售订单
    INSERT INTO saleOrders (id, time, state, userId, selling) VALUES ("2021-4-19 06:48:51", false, 1, 100);

    -- 删除出售订单
    DELETE FROM saleOrders WHERE id = 1;

    -- 更新出售订单
    UPDATE saleOrders SET time = "2020-10-6 06:30:51", state = true, userId = 2, selling = 200 WHERE id = 1;


-- 出库操作

    -- 查询出库操作
    SELECT * FROM saleOperations LIMIT 0,10;

    SELECT * FROM saleOperations WHERE id = 1;

    -- 新增出库操作
    INSERT INTO saleOperations (id, saleOrderId, productId, num) VALUES (1, 1, 10);

    -- 删除出库操作
    DELETE FROM saleOperations WHERE id = 1;

    -- 更新出库操作
    UPDATE saleOperations SET saleOrderId = 2, productId = 2, num = 20 WHERE id = 1;


-- 结账记录操作

    -- 查询结账记录
    SELECT * FROM checkOuts LIMIT 0,10;

    SELECT * FROM checkOuts WHERE id = 1;

    -- 新增结账记录
    INSERT INTO checkOuts (id, saleOrderId, time, amount) VALUES (1, "2021-4-19 06:48:51", 50);

    -- 删除结账记录
    DELETE FROM checkOuts WHERE id = 1;

    -- 更新结账记录
    UPDATE checkOuts SET saleOrderId = 2, time = "2020-10-6 06:30:51", amount = 70 WHERE id = 1;
