from flask import request
from server.src.service.PurchaseService import *

class PurchaseController:

    def index(self):
        return "Hello ProductController"