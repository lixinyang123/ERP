-- 产品操作

    -- 新增产品
    INSERT INTO products (price, num, specifications, notes) VALUES (10, 10, "10*10", "备注");

    -- 删除产品
    DELETE FROM products WHERE id = 1;

    -- 更新产品
    UPDATE products SET price = 20, num = 20, specifications = "20*20", notes = "备注2" WHERE id = 1;

-- 用户操作

    -- 新增用户
    INSERT INTO users (name, tel, address, notes) VALUES ("lllxy", 15637606156, "洛阳", "备注");

    -- 删除用户
    DELETE FROM users WHERE id = 1;

    -- 更新用户
    UPDATE users SET name = "ccczg", tel = 13683767894, address = "郑州", notes = "备注2" WHERE id = 1;

-- 采购订单操作

    -- 新增采购订单
    INSERT INTO purchaseOrders (time, state) VALUES ("2021-4-19 06:48:51", false);

    -- 删除采购订单
    DELETE FROM purchaseOrders WHERE id = 1;

    -- 更新采购订单
    UPDATE purchaseOrders SET time = "2020-10-6 06:30:51", state = true WHERE id = 1;
