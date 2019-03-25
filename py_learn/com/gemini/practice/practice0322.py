"""
1、猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
 以后每天早上都吃了前一天剩下的一半零一个。
 到第10天早上想再吃时，见只剩下一个桃子了。
 求第一天共摘了多少。
"""

""" 2、有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。"""

""" 3、求1+2!+3!+...+20!的和。"""
## 1! = 1×1 = 1            0 -->1
##2! = 2×1 = 2             1-->1 ×2
##3! = 3×2×1 = 6          2-->1 ×2 x3
##4! = 4×3×2×1 = 24      3-->1 ×2 ×3 ×4
##5! = 5×4×3×2×1 = 120  4-->1 ×2 ×3 ×4 ×5
def fun2(n):
    if (n == 1):
        return n
    else:
        return n * fun2(n - 1)

sums = 0
for i in range(1, 21):
    sums += fun2(i)

print("sums={}".format(sums))
""" 4、删除列表中的重复元素"""
list = [3, 4, 5, 6, 7, 8, 6]
setTemp = set(list)
print("setTemp={}".format(setTemp))
""" 5、定义函数实现字符串反转 例如：输入str="string"输出'gnirts'"""


def change(str):
    return str[::-1]


str = "string"
print("change string={}".format(change(str)))
""" 6、一行代码实现对列表a中的偶数位置的元素进行加3后求和"""
a = [1, 2, 4, 5]  # 1+3  4+3
c = 0
for i in range(len(a)):
    b = i % 2
    if (b == 0):
        c += (a[i] + 3)
print("sum={}".format(c))

""" 7、List = [-2, 1, 3, -6]，如何实现以绝对值大小从小到大将 List 中内容排序"""
List = [-2, 1, 3, -6]
List_result = []
for j in List:
    List_result.append(abs(j))

## 排序
List_result.sort()
print("List_result={}".format(List_result))
""" 8、合并两个list"""
a_list = [2, 3, 4, 5, 6]
b_list = [7, 8, 9]
a_list.extend(b_list)
print("a_list={}".format(a_list))

""" 9、什么是lambda函数？它有什么好处？另外python在函数编程方面提供了些什么函数和语法？"""
## Lambda函数，是一个匿名函数,简洁明了
## 绝对值 abs()/ 求和sum()./格式化 str.format

""" 10、详细说说tuple、list、dict的用法，它们的特点"""
## tuple 元组，例如  a=(1,2,3,4) 不可变
## list 列表，例如  b=[3,4,5,6,90] 可变，增删改查
## dic 字典  ，例如： c={"key":1,"key2":2,"key3":"helloworld"}

""" 11、list 对象 alist [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]， 请按 alist 中元素的age 由大到小排序；"""
print("===================================================================")
alist = [{'name': 'a', 'age': 20}, {'name': 'b', 'age': 30}, {'name': 'c', 'age': 25}]
blist = []
for k in range(len(alist)):
    blist.append(alist[k]['age'])

clist = []
blist.sort()
# for k in range(len(alist)):
#     for h in range(len(blist)):
#         if (alist[k]['age'] == blist[h]):
#             clist.append(alist[k])
for h in range(len(blist)):
    for k in range(len(alist)):
        if (alist[k]['age'] == blist[h]):
            clist.append(alist[k])

print("blist={}".format(blist))
print("clist={}".format(clist))
""" 12、将字符串："k:1|k1:2|k2:3|k3:4"，处理成 python 字典：{'k':'1', 'k1':'2', 'k2':'3','k3':'4' }"""

str_a = "k:1|k1:2|k2:3|k3:4"
str_list = str_a.split('|')
dict_total = {}
for j in range(len(str_list)):
    dict_ele_temp = str_list[j].split(":")
    key = dict_ele_temp[0]
    value = dict_ele_temp[1]
    dict_total[key] = value

print("dict_total={}".format(dict_total))

""" 13、用代码体现斐波那契数列"""
## 斐波那契数列指的是这样一个数列 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
# 233，377，610，987，1597，2584，4181，6765，10946，17711，28657，46368........
# F[n]=F[n-1]+F[n-2]    (n>=3,F[1]=1,F[2]=1)

a=0
b=1
while b < 1000:
    print(b)
    a, b = b, a+b
