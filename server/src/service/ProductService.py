from service.DbService import *
from model import *

# 产品管理
class ProductService:

    def __init__(self):
        self.products = DbService("products")
        self.conn = getConnection()

    # 释放连接
    def dispose(self):
        disposeConnection(self.conn)

    # 新增产品
    def add(self, product: Product) -> bool:

        sql = self.products.GetOperation("add")
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, [product.id, product.name, product.price, product.num, product.specifications, product.notes])
            self.conn.commit()
            return True
            
        except:
            return False

    # 删除产品
    def delete(self, id: str) -> bool:

        sql = self.products.GetOperation("delete")
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, [id])
            self.conn.commit()
            return True
            
        except Exception as e:
            return False

    # 更新产品信息
    def modify(self, product: Product) -> bool:

        sql = self.products.GetOperation("modify")
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, [product.name, product.price, product.num, product.specifications, product.notes, product.id])
            self.conn.commit()
            return True
            
        except:
            return False

    # 查找产品
    def find(self, id: str) -> Product:
        
        sql = self.products.GetOperation("find")
        try:
            cursor = self.conn.cursor()
            rows = cursor.execute(sql, [id])
            for row in rows:
                return Product(row[0], row[1], float(row[2]), int(row[3]), row[4], row[5])
            raise "can't find product"
                
        except:
            return None

    # 产品列表
    def list(self, pageIndex: int, pageSize: int) -> list:

        sql = self.products.GetOperation("list")
        try:
            cursor = self.conn.cursor()

            results = list()
            rows = cursor.execute(sql, [pageIndex*pageSize, pageSize]).fetchall()
            for row in rows:
                results.append(Product(row[0], row[1], float(row[2]), int(row[3]), row[4], row[5]))

            return results
        
        except:
            return []

    # 获取产品信息数量
    def count(self) -> int:

        sql = self.products.GetOperation("count")
        try:
            cursor = self.conn.cursor()

            for row in cursor.execute(sql):
                return row[0]
            return 0

        except:
            return 0