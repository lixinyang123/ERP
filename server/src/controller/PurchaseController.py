import json, math, uuid
from datetime import datetime
from flask import *
from service.PurchaseService import *
from util.Configuration import *

class PurchaseController:

    def __init__(self):
        self.pageSize = Configuration().get("PageSize")

    # 进货订单列表
    def index(self):
        purchaseService = PurchaseService()
        
        currentIndex = request.args.get("page")
        if currentIndex is None:
            return None

        lastIndex = math.ceil(purchaseService.count() / float(self.pageSize))

        purchases = purchaseService.list(int(currentIndex) - 1, self.pageSize)

        result = []
        for purchase in purchases:
            result.append(purchase.dicted())

        result = json.dumps({
            "currentIndex": currentIndex,
            "lastIndex": lastIndex,
            "purchases": result
        })

        purchaseService.dispose()
        return result

    # 新增进货订单
    def add(self):
        purchaseService = PurchaseService()

        if request.method != "POST":
            return None

        flag = False

        try:
            order = PurchaseOrder.dict2Obj(json.loads(request.data))
            order.id = str(uuid.uuid4())
            order.time = str(datetime.now())
            order.state = False
            
            for operation in order.purchaseOperations:
                operation.id = str(uuid.uuid4())
            
            flag = purchaseService.add(order)
        except Exception as e: {
            print(e)
        }

        result = json.dumps({
            "successful": flag
        })

        purchaseService.dispose()
        return result

    # 删除进货订单
    def delete(self):
        purchaseService = PurchaseService()

        orderId = request.args.get("id")
        if orderId is None:
            return None

        result = json.dumps({
            "successful": purchaseService.delete(orderId)
        })

        purchaseService.dispose()
        return result

    # 修改进货信息
    def modify(self):
        purchaseService = PurchaseService()

        if request.method != "POST":
            return None

        flag = False

        try:
            order = PurchaseOrder.dict2Obj(json.loads(request.data))
            flag = purchaseService.modify(order)
        except: {}

        result = json.dumps({
            "successful": flag
        })

        purchaseService.dispose()
        return result

    # 查找进货信息
    def find(self):
        purchaseService = PurchaseService()

        orderId = request.args.get("id")
        if orderId is None:
            return None
        
        order = purchaseService.find(orderId)

        purchaseService.dispose()

        return json.dumps(order.dicted())
