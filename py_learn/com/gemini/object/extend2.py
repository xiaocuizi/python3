class A:
    a = 1

    def fun(self):
        print("A")


class B:
    a = 2

    def fun(self):
        print("B")


class C(A, B):  ## 有先后顺序，访问变量的，排名第一个的优先使用
    a3 = 3

    def fun3(self):
        print("C")


c = C()
print(c.a3)
