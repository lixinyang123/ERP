import json
from flask import request
from service.UserService import *
from util.Configuration import *

class UserController:

    def __init__(self):
        self.pageSize = Configuration().get("PageSize")
        self.userService = UserService()

    def index(self):
        pageIndex = int(request.args.get("page")) - 1

        if pageIndex is None:
            return None

        # lastIndex = self.userService.count()

        users = self.userService.list(pageIndex, self.pageSize)

        result = []
        for user in users:
            result.append(user.dicted())

        return json.dumps(result)