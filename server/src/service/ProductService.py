import sqlite3
from server.src.service.DbService import *
from server.src.model.Product import *

# 用户管理
class ProductService:

    def __init__(self):
        self.operations = DbService("products")
        self.conn = sqlite3.connect('test.db').cursor()

    def Add(self, product: Product):
        sql = self.operations.GetOperation("add")
        print(sql)

    def Delete(self, id: int):
        sql = self.operations.GetOperation("delete")
        print(sql)

    def Modify(self, product: Product):
        sql = self.operations.GetOperation("modify")
        print(sql)

    def Get(self, id: int):
        sql = self.operations.GetOperation("find")
        print(sql)