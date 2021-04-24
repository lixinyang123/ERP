# 用户
class User:

    def __init__(self, id: str, name: str, tel: int, address: str, notes: str):
        # ID
        self.id: str = id
        # 姓名
        self.name: str = name
        # 电话
        self.tel: int = tel
        # 地址
        self.address: str = address
        # 备注
        self.notes: str = notes

    def dicted(self) -> dict:
        return self.__dict__