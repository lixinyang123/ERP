from service.DbService import *
from model import *

# 销售管理
class SaleService:

    def __init__(self):
        self.saleOrders = DbService("saleOrders")
        self.saleOperations = DbService("saleOperations")
        self.checkOuts = DbService("checkOuts")
        self.products = DbService("products")
        self.users = DbService("users")
        self.conn = getConnection()

    # 释放连接
    def dispose(self):
        disposeConnection(self.conn)

    # 新增销售订单
    def add(self, order: SaleOrder) -> bool:

        try:
            cursor = self.conn.cursor()

            paras = [order.id, order.time, order.state, order.user.id, order.selling]
            cursor.execute(self.saleOrders.GetOperation("add"), paras)

            for operation in order.saleOperations:
                paras = [operation.id, order.id, operation.product.id, operation.num]
                cursor.execute(self.saleOperations.GetOperation("add"), paras)

            for checkOut in order.checkOuts:
                paras = [checkOut.id, order.id, checkOut.time, checkOut.amount]
                cursor.execute(self.checkOuts.GetOperation("add"), )

            self.conn.commit()
            return True
            
        except Exception as e:
            return False
        
    # 删除销售订单
    def delete(self, id: str) -> bool:
        
        try:
            cursor = self.conn.cursor()
            
            # 删除此订单的进出库和结账记录
            cursor.execute(self.checkOuts.GetOperation("delete"), [id])
            cursor.execute(self.saleOperations.GetOperation("delete"), [id])

            cursor.execute(self.saleOrders.GetOperation("delete"), [id])

            self.conn.commit()
            return True

        except:
            return False

    # 修改销售订单
    def modify(self, order: SaleOrder) -> bool:
         
        try:
            cursor = self.conn.cursor()

            paras = [order.state, order.selling, order.id]
            cursor.execute(self.saleOrders.GetOperation("modify"), paras)

            for operation in order.saleOperations:
                paras = [operation.product.id, operation.num, operation.id]
                cursor.execute(self.saleOperations.GetOperation("modify"), paras)

            for checkOut in order.checkOuts:
                paras = [checkOut.amount, checkOut.id]
                cursor.execute(self.checkOuts.GetOperation("add"), paras)

            self.conn.commit()
            return True

        except:
            return False

    # 查找销售订单
    def find(self, id: str) -> SaleOrder:

        try:
            cursor = self.conn.cursor()

            # 商品操作记录
            rows = cursor.execute(self.saleOperations.GetOperation("find"), [id]).fetchall()

            operations = list()
            for row in rows:

                # 操作产品信息
                product = None
                results = cursor.execute(self.products.GetOperation("find"), [row[2]])

                for result in results:
                    product = Product(result[0], result[1], float(result[2]), int(result[3]), result[4], result[5])
                    break

                operations.append(ProductOperation(row[0], product, row[3]))
            

            # 订单付款记录
            rows = cursor.execute(self.checkOuts.GetOperation("find"), [id]).fetchall()

            checkOutList = list()
            for row in rows:
                checkOutList.append(CheckOut(row[0], row[2], row[3]))
            
            # 订单
            rows = cursor.execute(self.saleOrders.GetOperation("find"), [id])
            for row in rows:

                # 订单用户信息
                user = None
                results = cursor.execute(self.users.GetOperation("find"), [row[3]])

                for result in results:
                    user = User(row[0], row[1], int(row[2]), row[3], row[4])
                    break

                return SaleOrder(row[0], row[1], row[2], user, row[4], operations, checkOutList)

            raise "can't find order"

        except Exception as e:
            return None

    # 销售订单列表
    def list(self, pageIndex: int, pageSize: int) -> list:
        
        try:
            cursor = self.conn.cursor()
            rows = cursor.execute(self.saleOrders.GetOperation("list"), [pageIndex*pageSize, pageSize]).fetchall()

            results = []
            for row in rows:
                results.append(self.find(row[0]))
            
            return results

        except:
            return[]

    # 获取销售订单数量
    def count(self) -> int:

        try:
            cursor = self.conn.cursor()

            for row in cursor.execute(self.saleOrders.GetOperation("count")):
                return row[0]
            return 0

        except:
            return 0