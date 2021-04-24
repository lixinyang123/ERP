# 结账记录
class CheckOut:

    def __init__(self, id: str, time: str, amount: float):
        # ID
        self.id: str = id
        # 时间
        self.time: str = time
        # 付款金额
        self.amount: float = amount

    def dicted(self) -> dict:
        return self.__dict__