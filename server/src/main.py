from flask import Flask
# import os, json
# from server.src.service.SaleService import *

app = Flask(__name__)
app.secret_key = os.urandom(24)

# @app.before_request
# @app.after_request

@app.route('/')
def hello_world():

    # saleService = SaleService()
    # order = saleService.find("7d3de239-4810-4a2c-81d0-a76d6960c127")
    # saleService.dispose()

    # jsonStr = json.dumps(order.dicted())

    # return (jsonStr, 200, [("content-type", "application/json")])

    return "Hello World"