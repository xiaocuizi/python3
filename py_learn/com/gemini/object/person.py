class person:
    def cry(self):
        print("大哭")

    def __init__(self):  ## 构造方法（专有方法） 当实例化对象的时候，就会调用
        self.cry()


p1 = person()


class person2:
    def __init__(self, sex, name):
        self.sex = sex  ## 给person实例对象顶一个实例变量sex,然后赋值为sex
        self.name = name
    def speck(self):
        print(self.name,self.sex)



p2 = person2(sex="女",name="张三妹")
p2.speck()