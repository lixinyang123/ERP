from model.ProductOperation import *

# 采购订单
class PurchaseOrder:

    def __init__(self, id: str, time: str ,state: bool, purchaseOperations: list):
        # ID
        self.id: str = id
        # 时间
        self.time: str = time
        # 状态（订单完成状态）
        self.state: bool = state
        # 进库操作 list<ProductOperation>
        self.purchaseOperations: list = purchaseOperations

    def dicted(self) -> dict:

        results = []
        for operation in self.purchaseOperations:
            results.append(operation.dicted())
        self.purchaseOperations = results

        return self.__dict__

    def dict2Obj(dict: dict):
        
        operations = list()
        for operation in dict["purchaseOperations"]:
            operations.append(ProductOperation.dict2Obj(operation))

        return PurchaseOrder(dict["id"], dict["time"], dict["state"], operations)
