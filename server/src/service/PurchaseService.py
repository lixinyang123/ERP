import sqlite3
from server.src.service.DbService import *
from server.src.model.PurchaseOrder import *
from server.src.model.ProductOperation import *

# 采购管理
class PurchaseService:

    def __init__(self):
        self.purchaseOrders = DbService("purchaseOrders")
        self.purchaseOperations = DbService("purchaseOperations")
        self.products = DbService("products")
        self.conn = sqlite3.connect('server/erp.db')

    # 释放连接
    def dispose(self):
        self.conn.close()

    # 新增采购订单
    def add(self, order: PurchaseOrder) -> bool:
        
        orderSql = self.purchaseOrders.GetOperation("add")
        purchaseSql = self.purchaseOperations.GetOperation("add")
        try:
            cursor = self.conn.cursor()
            cursor.execute(orderSql, [order.id, order.time, order.state])

            for operation in order.purchaseOperations:
                cursor.execute(purchaseSql, [operation.id, order.id, operation.product.id, operation.num])

            self.conn.commit()
            return True
            
        except:
            return False

    # 删除采购订单
    def delete(self, id: int) -> bool:
        
        orderSql = self.purchaseOrders.GetOperation("delete")
        purchaseSql = self.purchaseOperations.GetOperation("delete")
        try:
            cursor = self.conn.cursor()
            cursor.execute(purchaseSql, [id])
            cursor.execute(orderSql, [id])
            
            self.conn.commit()
            return True
        except:
            return False

    # 更新采购订单
    def modify(self, order: PurchaseOrder) -> bool:
        
        orderSql = self.purchaseOrders.GetOperation("modify")
        addPurchaseSql = self.purchaseOperations.GetOperation("add")
        deletePurchaseSql = self.purchaseOperations.GetOperation("delete")
        try:
            cursor = self.conn.cursor()
            cursor.execute(orderSql, [order.time, order.state, order.id])
            cursor.execute(deletePurchaseSql, [order.id])

            for operation in order.purchaseOperations:
                cursor.execute(addPurchaseSql, [operation.id, order.id, operation.product.id, operation.num])

            self.conn.commit()
            return True
        except:
            return False

    # 查找采购订单
    def find(self, id: str) -> PurchaseOrder:
        
        orderSql = self.purchaseOrders.GetOperation("find")
        purchaseSql = self.purchaseOperations.GetOperation("find")
        productSql = self.products.GetOperation("find")
        try:
            cursor = self.conn.cursor()
            rows = cursor.execute(purchaseSql, [id]).fetchall()

            operations = list()
            for row in rows:
                results = cursor.execute(productSql, [row[2]])
                product = None

                for result in results:
                    product = Product(result[0], float(result[1]), int(result[2]), result[3], result[4])
                    break

                operations.append(ProductOperation(row[0], product, row[3]))

            orders = cursor.execute(orderSql, [id])

            for order in orders:
                return PurchaseOrder(order[0], order[1], order[2], operations)
            
        except:
            return None