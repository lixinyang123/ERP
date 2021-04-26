from datetime import *
from model.User import *
from model.ProductOperation import *
from model.CheckOut import *

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

    def dict2Obj(dict: dict):
        user = User.dict2Obj(dict["user"])
        
        operations = list()
        for operation in dict["saleOperations"]:
            operations.append(ProductOperation.dict2Obj(operation))

        checkOutList = list()
        for checkOut in dict["checkOuts"]:
            checkOutList.append(CheckOut.dict2Obj(checkOut))

        SaleOrder(dict["id"], dict["time"], dict["state"], user, dict["selling"], operations, checkOutList)
        return 