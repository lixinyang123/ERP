import json, math, uuid
from flask import *
from service.ProductService import *
from util.Configuration import *

product = Blueprint('product',__name__)

pageSize = Configuration().get("PageSize")

# 产品列表
@product.route("index", methods=["get"])
def index():
    productService = ProductService()
    
    currentIndex = request.args.get("page")
    if currentIndex is None:
        return ("forbidden", 403)

    lastIndex = math.ceil(productService.count() / float(pageSize))

    products = productService.list(int(currentIndex) - 1, pageSize)

    result = []
    for product in products:
        result.append(product.dicted())

    result = json.dumps({
        "currentIndex": currentIndex,
        "lastIndex": lastIndex,
        "products": result
    })

    productService.dispose()
    return (result, 200)

# 新增产品
@product.route("add", methods=["post"])
def add():
    productService = ProductService()

    flag = False

    try:
        product = Product.dict2Obj(json.loads(request.data))
        product.id = str(uuid.uuid4())
        flag = productService.add(product)
    except: 
        return ("forbidden", 403)

    result = json.dumps({
        "successful": flag
    })

    productService.dispose()
    return (result, 200)

# 删除产品
@product.route("delete", methods=["get"])
def delete():
    productService = ProductService()

    productId = request.args.get("id")
    if productId is None:
        return ("forbidden", 403)

    result = json.dumps({
        "successful": productService.delete(productId)
    })

    productService.dispose()
    return (result, 200)

# 修改产品信息
@product.route("modify", methods=["post"])
def modify():
    productService = ProductService()

    flag = False

    try:
        product = Product.dict2Obj(json.loads(request.data))
        flag = productService.modify(product)
    except: 
        return ("forbidden", 403)

    result = json.dumps({
        "successful": flag
    })

    productService.dispose()
    return (result, 200)

# 查找指定产品
@product.route("find", methods=["get"])
def find():
    productService = ProductService()

    productId = request.args.get("id")
    if productId is None:
        return None
    
    product = productService.find(productId)
    result = json.dumps(product.dicted())

    productService.dispose()

    return (result, 200)
