from server.src.model import *

# 进出库操作
class ProductOperation:

    def __init__(self, id: str, product: Product, num: int):
        # ID
        self.id: str = id
        # 商品
        self.product: Product = product
        # 操作商品数量
        self.num: int = num

    def dicted(self) -> dict:
        self.product = self.product.dicted()
        return self.__dict__