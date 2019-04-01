import os

# 冰箱放食物Demo
"""
 数据结构
 {'海尔': ['苹果', '苹果', '苹果', '苹果', '鸡蛋', '鸡蛋', '鸡蛋'], 
 '美菱': ['香蕉', '香蕉', '香蕉'], 
'晶弘': ['西瓜', '西瓜', '西瓜', '西瓜']}
"""
class Refrigerator2:
    tup = {}
    order_list = {1: "查询食物", 2: "放入食物", 3: "取出食物"}
    path = r"./regitry.txt"

    def __init__(self):
        name = input("第一次使用冰箱，请输入名字：")
        # print("name=" + name)
        if len(name) == 0:
            # name = input("输入不能为空，请输入名字：")
            self.__init__()
            # os.system('pause')
        else:
            #  读取文件
            if not os.path.exists(self.path):
                file_path, file_name = os.path.split(self.path)
            else:
                file = open(self.path, mode="r", encoding="utf-8")
                for i in file:
                    # 字符串转换为字典
                    self.tup = eval(i)
        # 判断name在tup中有没有
        if name not in self.tup:
            self.tup.setdefault(name, [])
        order_no = input("欢迎使用{}冰箱，请输入对应序号进行操作，1.查询冰箱食物，2.放入食物，3.取出食物 ：".format(name))
        if len(order_no) == 0:
            print("请输入正确的序号.....")
        if order_no.isnumeric():
            order_no = int(order_no)
        else:
            if __name__ == '__main__':
                print("请输入正确的序号.....")
            return

        if order_no not in self.order_list:
            print("请输入正确的序号.....")
            # os.system('pause')
            return
        else:
            # 1 查询食物，2 放入食物  3 取出食物
            if order_no == 1:
                print("操作成功1！")
                print(self.tup[name])
            elif order_no == 2:
                food_name = input("请输入要放入的食品名称：")
                if len(name) <= 0:
                    food_name = input("请输入要放入的食品名称：")
                food_num = input("请输入要放入的食品数量：")
                if len(food_num) <= 0:
                    food_num = input("请输入要放入的食品数量：")
                # 取出list
                list_temp = self.tup[name]
                for i in range(0, int(food_num)):
                    if isinstance(list_temp, list):
                        list_temp.append(food_name)

                self.tup[name] = list_temp
                print("操作成功2！")
                print(list_temp)
                #  写入文件
                self.save()
            else:
                food_name = input("请输入要取出的食品名称：")
                if len(name) <= 0:
                    food_name = input("请输入要要取出的食品名称：")
                food_num = input("请输入要要取出的食品数量：")
                if len(food_num) <= 0:
                    food_num = input("请要取出要放入的食品数量：")
                # 取出list
                list_temp = self.tup[name]
                if isinstance(list_temp, list):
                    if list_temp.count(food_name) < int(food_num):
                        print("冰箱里面{}的数量不够了，赶紧添加吧~".format(food_name))
                        return
                    if list_temp.count(food_name) <= 0:
                        print("冰箱里面已经没有{}了，赶紧添加吧~".format(food_name))
                        return
                    for i in range(0, int(food_num)):
                        list_temp.remove(food_name)
                self.tup[name] = list_temp
                print("操作成功3！")
                print(list_temp)
                #  写入文件
                self.save()

    def save(self):
        try:
            file = open(self.path, mode="w", encoding="utf-8")
            file.write(str(self.tup))
            file.close()
        except IOError:
            print("请重新尝试...")
        finally:
            file.close()


# 初始化
b = Refrigerator2()
