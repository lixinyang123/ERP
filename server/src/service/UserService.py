from service.DbService import *
from model import *

# 用户管理
class UserService:

    def __init__(self):
        self.users = DbService("users")
        self.saleOperations = DbService("saleOperations")
        self.checkOuts = DbService("checkOuts")
        self.saleOrders = DbService("saleOrders")
        self.conn = getConnection()

    # 释放连接
    def dispose(self):
        disposeConnection(self.conn)

    # 新增用户
    def add(self, user: User) -> bool:
        
        try:
            cursor = self.conn.cursor()

            paras = [user.id, user.name, user.tel, user.address, user.notes]
            rows = cursor.execute(self.users.GetOperation("add"), paras)

            if rows.rowcount != 0:
                self.conn.commit()
                return True
            return False
            
        except:
            return False

    # 删除用户
    def delete(self, id: str) -> bool:
        
        try:
            cursor = self.conn.cursor()

            # 删除此用户的出货订单、订单操作、账单
            rows = cursor.execute(self.saleOrders.GetOperation("findByUser"), [id]).fetchall()
            for row in rows:
                cursor.execute(self.saleOperations.GetOperation("delete"), [row[0]])
                cursor.execute(self.checkOuts.GetOperation("delete"), [row[0]])
                cursor.execute(self.saleOrders.GetOperation("delete"), [row[0]])

            rows = cursor.execute(self.users.GetOperation("delete"), [id])

            if rows.rowcount != 0:
                self.conn.commit()
                return True
            return False
            
        except Exception as e:
            return False

    # 修改用户信息
    def modify(self, user: User) -> bool:
        
        try:
            cursor = self.conn.cursor()

            paras = [user.name, user.tel, user.address, user.notes, user.id]
            rows = cursor.execute(self.users.GetOperation("modify"), paras)
            
            if rows.rowcount != 0:
                self.conn.commit()
                return True
            return False
            
        except:
            return False

    # 查找用户信息
    def find(self, id: str) -> User:
        
        try:
            cursor = self.conn.cursor()
            rows = cursor.execute(self.users.GetOperation("find"), [id])
            for row in rows:
                return User(row[0], row[1], int(row[2]), row[3], row[4])
            raise "can't find user"

        except:
            return None

    # 用户信息列表
    def list(self, pageIndex: int, pageSize: int) -> list:

        try:
            cursor = self.conn.cursor()

            results = list()
            rows = cursor.execute(self.users.GetOperation("list"), [pageIndex*pageSize, pageSize]).fetchall()
            for row in rows:
                results.append(User(row[0], row[1], int(row[2]), row[3], row[4]))

            return results
        
        except:
            return []

    # 获取用户信息数量
    def count(self) -> int:

        try:
            cursor = self.conn.cursor()

            for row in cursor.execute(self.users.GetOperation("count")):
                return row[0]
            return 0

        except:
            return 0