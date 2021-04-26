from flask import request
from service.ProductService import *

class ProductController:

    def index(self):
        return "Hello ProductController"