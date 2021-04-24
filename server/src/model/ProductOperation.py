from server.src.model.Product import *

# 进出库操作
class SaleOperation:

    def __init__(self, id: str, product: Product, num: int):
        # ID
        self.id: str = id
        # 商品
        self.product: Product = product
        # 操作商品数量
        self.num: int = num
