import sqlite3,uuid
from server.src.service.DbService import *
from server.src.model.User import *

# 用户管理
class UserService:

    def __init__(self):
        self.operations = DbService("users")
        self.conn = sqlite3.connect('server/erp.db')

    # 释放连接
    def dispose(self):
        self.conn.close()

    # 新增用户
    def add(self, user: User) -> bool:
        
        sql = self.operations.GetOperation("add")
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (user.id, user.name, user.tel, user.address, user.notes))
            self.conn.commit()
            return True
            
        except:
            return False

    # 删除用户
    def delete(self, id: str) -> bool:
        
        sql = self.operations.GetOperation("delete")
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, id)
            self.conn.commit()
            return True
            
        except Exception as e:
            return False

    # 修改用户信息
    def modify(self, user: User):
        
        sql = self.operations.GetOperation("modify")
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (user.name, user.tel, user.address, user.notes, user.id))
            self.conn.commit()
            return True
            
        except:
            return False

    def find(self, id: str):
        
        sql = self.operations.GetOperation("find")
        try:
            cursor = self.conn.cursor()
            rows = cursor.execute(sql, id)
            for row in rows:
                return User(int(row[0]), row[1], int(row[2]), row[3], row[4])
                
        except:
            return None