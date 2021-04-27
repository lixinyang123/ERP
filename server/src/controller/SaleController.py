import json, math, uuid
from flask import *
from service.SaleService import *
from util.Configuration import *

class SaleController:

    def __init__(self):
        self.pageSize = Configuration().get("PageSize")
        self.saleService = SaleService()

    # 销售订单列表
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

    # 新增销售订单
    def add(self):

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
            
            flag = self.saleService.add(order)
        except Exception as e: {
            print(e)
        }

        return json.dumps({
            "successful": flag
        })
