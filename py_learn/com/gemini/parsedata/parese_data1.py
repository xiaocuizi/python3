import json

count = 1
data = open("data1.json", encoding="utf-8")
str_json = json.load(data)
flag = False
lock_flag = False
while count <= 3:
    if count == 3:
        break
    user_name = input("请输入用户名：")
    password = input("请输入密码：")
    for user in str_json:
        if user_name == user["username"] and password == user["password"]:
            if not user["lock"]:
                flag = True
            else:
                lock_flag = False
                break
        if flag:
            print("登陆成功")
            break
        else:
            print("账号或者密码错误")
        count = count + 1
