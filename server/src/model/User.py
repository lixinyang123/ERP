# 用户
class User:

    def __init__(self, id: int, name: str, tel: int, address: str, notes: str):
        # ID
        self.id: int = id
        # 姓名
        self.name: str = name
        # 电话
        self.tel: int = tel
        # 地址
        self.address: str = address
        # 备注
        self.notes: str = notes
