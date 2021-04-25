from flask import Flask
from flask import redirect
from server.src.controller import *
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# @app.before_request
# @app.after_request

def controllers():
    return {
        "user": UserController(),
        "product": ProductController(),
        "purchase": PurchaseController(),
        "sale": SaleController()
    }

@app.route("/<controller>/<action>")
def action(controller: str, action: str):

    controllerName = controller.lower()
    actionName = action.lower()

    result = getattr(controllers()[controllerName], actionName)()
    return result