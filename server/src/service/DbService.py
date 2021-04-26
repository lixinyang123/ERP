import sqlite3
from xml.dom.minidom import *
from util.Configuration import *

# 获取数据库连接
def getConnection():
    return sqlite3.connect(Configuration().get("DatabaseCWD"))

# 释放数据库连接
def disposeConnection(conn):
    conn.close()

# 数据库操作服务
class DbService:

    # 构造器初始化操作表
    def __init__(self, tableName: str):
        DOMTree = parse("DbOperation.xml")
        tables = DOMTree.documentElement
        self.table = tables.getElementsByTagName(tableName)[0]

    # 获取指定操作的 SQL
    def GetOperation(self, operationName: str) -> str:
        return self.table.getElementsByTagName(operationName)[0].childNodes[0].data.strip()
