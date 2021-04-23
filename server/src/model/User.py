# 用户
class User:
    # ID
    id = None
    # 姓名
    name = None
    # 电话
    tel = None
    # 地址
    address = None
    # 备注
    notes = None

    def __init__(self,id,name,tel,address,notes):
        self.id = id
        self.name = name
        self.tel = tel
        self.address = address
        self.notes = notes
