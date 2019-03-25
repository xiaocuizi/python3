def adds(a, b):
    sum = a + b
    return sum
### 实现这个函数的时候，是否需要未知数的参与，要几个？
### 该能功能是否产生一个具体的值，如果需要，则需要return 语句
### 提高代码的重复使用

"""
 wo de object 
"""
c = adds(1, 2)
print(c)

print("----------------------")
def change(a):
    a=4
    return a
a=1
change(a)
print(a)

def fun(age,name,sex):
    print("age={},name={},sex={}".format(age,name,sex))

def fun1(name,sex,age=0):
    print("age={},name={},sex={}".format(age,name,sex))
fun(name="张三",age="34",sex="男")

print("----------------------》")
def fun2(a,*b):
    sums =0
    for i in b:
        sums +=i
        return a+sums

print(fun2(1,2,3,4,5,6,7))
print("----------------------")
# sum2 = lambda arg1,arg2:arg1+arg2
#
# print("--->"+str(sum2(2,2)))