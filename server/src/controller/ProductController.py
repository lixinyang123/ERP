import json, math
from flask import request
from service.ProductService import *

class ProductController:

    def __init__(self):
        self.pageSize = Configuration().get("PageSize")
        self.productService = ProductService()

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