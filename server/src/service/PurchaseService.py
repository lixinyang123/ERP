import sqlite3
from server.src.service.DbService import *
from server.src.model.PurchaseOrder import *

# 采购管理
class PurchaseService:

    def __init__(self):
        self.purchaseOrder = DbService("purchaseOrder")
        self.purchaseOperations = DbService("purchaseOperations")
        self.conn = sqlite3.connect('server/erp.db')

    # 释放连接
    def dispose(self):
        self.conn.close()

    # 新增采购订单
    def add(self, product: PurchaseOrder) -> bool:
        print("add PurchaseOrder")

    # 删除采购订单
    def delete(self, id: int) -> bool:
        print("delete PurchaseOrder")

    # 更新采购订单
    def modify(self, product: PurchaseOrder) -> bool:
        print("modify PurchaseOrder")

    # 查找采购订单
    def find(self, id: int) -> Product:
        print("find PurchaseOrder")