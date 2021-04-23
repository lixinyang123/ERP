# 采购订单
class PurchaseOrder:
    # ID
    id = None
    # 时间
    time = None
    # 状态（订单完成状态）
    state = None
    # 进库操作 ProductOperation[]
    purchaseOperations = []

    def __init__(self,id,time,state,purchaseOperations):
        self.id = id
        self.name = name
        self.time = time
        self.state = state
        self.purchaseOperations = purchaseOperations
