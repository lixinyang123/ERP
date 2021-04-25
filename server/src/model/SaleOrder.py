from datetime import *
from server.src.model import *

# 出售订单
class SaleOrder:

    def __init__(self, id: str, time: str, state: bool, user: User, selling: float, saleOperations: list, checkOuts: list):
        # ID
        self.id: str = id
        # 时间
        self.time: str = time
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

    def dicted(self) -> dict:
        self.user = self.user.dicted()

        results = []
        for operation in self.saleOperations:
            results.append(operation.dicted())
        self.saleOperations = results

        results = []
        for checkOut in self.checkOuts:
            results.append(checkOut.dicted())
        self.checkOuts = results

        return self.__dict__