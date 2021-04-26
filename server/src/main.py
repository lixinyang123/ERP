from flask import Flask
from flask import redirect
from controller import *
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

    if result is None:
        return ("forbidden", 403)

    return result, 200, {'Content-Type': 'application/json'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
