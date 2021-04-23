import sqlite3
from server.src.model.User import *

# 用户管理
class UserService:

    def Add(self, user: User):
        print("add user")

    def Delete(self, id: int):
        print("delete user")

    def Modify(self, user: User):
        print("modify user")

    def Get(self, id: int):
        print("search user")