import sqlite3
from server.src.service.DbService import *
from server.src.model.PurchaseOrder import *

# 用户管理
class PurchaseService:

    def __init__(self):
        self.operations = DbService("purchaseOrder")
        self.conn = sqlite3.connect('server/erp.db')

    # 释放连接
    def dispose(self):
        self.conn.close()

    # 新增产品
    def add(self, product: PurchaseOrder) -> bool:
        print("add PurchaseOrder")

    # 删除产品
    def delete(self, id: int) -> bool:
        print("delete PurchaseOrder")

    # 更新产品信息
    def modify(self, product: PurchaseOrder) -> bool:
        print("modify PurchaseOrder")

    # 查找产品
    def find(self, id: int) -> Product:
        print("find PurchaseOrder")