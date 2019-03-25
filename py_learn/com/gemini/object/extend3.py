class student(object):
    def __init__(self,name,sex,age):
        self.name= name
        self.sex = sex
        self.age =age
    def __str__(self):  ## 对专有方法的重新，叫运算符重载
        return "姓名：{0}，性别：{1},年龄:{2}".format(self.name,self.sex,self.age)


st = student("张三","男",18)
print(st)