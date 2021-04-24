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
