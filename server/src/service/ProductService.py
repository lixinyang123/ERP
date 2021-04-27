from service.DbService import *
from model import *

# 产品管理
class ProductService:

    def __init__(self):
        self.products = DbService("products")
        self.checkOuts = DbService("checkOuts")

        self.purchaseOperations = DbService("purchaseOperations")
        self.saleOperations = DbService("saleOperations")

        self.purchaseOrders = DbService("purchaseOrders")
        self.saleOrders = DbService("saleOrders")

        self.conn = getConnection()

    # 释放连接
    def dispose(self):
        disposeConnection(self.conn)

    # 新增产品
    def add(self, product: Product) -> bool:

        try:
            cursor = self.conn.cursor()

            paras = [product.id, product.name, product.price, product.num, product.specifications, product.notes]
            rows = cursor.execute(self.products.GetOperation("add"), paras)
            
            if rows.rowcount != 0:
                self.conn.commit()
                return True
            return False
            
        except:
            return False

    # 删除产品
    def delete(self, id: str) -> bool:

        try:
            cursor = self.conn.cursor()

            # 删除此商品的进货订单
            rows = cursor.execute(self.purchaseOperations.GetOperation("findByProduct"), [id]).fetchall()
            for row in rows:
                cursor.execute(self.purchaseOperations.GetOperation("delete"), [row[1]])
                cursor.execute(self.purchaseOrders.GetOperation("delete"), [row[1]])

            # 删除此商品的出货订单
            rows = cursor.execute(self.saleOperations.GetOperation("findByProduct"), [id])
            for row in rows:
                cursor.execute(self.saleOperations.GetOperation("delete"), [row[1]])
                cursor.execute(self.checkOuts.GetOperation("delete"), [row[1]])
                cursor.execute(self.saleOrders.GetOperation("delete"), [row[1]])

            # 删除此商品
            rows = cursor.execute(self.products.GetOperation("delete"), [id])
            
            if rows.rowcount != 0:
                self.conn.commit()
                return True
            return False
            
        except Exception as e:
            return False

    # 更新产品信息
    def modify(self, product: Product) -> bool:

        try:
            cursor = self.conn.cursor()

            paras = [product.name, product.price, product.num, product.specifications, product.notes, product.id]
            rows = cursor.execute(self.products.GetOperation("modify"), paras)
            
            if rows.rowcount != 0:
                self.conn.commit()
                return True
            return False
            
        except:
            return False

    # 查找产品
    def find(self, id: str) -> Product:
        
        try:
            cursor = self.conn.cursor()
            rows = cursor.execute(self.products.GetOperation("find"), [id])
            for row in rows:
                return Product(row[0], row[1], float(row[2]), int(row[3]), row[4], row[5])
            raise "can't find product"
                
        except:
            return None

    # 产品列表
    def list(self, pageIndex: int, pageSize: int) -> list:

        try:
            cursor = self.conn.cursor()

            results = list()
            rows = cursor.execute(self.products.GetOperation("list"), [pageIndex*pageSize, pageSize]).fetchall()
            for row in rows:
                results.append(Product(row[0], row[1], float(row[2]), int(row[3]), row[4], row[5]))

            return results
        
        except:
            return []

    # 获取产品信息数量
    def count(self) -> int:

        try:
            cursor = self.conn.cursor()

            for row in cursor.execute(self.products.GetOperation("count")):
                return row[0]
            return 0

        except:
            return 0