import json, math, uuid
from flask import *
from service.ProductService import *
from util.Configuration import *

class ProductController:

    def __init__(self):
        self.pageSize = Configuration().get("PageSize")

    # 产品列表
    def index(self):
        productService = ProductService()
        
        currentIndex = request.args.get("page")
        if currentIndex is None:
            return None

        lastIndex = math.ceil(productService.count() / float(self.pageSize))

        products = productService.list(int(currentIndex) - 1, self.pageSize)

        result = []
        for product in products:
            result.append(product.dicted())

        productService.dispose()

        return json.dumps({
            "currentIndex": currentIndex,
            "lastIndex": lastIndex,
            "products": result
        })

    # 新增产品
    def add(self):
        productService = ProductService()

        if request.method != "POST":
            return None

        flag = False

        try:
            product = Product.dict2Obj(json.loads(request.data))
            product.id = str(uuid.uuid4())
            flag = productService.add(product)
        except: {}

        productService.dispose()

        return json.dumps({
            "successful": flag
        })

    # 删除产品
    def delete(self):
        productService = ProductService()

        productId = request.args.get("id")
        if productId is None:
            return None

        productService.dispose()

        return json.dumps({
            "successful": productService.delete(productId)
        })

    # 修改产品信息
    def modify(self):
        productService = ProductService()

        if request.method != "POST":
            return None

        flag = False

        try:
            product = Product.dict2Obj(json.loads(request.data))
            flag = productService.modify(product)
        except: {}

        productService.dispose()

        return json.dumps({
            "successful": flag
        })

    # 查找指定产品
    def find(self):
        productService = ProductService()

        productId = request.args.get("id")
        if productId is None:
            return None
        
        product = productService.find(productId)

        productService.dispose()

        return json.dumps(product.dicted())