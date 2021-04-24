import sqlite3
from server.src.service.DbService import *
from server.src.model.SaleOrder import *
from server.src.model.ProductOperation import *
from server.src.model.CheckOut import *

# 销售管理
class SaleService:

    def __init__(self):
        self.saleOrders = DbService("saleOrders")
        self.saleOperations = DbService("saleOperations")
        self.checkOuts = DbService("checkOuts")
        self.products = DbService("products")
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

            for operation in order.saleOperations:
                cursor.execute(saleSql, [operation.id, order.id, operation.product.id, operation.num])

            self.conn.commit()
            return True
            
        except Exception as e:
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
        addCheckOutSql = self.checkOuts.GetOperation("add")
        deleteCheckOutSql = self.checkOuts.GetOperation("delete")
        try:
            cursor = self.conn.cursor()
            cursor.execute(orderSql, [order.time, order.state, order.user.id, order.selling, order.id])
            
            cursor.execute(deleteSaleSql, [order.id])
            cursor.execute(deleteCheckOutSql, [order.id])

            for operation in order.saleOperations:
                cursor.execute(addSaleSql, [operation.id, order.id, operation.product.id, operation.num])

            for checkOut in order.checkOuts:
                cursor.execute(addCheckOutSql, [checkOut.id, order.id, checkOut.time, checkOut.amount])

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

            # 商品操作记录
            rows = cursor.execute(saleSql, [id]).fetchall()

            operations = list()
            for row in rows:

                # 操作产品信息
                product = None
                results = cursor.execute(productSql, [row[2]])

                for result in results:
                    product = Product(result[0], result[1], float(result[2]), int(result[3]), result[4], result[5])
                    break

                operations.append(ProductOperation(row[0], product, row[3]))
            

            # 订单付款记录
            rows = cursor.execute(checkOutSql, [id]).fetchall()

            checkOutList = list()
            for row in rows:
                checkOutList.append(CheckOut(row[0], row[1], row[2]))
            
            # 订单
            rows = cursor.execute(orderSql, [id])
            for row in rows:

                # 订单用户信息
                user = None
                results = cursor.execute(userSql, [row[3]])

                for result in results:
                    user = User(row[0], row[1], int(row[2]), row[3], row[4])
                    break

                return SaleOrder(row[0], row[1], row[2], user, row[4], operations, checkOutList)

            raise "can't find order"

        except Exception as e:
            return None