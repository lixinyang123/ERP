import sqlite3
from server.src.service.DbService import *
from server.src.model.Product import *

# 用户管理
class ProductService:

    def __init__(self):
        self.operations = DbService("products")
        self.conn = sqlite3.connect('server/erp.db')

    # 释放连接
    def dispose(self):
        self.conn.close()

    # 新增产品
    def Add(self, product: Product) -> bool:

        sql = self.operations.GetOperation("add")
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (product.price, product.num, product.specifications, product.notes))
            self.conn.commit()
            return True
            
        except:
            return False

    # 删除产品
    def Delete(self, id: int) -> bool:

        sql = self.operations.GetOperation("delete")
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, str(id))
            self.conn.commit()
            return True
            
        except Exception as e:
            return False

    # 更新产品信息
    def Modify(self, product: Product) -> bool:
        sql = self.operations.GetOperation("modify")

        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (product.price, product.num, product.specifications, product.notes, product.id))
            self.conn.commit()
            return True
            
        except:
            return False

    # 查找产品
    def Find(self, id: int) -> Product:
        sql = self.operations.GetOperation("find")
        
        try:
            cursor = self.conn.cursor()
            rows = cursor.execute(sql, str(id))
            for row in rows:
                return Product(int(row[0]), float(row[1]), int(row[2]), row[3], row[4])
                
        except:
            return None