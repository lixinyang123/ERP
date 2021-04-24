from flask import Flask
import os, uuid
from datetime import datetime
from server.src.service.SaleService import *
from server.src.service.ProductService import *
from server.src.service.UserService import *

app = Flask(__name__)
app.secret_key = os.urandom(24)

# @app.before_request
# @app.after_request

@app.route('/')
def hello_world():

    # productService = ProductService()
    # product = productService.find("cfd09420-55f6-4925-9fa3-86528a1ebf74")
    # productService.dispose()

    # userService = UserService()
    # user = userService.find("684f1623-fbde-4b3d-8ef3-24c545b27523")
    # userService.dispose()

    # saleService = SaleService()

    # operations = list()
    # operations.append(ProductOperation(str(uuid.uuid4()), product, 10))
    # operations.append(ProductOperation(str(uuid.uuid4()), product, 20))
    # operations.append(ProductOperation(str(uuid.uuid4()), product, 30))

    # checkouts = list()
    # checkouts.append(CheckOut(str(uuid.uuid4()), str(datetime.now()), 100))

    # saleOrder = SaleOrder(str(uuid.uuid4()), str(datetime.now()), False, user, 100, operations, checkouts)
    # saleService.add(saleOrder)
    # saleService.dispose()


    # saleService = SaleService()
    # order = saleService.find("7d3de239-4810-4a2c-81d0-a76d6960c127")
    # saleService.dispose()


    return 'Hello, World!'