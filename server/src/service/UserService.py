from service.DbService import *
from model import *

# 用户管理
class UserService:

    def __init__(self):
        self.users = DbService("users")
        self.conn = getConnection()

    # 释放连接
    def dispose(self):
        disposeConnection(self.conn)

    # 新增用户
    def add(self, user: User) -> bool:
        
        sql = self.users.GetOperation("add")
        try:
            cursor = self.conn.cursor()
            rows = cursor.execute(sql, [user.id, user.name, user.tel, user.address, user.notes])

            if rows.rowcount != 0:
                self.conn.commit()
                return True
            return False
            
        except:
            return False

    # 删除用户
    def delete(self, id: str) -> bool:
        
        sql = self.users.GetOperation("delete")
        try:
            cursor = self.conn.cursor()
            rows = cursor.execute(sql, [id])

            if rows.rowcount != 0:
                self.conn.commit()
                return True
            return False
            
        except Exception as e:
            return False

    # 修改用户信息
    def modify(self, user: User) -> bool:
        
        sql = self.users.GetOperation("modify")
        try:
            cursor = self.conn.cursor()
            rows = cursor.execute(sql, [user.name, user.tel, user.address, user.notes, user.id])
            if rows.rowcount != 0:
                self.conn.commit()
                return True
            return False
            
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

    # 获取用户信息数量
    def count(self) -> int:

        sql = self.users.GetOperation("count")
        try:
            cursor = self.conn.cursor()

            for row in cursor.execute(sql):
                return row[0]
            return 0

        except:
            return 0