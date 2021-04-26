from flask import request
from service.SaleService import *

class SaleController:

    def index(self, request):
        return "Hello SaleController"