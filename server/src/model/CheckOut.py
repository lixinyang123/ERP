# 结账记录
class CheckOut:
    # ID
    id = None
    # 时间
    time = None
    # 付款金额
    amount = None

    def __init__(self,id,name,tel,address,notes):
        self.id = id
        self.name = name
        self.tel = tel
        self.address = address
        self.notes = notes
