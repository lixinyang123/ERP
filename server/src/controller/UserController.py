import json, math, uuid
from flask import *
from service.UserService import *
from util.Configuration import *

user = Blueprint('user',__name__)

pageSize = Configuration().get("PageSize")

# 用户列表
@user.route("index", methods=["get"])
def index():
    userService = UserService()

    currentIndex = request.args.get("page")
    if currentIndex is None:
        return ("forbidden", 403)

    lastIndex = math.ceil(userService.count() / float(pageSize))

    users = userService.list(int(currentIndex) - 1, pageSize)

    result = []
    for user in users:
        result.append(user.dicted())
    
    result = json.dumps({
        "currentIndex": currentIndex,
        "lastIndex": lastIndex,
        "users": result
    })

    userService.dispose()
    return (result, 200)

# 创建用户
@user.route("add", methods=["post"])
def add():

    userService = UserService()

    flag = False

    try:
        user = User.dict2Obj(json.loads(request.data))
        user.id = str(uuid.uuid4())
        flag = userService.add(user)
    except:
        return ("forbidden", 403)

    result = json.dumps({
        "successful": flag
    })

    userService.dispose()
    return (result, 200)

# 删除用户
@user.route("delete", methods=["get"])
def delete():

    userService = UserService()

    userId = request.args.get("id")
    if userId is None:
        return ("forbidden", 403)

    result = json.dumps({
        "successful": userService.delete(userId)
    })

    userService.dispose()
    return (result, 200)

# 修改用户信息
@user.route("modify", methods=["post"])
def modify():

    userService = UserService()

    flag = False

    try:
        user = User.dict2Obj(json.loads(request.data))
        flag = userService.modify(user)
    except: 
        return ("forbidden", 403)

    result = json.dumps({
        "successful": flag
    })

    userService.dispose()
    return (result, 200)

# 查找指定用户
@user.route("find", methods=["get"])
def find():

    userService = UserService()

    userId = request.args.get("id")
    if userId is None:
        return ("forbidden", 403)
    
    user = userService.find(userId)
    result = json.dumps(user.dicted())

    userService.dispose()

    return (result, 200)
