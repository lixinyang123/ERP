# 产品
class Product:
    # ID
    id = None
    # 价格
    price = None
    # 库存数量
    num = None
    # 规格
    specifications = None
    # 备注
    notes = None

    def __init__(self,id,price,num,specifications,notes):
        self.id = id
        self.price = price
        self.num = num
        self.specifications = specifications
        self.notes = notes
