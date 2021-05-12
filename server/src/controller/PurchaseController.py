import json, math, uuid
from datetime import datetime
from flask import *
from service.PurchaseService import *
from util.Configuration import *

purchase = Blueprint('purchase',__name__)

pageSize = Configuration().get("PageSize")

# 进货订单列表
@purchase.route("index", methods=["get"])
def index():
    purchaseService = PurchaseService()
    
    currentIndex = request.args.get("page")
    if currentIndex is None:
        return ("forbidden", 403)

    lastIndex = math.ceil(purchaseService.count() / float(pageSize))

    purchases = purchaseService.list(int(currentIndex) - 1, pageSize)

    result = []
    for purchase in purchases:
        result.append(purchase.dicted())

    result = json.dumps({
        "currentIndex": currentIndex,
        "lastIndex": lastIndex,
        "purchases": result
    })

    purchaseService.dispose()
    return (result, 200)

# 新增进货订单
@purchase.route("add", methods=["post"])
def add():
    purchaseService = PurchaseService()

    flag = False

    try:
        order = PurchaseOrder.dict2Obj(json.loads(request.data))
        order.id = str(uuid.uuid4())
        order.time = str(datetime.now())
        order.state = False
        
        for operation in order.purchaseOperations:
            operation.id = str(uuid.uuid4())
        
        flag = purchaseService.add(order)
    except:
        return ("forbidden", 403)

    result = json.dumps({
        "successful": flag
    })

    purchaseService.dispose()
    return (result, 200)

# 删除进货订单
@purchase.route("delete", methods=["get"])
def delete():
    purchaseService = PurchaseService()

    orderId = request.args.get("id")
    if orderId is None:
        return ("forbidden", 403)

    result = json.dumps({
        "successful": purchaseService.delete(orderId)
    })

    purchaseService.dispose()
    return (result, 200)

# 修改进货信息
@purchase.route("modify", methods=["post"])
def modify():
    purchaseService = PurchaseService()

    flag = False

    try:
        order = PurchaseOrder.dict2Obj(json.loads(request.data))
        flag = purchaseService.modify(order)
    except:
        return ("forbidden", 403)

    result = json.dumps({
        "successful": flag
    })

    purchaseService.dispose()
    return (result, 200)

# 查找进货信息
@purchase.route("find", methods=["get"])
def find():
    purchaseService = PurchaseService()

    orderId = request.args.get("id")
    if orderId is None:
        return ("forbidden", 403)
    
    order = purchaseService.find(orderId)
    result = json.dumps(order.dicted())

    purchaseService.dispose()

    return (result, 200)

# 完成进货订单
@purchase.route("complete", methods=["get"])
def complete():
    purchaseService = PurchaseService()

    orderId = request.args.get("id")
    if orderId is None:
        return ("forbidden", 403)

    result = json.dumps({
        "successful": purchaseService.complete(orderId)
    })

    purchaseService.dispose()
    return (result, 200)