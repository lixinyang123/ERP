import sqlite3
from server.src.model.SaleOrder import *
from server.src.model.ProductOperation import *
from server.src.model.CheckOut import *

# 销售管理
class SaleService:

    def __init__(self):
        self.saleOrders = DbService("saleOrders")
        self.saleOperations = DbService("saleOperations")
        self.checkOuts = DbService("checkOuts")
        self.users = DbService("users")
        self.conn = sqlite3.connect('server/erp.db')

    # 释放连接
    def dispose(self):
        self.conn.close()

    # 新增销售订单
    def add(self, order: SaleOrder) -> bool:

        orderSql = self.saleOrders.GetOperation("add")
        saleSql = self.saleOperations.GetOperation("add")
        try:
            cursor = self.conn.cursor()
            cursor.execute(orderSql, [order.id, order.time, order.state, order.user.id, order.selling])

            for operation in saleOrder.saleOperations:
                cursor.execute(saleSql, [operation.id, order.id, operation.product.id, operation.num])

            self.conn.commit()
            return True
            
        except:
            return False
        
    # 删除销售订单
    def delete(self, id: str) -> bool:
        
        orderSql = self.saleOrders.GetOperation("delete")
        saleSql = self.saleOperations.GetOperation("delete")
        checkOutSql = self.checkOuts.GetOperation("delete")
        try:
            cursor = self.conn.cursor()
            cursor.execute(saleSql, [id])
            cursor.execute(orderSql, [id])
            cursor.execute(checkOutSql, [id])

            self.conn.commit()
            return True

        except:
            return False

    # 修改销售订单
    def modify(self, order: SaleOrder) -> bool:
        
        orderSql = self.saleOrders.GetOperation("modify")
        addSaleSql = self.saleOperations.GetOperation("add")
        deleteSaleSql = self.saleOperations.GetOperation("delete")
        try:
            cursor = self.conn.cursor()
            cursor.execute(orderSql, [order.time, order.state, order.user.id, order.selling, order.id])
            cursor.execute(deleteSaleSql, [order.id])

            for operation in order.saleOperations:
                cursor.execute(addSaleSql, [operation.id, order.id, operation.product.id, operation.num])

            self.conn.commit()
            return True

        except:
            return False

    # 查找销售订单
    def find(self, id: str) -> SaleOrder:
        
        orderSql = self.saleOrders.GetOperation("find")
        saleSql = self.saleOperations.GetOperation("find")
        productSql = self.products.GetOperation("find")
        checkOutSql = self.checkOuts.GetOperation("find")
        userSql = self.users.GetOperation("find")
        try:
            cursor = self.conn.cursor()
            rows = cursor.execute(saleSql, [id]).fetchall()

            operations = list()
            for row in rows:
                results = cursor.execute(productSql, [row[2]])
                product = None

                for result in results:
                    product = Product(result[0], float(result[1]), int(result[2]), result[3], result[4])
                    break

            return None

        except:
            return None