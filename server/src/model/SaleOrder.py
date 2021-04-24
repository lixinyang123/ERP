from datetime import *
from server.src.model.User import *

# 出售订单
class SaleOrder:

    def __init__(self, id: str, time: datetime, state: bool, user: User, selling: float, saleOperations: list, checkOuts: list):
        # ID
        self.id: str = id
        # 时间
        self.time: datetime = time
        # 状态（订单完成状态）
        self.state: bool = state
        # 用户
        self.user: User = user
        # 售价
        self.selling: float = selling
        # 出库操作 list<ProductOperation>
        self.saleOperations: list = saleOperations
        # 结账记录 list<CheckOut>
        self.checkOuts: list = checkOuts
