import json, math, uuid
from flask import *
from service.UserService import *
from util.Configuration import *

class UserController:

    def __init__(self):
        self.pageSize = Configuration().get("PageSize")
        self.userService = UserService()

    # 用户列表
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

    # 创建用户
    def add(self):

        if request.method != "POST":
            return None

        flag = False

        try:
            user = User.dict2Obj(json.loads(request.data))
            user.id = str(uuid.uuid4())
            flag = self.userService.add(user)
        except: {}

        return json.dumps({
            "successful": flag
        })

    # 删除用户
    def delete(self):

        userId = request.args.get("id")
        if userId is None:
            return None

        return json.dumps({
            "successful": self.userService.delete(userId)
        })

    # 修改用户信息
    def modify(self):

        if request.method != "POST":
            return None

        flag = False

        try:
            user = User.dict2Obj(json.loads(request.data))
            flag = self.userService.modify(user)
        except: {}

        return json.dumps({
            "successful": flag
        })

    # 查找指定用户
    def find(self):

        userId = request.args.get("id")
        if userId is None:
            return None
        
        user = self.userService.find(userId)

        return json.dumps(user.dicted())