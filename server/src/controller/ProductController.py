from flask import request
from server.src.service.ProductService import *

class ProductController:

    def index(self):
        return "Hello ProductController"