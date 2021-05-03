import json, math, uuid
from flask import *
from service.SaleService import *
from util.Configuration import *

sale = Blueprint('sale',__name__)

pageSize = Configuration().get("PageSize")

# 销售订单列表
@sale.route("index", methods=["get"])
def index():
    saleService = SaleService()
    
    currentIndex = request.args.get("page")
    if currentIndex is None:
        return ("forbidden", 403)

    lastIndex = math.ceil(saleService.count() / float(self.pageSize))

    sales = saleService.list(int(currentIndex) - 1, self.pageSize)

    result = []
    for sale in sales:
        result.append(sale.dicted())

    result = json.dumps({
        "currentIndex": currentIndex,
        "lastIndex": lastIndex,
        "sales": result
    })

    saleService.dispose()
    return (result, 200)

# 新增销售订单
@sale.route("add", methods=["post"])
def add():
    saleService = SaleService()

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

    except: 
        return ("forbidden", 403)

    result = json.dumps({
        "successful": flag
    })

    saleService.dispose()
    return (result, 200)

# 删除销售订单
@sale.route("delete", methods=["get"])
def delete():
    saleService = SaleService()

    orderId = request.args.get("id")
    if orderId is None:
        return ("forbidden", 403)

    result = json.dumps({
        "successful": saleService.delete(orderId)
    })

    saleService.dispose()
    return (result, 200)

# 修改销售信息
@sale.route("modify", methods=["post"])
def modify():
    saleService = SaleService()

    flag = False

    try:
        order = SaleOrder.dict2Obj(json.loads(request.data))
        flag = saleService.modify(order)
    except: 
        return ("forbidden", 403)

    result = json.dumps({
        "successful": flag
    })

    saleService.dispose()
    return (result, 200)

# 查找销售信息
@sale.route("find", methods=["get"])
def find():
    saleService = SaleService()

    orderId = request.args.get("id")
    if orderId is None:
        return ("forbidden", 403)

    order = saleService.find(orderId)
    result = json.dumps(order.dicted())

    saleService.dispose()

    return (result, 200)
