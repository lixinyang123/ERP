# 出售订单
class SaleOrder:
    # ID
    id = None
    # 时间
    time = None
    # 状态（订单完成状态）
    state = None
    # 用户
    user = None
    # 售价
    selling = None
    # 出库操作 ProductOperation[]
    saleOperations = []
    # 结账记录
    checkOuts = []

    def __init__(self,id,time,state,user,selling,saleOperations,checkOuts):
        self.id = id
        self.time = time
        self.state = state
        self.user = user
        self.selling = selling
        self.saleOperations = saleOperations
        self.checkOuts = checkOuts
