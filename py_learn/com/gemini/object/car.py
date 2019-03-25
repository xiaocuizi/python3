"""
 通过类来描述对象
"""
class car:
    color="红色"  ## 类变量，被类对所共享
    name="宝马"
    def run(self):
        print("车跑起来了了。。")


c1 = car()
c2 = car()

print(c1.color) ## 实例对象
c2.run()


print(car.color) ## 类对象，智能引用属性，不能使用功能，


car.run(c1)
