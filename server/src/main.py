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
        "home": HomeController(),
        "user": UserController()
    }

@app.route("/")
def root():
    return redirect("/home")

@app.route("/<controller>")
def controller(controller: str):
    return redirect("/" + controller + "/index")

@app.route("/<controller>/<action>")
def action(controller: str, action: str):

    controllerName = controller.lower()
    actionName = action.lower()

    result = getattr(controllers()[controllerName], actionName)()
    return result