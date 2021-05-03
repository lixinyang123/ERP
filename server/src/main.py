from flask import *
from controller import *
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(product, url_prefix='/product')
app.register_blueprint(purchase, url_prefix='/purchase')
app.register_blueprint(sale, url_prefix='/sale')

# @app.before_request

@app.after_request
def handlerResponse(response):
    response.content_type = "application/json"
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
