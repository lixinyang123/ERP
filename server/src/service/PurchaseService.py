import uuid
from service.DbService import *
from model import *

# 采购管理
class PurchaseService:

    def __init__(self):
        self.purchaseOrders = DbService("purchaseOrders")
        self.purchaseOperations = DbService("purchaseOperations")
        self.products = DbService("products")
        self.conn = getConnection()

    # 释放连接
    def dispose(self):
        disposeConnection(self.conn)

    # 新增采购订单
    def add(self, order: PurchaseOrder) -> bool:
        
        try:
            cursor = self.conn.cursor()

            for operation in order.purchaseOperations:
                paras = [operation.id, order.id, operation.product.id, operation.salePrice, operation.num]
                cursor.execute(self.purchaseOperations.GetOperation("add"), paras)

            paras = [order.id, order.time, order.state]
            rows = cursor.execute(self.purchaseOrders.GetOperation("add"), paras)
            
            if rows.rowcount != 0:
                self.conn.commit()
                return True
            return False
            
        except:
            return False

    # 删除采购订单
    def delete(self, id: int) -> bool:
        
        try:
            cursor = self.conn.cursor()

            # 删除此订单的进出库记录
            cursor.execute(self.purchaseOperations.GetOperation("delete"), [id])
            rows = cursor.execute(self.purchaseOrders.GetOperation("delete"), [id])
            
            if rows.rowcount != 0:
                self.conn.commit()
                return True
            return False

        except:
            return False

    # 更新采购订单
    def modify(self, order: PurchaseOrder) -> bool:
        
        try:
            cursor = self.conn.cursor()

            currentOrder = self.find(order.id)
            if currentOrder.state:
                return False

            cursor.execute(self.purchaseOperations.GetOperation("delete"), [order.id])

            for operation in order.purchaseOperations:
                paras = [str(uuid.uuid4()), order.id, operation.product.id, operation.salePrice, operation.num]
                cursor.execute(self.purchaseOperations.GetOperation("add"), paras)

            paras = [order.state, order.id]
            rows = cursor.execute(self.purchaseOrders.GetOperation("modify"), paras)

            if rows.rowcount != 0:
                self.conn.commit()
                return True
            return False
            
        except:
            return False

    # 查找采购订单
    def find(self, id: str) -> PurchaseOrder:
        
        try:
            cursor = self.conn.cursor()
            rows = cursor.execute(self.purchaseOperations.GetOperation("find"), [id]).fetchall()

            operations = list()
            for row in rows:
                results = cursor.execute(self.products.GetOperation("find"), [row[3]])
                product = None

                for result in results:
                    product = Product(result[1], result[2], float(result[3]), int(result[4]), result[5], result[6])
                    break

                operations.append(ProductOperation(row[1], product, row[4], row[5]))

            orders = cursor.execute(self.purchaseOrders.GetOperation("find"), [id])

            for order in orders:
                return PurchaseOrder(order[1], order[2], order[3], operations)

            raise "can't find order"
            
        except:
            return None

    # 采购订单列表
    def list(self, pageIndex: int, pageSize: int) -> list:
        
        try:
            cursor = self.conn.cursor()
            rows = cursor.execute(self.purchaseOrders.GetOperation("list"), [pageIndex*pageSize, pageSize]).fetchall()

            results = []
            for row in rows:
                results.append(self.find(row[1]))
            
            return results

        except:
            return []

    # 获取采购订单数量
    def count(self) -> int:

        try:
            cursor = self.conn.cursor()

            for row in cursor.execute(self.purchaseOrders.GetOperation("count")):
                return row[0]
            return 0

        except:
            return 0

    # 完成采购订单
    def complete(self, id: str) -> bool:

        cursor = self.conn.cursor()

        try:
            order = self.find(id)
            if order == None or order.state:
                return False

            flag = True
            for operation in order.purchaseOperations:

                product = None
                rows = cursor.execute(self.products.GetOperation("find"), [operation.product.id])
                for row in rows:
                    product = Product(row[1], row[2], float(row[3]), int(row[4]) + operation.num, row[5], row[6])

                paras = [product.name, product.price, product.num, product.specifications, product.notes, product.id]
                rows = cursor.execute(self.products.GetOperation("modify"), paras)

                if rows.rowcount == 0:
                    flag = False

            rows = cursor.execute(self.purchaseOrders.GetOperation("modify"), [True, id]);
            if rows.rowcount == 0:
                flag = False

            if flag:
                self.conn.commit()
            return flag

        except:
            return False