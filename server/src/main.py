from flask import Flask
from flask import redirect, Request, Response
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# @app.before_request
# @app.after_request

@app.route("/")
def root():
    return redirect("/home")

@app.route("/home")
def home():
    return redirect("/home/index")

@app.route("/<controller>/<action>")
def index(controller: str, action: str):
    return "Hello World"