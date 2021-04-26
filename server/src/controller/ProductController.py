import json, math, uuid
from flask import *
from service.ProductService import *
from util.Configuration import *

class ProductController:

    def __init__(self):
        self.pageSize = Configuration().get("PageSize")
        self.productService = ProductService()

    # 产品列表
    def index(self):
        
        currentIndex = request.args.get("page")
        if currentIndex is None:
            return None

        lastIndex = math.ceil(self.productService.count() / float(self.pageSize))

        products = self.productService.list(int(currentIndex) - 1, self.pageSize)

        result = []
        for product in products:
            result.append(product.dicted())

        return json.dumps({
            "currentIndex": currentIndex,
            "lastIndex": lastIndex,
            "products": result
        })

    # 新增产品
    def add(self):

        if request.method != "POST":
            return None

        flag = False

        try:
            product = Product.dict2Obj(json.loads(request.data))
            product.id = str(uuid.uuid4())
            flag = self.productService.add(product)
        except: {}

        return json.dumps({
            "successful": flag
        })

    # 删除产品
    def delete(self):     

        productId = request.args.get("id")
        if productId is None:
            return None

        return json.dumps({
            "successful": self.productService.delete(productId)
        })

    # 修改产品信息
    def modify(self):

        if request.method != "POST":
            return None

        flag = False

        try:
            product = Product.dict2Obj(json.loads(request.data))
            flag = self.productService.modify(product)
        except: {}

        return json.dumps({
            "successful": flag
        })

    # 查找指定产品
    def find(self):

        productId = request.args.get("id")
        if productId is None:
            return None
        
        product = self.productService.find(productId)

        return json.dumps(product.dicted())