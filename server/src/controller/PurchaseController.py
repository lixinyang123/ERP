import json, math, uuid
from datetime import datetime
from flask import *
from service.PurchaseService import *
from util.Configuration import *

class PurchaseController:

    def __init__(self):
        self.pageSize = Configuration().get("PageSize")
        self.purchaseService = PurchaseService()

    # 进货订单列表
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

    # 新增进货订单
    def add(self):

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
            
            flag = self.purchaseService.add(order)
        except Exception as e: {
            print(e)
        }

        return json.dumps({
            "successful": flag
        })

    # 删除进货订单
    def delete(self):

        orderId = request.args.get("id")
        if orderId is None:
            return None

        return json.dumps({
            "successful": self.purchaseService.delete(orderId)
        })

    # 修改进货信息
    def modify(self):

        if request.method != "POST":
            return None

        flag = False

        try:
            order = PurchaseOrder.dict2Obj(json.loads(request.data))
            flag = self.purchaseService.modify(order)
        except: {}

        return json.dumps({
            "successful": flag
        })

    # 查找进货信息
    def find(self):

        orderId = request.args.get("id")
        if orderId is None:
            return None
        
        order = self.purchaseService.find(orderId)

        return json.dumps(order.dicted())
