# 产品
class Product:

    def __init__(self, id: int, price: float, num: int, specifications: str, notes: str):
        # ID
        self.id: int = id
        # 价格
        self.price: float = price
        # 库存数量
        self.num: int = num
        # 规格
        self.specifications: str = specifications
        # 备注
        self.notes: str = notes
