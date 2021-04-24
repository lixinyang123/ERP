import sqlite3
from server.src.service.DbService import *
from server.src.model.Product import *

# 产品管理
class ProductService:

    def __init__(self):
        self.products = DbService("products")
        self.conn = sqlite3.connect('server/erp.db')

    # 释放连接
    def dispose(self):
        self.conn.close()

    # 新增产品
    def add(self, product: Product) -> bool:

        sql = self.products.GetOperation("add")
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, [product.id, product.price, product.num, product.specifications, product.notes])
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
            cursor.execute(sql, [product.price, product.num, product.specifications, product.notes, product.id])
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
                return Product(row[0], float(row[1]), int(row[2]), row[3], row[4])
                
        except:
            return None