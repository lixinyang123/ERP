from datetime import *

# 结账记录
class CheckOut:

    def __init__(self, id: str, time: datetime, amount: float):
        # ID
        self.id: str = id
        # 时间
        self.time: datetime = time
        # 付款金额
        self.amount: float = amount
