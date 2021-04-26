import json, math
from flask import request
from service.PurchaseService import *

class PurchaseController:

    def __init__(self):
        self.pageSize = Configuration().get("PageSize")
        self.purchaseService = PurchaseService()

    def index(self):
        
        currentIndex = request.args.get("page")
        if currentIndex is None:
            return None

        lastIndex = math.ceil(self.purchaseService.count() / float(self.pageSize))

        purchases = self.purchaseService.list(int(currentIndex) - 1, self.pageSize)

        result = []
        for purchase in purchases:
            result.append(purchase.dicted())

        return json.dumps({
            "currentIndex": currentIndex,
            "lastIndex": lastIndex,
            "purchases": result
        })