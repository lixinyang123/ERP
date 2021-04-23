import sqlite3
from server.src.service.DbService import *

# 用户管理
class ProductService:

    def __init__(self):
        self.operations = DbService("products")

    def Add(self,product):
        sql = self.operations.GetOperation("add")
        print(sql)

    def Delete(self,id):
        sql = self.operations.GetOperation("delete")
        print(sql)

    def Modify(self,product):
        sql = self.operations.GetOperation("modify")
        print(sql)

    def Get(self,id):
        sql = self.operations.GetOperation("find")
        print(sql)