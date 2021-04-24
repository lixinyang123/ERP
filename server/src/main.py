from flask import Flask
import os,uuid
from datetime import datetime
from server.src.service.ProductService import *
from server.src.service.PurchaseService import *
from server.src.model.Product import *

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def hello_world():

    productService = ProductService()
    product = productService.find("03618fbb-04fb-4449-a0b1-96f0c4a11891")
    productService.dispose()

    purchaseService = PurchaseService()

    # operations = list()
    # operations.append(ProductOperation(str(uuid.uuid4()), product, 10))
    # order = PurchaseOrder(str(uuid.uuid4()), str(datetime.now()), False, operations)
    # purchaseService.add(order)

    # operations = list()
    # operations.append(ProductOperation(str(uuid.uuid4()), product, 1000))
    # order = PurchaseOrder("80feda52-910c-4b63-9501-2414dc0c64c0", str(datetime.now()), True, operations)
    # purchaseService.modify(order)

    order = purchaseService.find("80feda52-910c-4b63-9501-2414dc0c64c0")

    # purchaseService.delete("80feda52-910c-4b63-9501-2414dc0c64c0")

    return 'Hello, World!'