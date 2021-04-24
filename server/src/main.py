from flask import Flask
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def hello_world():
    return 'Hello, World!'