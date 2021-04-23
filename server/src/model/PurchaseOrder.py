from datetime import *

# 采购订单
class PurchaseOrder:

    def __init__(self, id: int, time: datetime ,state: bool, purchaseOperations: list):
        # ID
        self.id: int = id
        # 时间
        self.time: datetime = time
        # 状态（订单完成状态）
        self.state: bool = state
        # 进库操作 list<ProductOperation>
        self.purchaseOperations: list = purchaseOperations
