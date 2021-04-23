# 进出库操作
class SaleOperation:
    # ID
    id = None
    # 商品
    product = None
    # 操作商品数量
    num = None

    def __init__(self,id,product,num):
        self.id = id
        self.product = product
        self.num = num
