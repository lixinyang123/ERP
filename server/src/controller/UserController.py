import json, math
from flask import request
from service.UserService import *
from util.Configuration import *

class UserController:

    def __init__(self):
        self.pageSize = Configuration().get("PageSize")
        self.userService = UserService()

    def index(self):

        currentIndex = request.args.get("page")
        if currentIndex is None:
            return None

        lastIndex = math.ceil(self.userService.count() / float(self.pageSize))

        users = self.userService.list(int(currentIndex) - 1, self.pageSize)

        result = []
        for user in users:
            result.append(user.dicted())

        return json.dumps({
            "currentIndex": currentIndex,
            "lastIndex": lastIndex,
            "users": result
        })