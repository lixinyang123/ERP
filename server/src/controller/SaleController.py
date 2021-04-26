import json, math
from flask import request
from service.SaleService import *

class SaleController:

    def __init__(self):
        self.pageSize = Configuration().get("PageSize")
        self.saleService = SaleService()

    def index(self):
        
        currentIndex = request.args.get("page")
        if currentIndex is None:
            return None

        lastIndex = math.ceil(self.saleService.count() / float(self.pageSize))

        sales = self.saleService.list(int(currentIndex) - 1, self.pageSize)

        result = []
        for sale in sales:
            result.append(sale.dicted())

        return json.dumps({
            "currentIndex": currentIndex,
            "lastIndex": lastIndex,
            "sales": result
        })