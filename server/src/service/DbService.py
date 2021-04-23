from xml.dom.minidom import parse
import xml.dom.minidom

class DbService:

    # 构造器初始化操作表
    def __init__(self, tableName: str):
        DOMTree = parse("server/DbOperation.xml")
        tables = DOMTree.documentElement
        self.table = tables.getElementsByTagName(tableName)[0]

    # 获取指定操作的 SQL
    def GetOperation(self, operationName: str) -> str:
        return self.table.getElementsByTagName(operationName)[0].childNodes[0].data.strip()