from com.gemini.practice.extends.Animal import Animal


# 猫
class Cat(Animal):

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def rlclover(self):
        print("卖萌。。。。。")


cat = Cat("折耳", 2)

print(cat.eat())
