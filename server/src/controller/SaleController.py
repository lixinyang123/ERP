import json, math, uuid
from flask import *
from service.SaleService import *
from util.Configuration import *

class SaleController:

    def __init__(self):
        self.pageSize = Configuration().get("PageSize")

    # 销售订单列表
    def index(self):
        saleService = SaleService()
        
        currentIndex = request.args.get("page")
        if currentIndex is None:
            return None

        lastIndex = math.ceil(saleService.count() / float(self.pageSize))

        sales = saleService.list(int(currentIndex) - 1, self.pageSize)

        result = []
        for sale in sales:
            result.append(sale.dicted())

        saleService.dispose()

        return json.dumps({
            "currentIndex": currentIndex,
            "lastIndex": lastIndex,
            "sales": result
        })

    # 新增销售订单
    def add(self):
        saleService = SaleService()

        if request.method != "POST":
            return None

        flag = False
        
        try:
            order = SaleOrder.dict2Obj(json.loads(request.data))
            order.id = str(uuid.uuid4())
            order.time = str(datetime.now())
            order.state = False
            
            for operation in order.saleOperations:
                operation.id = str(uuid.uuid4())

            for checkOut in order.checkOuts:
                checkOut.id = str(uuid.uuid4())
                checkOut.time = str(datetime.now())
            
            flag = saleService.add(order)

        except Exception as e: {
            print(e)
        }

        saleService.dispose()

        return json.dumps({
            "successful": flag
        })

    # 删除销售订单
    def delete(self):
        saleService = SaleService()

        orderId = request.args.get("id")
        if orderId is None:
            return None

        saleService.dispose()

        return json.dumps({
            "successful": saleService.delete(orderId)
        })

    # 修改销售信息
    def modify(self):
        saleService = SaleService()

        if request.method != "POST":
            return None

        flag = False

        try:
            order = SaleOrder.dict2Obj(json.loads(request.data))
            flag = saleService.modify(order)
        except: {}

        saleService.dispose()

        return json.dumps({
            "successful": flag
        })

    # 查找销售信息
    def find(self):
        saleService = SaleService()

        orderId = request.args.get("id")
        if orderId is None:
            return None

        order = saleService.find(orderId)

        saleService.dispose()

        return json.dumps(order.dicted())
