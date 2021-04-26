from flask import request
from service.UserService import *

class UserController:

    def __init__(self):
        self.userService = UserService()

    def index(self):
        return "Hello UserController"