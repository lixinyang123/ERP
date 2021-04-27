import json, math, uuid
from flask import *
from service.UserService import *
from util.Configuration import *

class UserController:

    def __init__(self):
        self.pageSize = Configuration().get("PageSize")

    # 用户列表
    def index(self):
        userService = UserService()

        currentIndex = request.args.get("page")
        if currentIndex is None:
            return None

        lastIndex = math.ceil(userService.count() / float(self.pageSize))

        users = userService.list(int(currentIndex) - 1, self.pageSize)

        result = []
        for user in users:
            result.append(user.dicted())
        
        result = json.dumps({
            "currentIndex": currentIndex,
            "lastIndex": lastIndex,
            "users": result
        })

        userService.dispose()
        return result

    # 创建用户
    def add(self):

        userService = UserService()

        if request.method != "POST":
            return None

        flag = False

        try:
            user = User.dict2Obj(json.loads(request.data))
            user.id = str(uuid.uuid4())
            flag = userService.add(user)
        except: {}

        result = json.dumps({
            "successful": flag
        })

        userService.dispose()
        return result

    # 删除用户
    def delete(self):

        userService = UserService()

        userId = request.args.get("id")
        if userId is None:
            return None

        result = json.dumps({
            "successful": userService.delete(userId)
        })

        userService.dispose()
        return result

    # 修改用户信息
    def modify(self):

        userService = UserService()

        if request.method != "POST":
            return None

        flag = False

        try:
            user = User.dict2Obj(json.loads(request.data))
            flag = userService.modify(user)
        except: {}

        result = json.dumps({
            "successful": flag
        })

        userService.dispose()
        return result

    # 查找指定用户
    def find(self):

        userService = UserService()

        userId = request.args.get("id")
        if userId is None:
            return None
        
        user = userService.find(userId)

        userService.dispose()

        return json.dumps(user.dicted())