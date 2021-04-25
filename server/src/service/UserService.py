import sqlite3
from server.src.service import *
from server.src.model import *

# 用户管理
class UserService:

    def __init__(self):
        self.users = DbService("users")
        self.conn = sqlite3.connect('server/erp.db')

    # 释放连接
    def dispose(self):
        self.conn.close()

    # 新增用户
    def add(self, user: User) -> bool:
        
        sql = self.users.GetOperation("add")
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, [user.id, user.name, user.tel, user.address, user.notes])
            self.conn.commit()
            return True
            
        except:
            return False

    # 删除用户
    def delete(self, id: str) -> bool:
        
        sql = self.users.GetOperation("delete")
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, [id])
            self.conn.commit()
            return True
            
        except Exception as e:
            return False

    # 修改用户信息
    def modify(self, user: User) -> bool:
        
        sql = self.users.GetOperation("modify")
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, [user.name, user.tel, user.address, user.notes, user.id])
            self.conn.commit()
            return True
            
        except:
            return False

    # 查找用户信息
    def find(self, id: str) -> User:
        
        sql = self.users.GetOperation("find")
        try:
            cursor = self.conn.cursor()
            rows = cursor.execute(sql, [id])
            for row in rows:
                return User(row[0], row[1], int(row[2]), row[3], row[4])
            raise "can't find user"

        except:
            return None

    # 用户信息列表
    def list(self, pageIndex: int, pageSize: int) -> list:

        sql = self.users.GetOperation("list")
        try:
            cursor = self.conn.cursor()

            results = list()
            rows = cursor.execute(sql, [pageIndex*pageSize, pageSize]).fetchall()
            for row in rows:
                results.append(User(row[0], row[1], int(row[2]), row[3], row[4]))

            return results
        
        except:
            return []
