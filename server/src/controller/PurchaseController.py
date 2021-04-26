from flask import request
from service.PurchaseService import *

class PurchaseController:

    def index(self):
        return "Hello ProductController"