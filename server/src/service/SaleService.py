import sqlite3
from server.src.model.SaleOrder import *

# 销售管理
class SaleService:

    def __init__(self):
        self.saleOrders = DbService("saleOrders")
        self.conn = sqlite3.connect('server/erp.db')

    # 释放连接
    def dispose(self):
        self.conn.close()

    # 新增销售订单
    def add(self, saleOrder: SaleOrder) -> bool:
        print()

    # 删除销售订单
    def delete(self, id: str) -> bool:
        print()

    # 修改销售订单
    def modify(self, saleOrder: SaleOrder):
        print()

    # 查找销售订单
    def find(self, id: str):
        print()