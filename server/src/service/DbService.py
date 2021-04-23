from xml.dom.minidom import parse
import xml.dom.minidom

class DbService:

    # 构造器初始化操作表
    def __init__(self, tableName):
        DOMTree = parse("server/src/DbOperation.xml")
        tables = DOMTree.documentElement
        self.table = tables.getElementsByTagName(tableName)[0]

    # 获取指定操作的 SQL
    def GetOperation(self, operationName):
        return self.table.getElementsByTagName(operationName)[0].childNodes[0].data.strip()