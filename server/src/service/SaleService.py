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

            for operation in order.saleOperations:
                paras = [operation.id, order.id, operation.product.id, operation.num]
                cursor.execute(self.saleOperations.GetOperation("add"), paras)

            for checkOut in order.checkOuts:
                paras = [checkOut.id, order.id, checkOut.time, checkOut.amount]
                cursor.execute(self.checkOuts.GetOperation("add"), paras)

            paras = [order.id, order.time, order.state, order.user.id, order.selling]
            rows = cursor.execute(self.saleOrders.GetOperation("add"), paras)

            if rows.rowcount != 0:
                self.conn.commit()
                return True
            return False
            
        except Exception as e:
            return False
        
    # 删除销售订单
    def delete(self, id: str) -> bool:
        
        try:
            cursor = self.conn.cursor()
            
            # 删除此订单的进出库和结账记录
            cursor.execute(self.checkOuts.GetOperation("delete"), [id])
            cursor.execute(self.saleOperations.GetOperation("delete"), [id])

            rows = cursor.execute(self.saleOrders.GetOperation("delete"), [id])

            if rows.rowcount != 0:
                self.conn.commit()
                return True
            return False

        except:
            return False

    # 修改销售订单
    def modify(self, order: SaleOrder) -> bool:
         
        try:
            cursor = self.conn.cursor()

            for operation in order.saleOperations:
                paras = [operation.product.id, operation.num, operation.id]
                cursor.execute(self.saleOperations.GetOperation("modify"), paras)

            for checkOut in order.checkOuts:
                paras = [checkOut.amount, checkOut.id]
                cursor.execute(self.checkOuts.GetOperation("modify"), paras)

            paras = [order.state, order.selling, order.id]
            rows = cursor.execute(self.saleOrders.GetOperation("modify"), paras)

            if rows.rowcount != 0:
                self.conn.commit()
                return True
            return False

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
                results = cursor.execute(self.products.GetOperation("find"), [row[3]])

                for result in results:
                    product = Product(result[1], result[2], float(result[3]), int(result[4]), result[5], result[6])
                    break

                operations.append(ProductOperation(row[1], product, row[4]))
            

            # 订单付款记录
            rows = cursor.execute(self.checkOuts.GetOperation("find"), [id]).fetchall()

            checkOutList = list()
            for row in rows:
                checkOutList.append(CheckOut(row[1], row[3], row[4]))
            
            # 订单
            rows = cursor.execute(self.saleOrders.GetOperation("find"), [id])
            for row in rows:

                # 订单用户信息
                user = None
                results = cursor.execute(self.users.GetOperation("find"), [row[4]])

                for result in results:
                    user = User(result[1], result[2], int(result[3]), result[4], result[5])
                    break

                return SaleOrder(row[1], row[2], row[3], user, row[5], operations, checkOutList)

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
                results.append(self.find(row[1]))
            
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

    # 完成销售订单
    def complete(self, id: str) -> bool:

        cursor = self.conn.cursor()

        try:
            order = self.find(id)
            if order == None or order.state:
                return False

            flag = True
            for operation in order.saleOperations:
                product = operation.product
                num = product.num - operation.num

                paras = [product.name, product.price, num, product.specifications, product.notes, product.id]
                rows = cursor.execute(self.products.GetOperation("modify"), paras)

                if rows.rowcount == 0:
                    flag = False

            rows = cursor.execute(self.saleOrders.GetOperation("modify"), [True, order.selling, id])
            if rows.rowcount == 0:
                flag = False

            if flag:
                self.conn.commit()
            return flag

        except:
            return False