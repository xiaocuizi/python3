def fun():
    a = 3  ## 闭包外的函数变量
    print(a)

    def inside():
        b = 4  ## 局部变量


x = int(10)  ## 内置作用域，通过系统函数创建的数据集、、
y = 2  ## 全局变量


a=4
def fun():
    global  a  ### 声明加权限 ，就可以修改，否则引用函数外的变量是只读的，不得修改
    a=5
    print(a)
fun()
print(a)