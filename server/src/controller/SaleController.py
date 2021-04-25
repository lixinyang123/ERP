from flask import request
from server.src.service.SaleService import *

class SaleController:

    def index(self):
        return "Hello ProductController"