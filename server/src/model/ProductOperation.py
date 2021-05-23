from model.Product import *

# 进出库操作
class ProductOperation:

    def __init__(self, id: str, product: Product, salePrice: float, num: int):
        # ID
        self.id: str = id
        # 商品
        self.product: Product = product
        # 售价
        self.salePrice: float = salePrice
        # 操作商品数量
        self.num: int = num

    def dicted(self) -> dict:
        self.product = self.product.dicted()
        return self.__dict__

    def dict2Obj(dict: dict):
        product = Product.dict2Obj(dict["product"])
        return ProductOperation(dict["id"], product, dict["salePrice"], dict["num"])