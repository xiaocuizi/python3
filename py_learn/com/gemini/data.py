# 标准的数据类型   数字、数组、String 、元组，

## 编程式为了解决实际问题(模拟)

## 思想   ：面向对象

print(4)

print(type(4))

a=4.3
a=True
a= 3+4j # a= 3+4i
print(type(a))

b=14;

print(bin(b))
print(oct(b))
print(hex(b)) #0-9  a-f 16进制
print("0x16",16)
str0="wrehowegoj sndnsfdsf"
print(str0[8])
str0 = '你好吗'
## 可以当做注释
str0 = """你好吗
sdadnasodnso dnao doa按到那
"""

print(str0)
print("---------------------")
str2 = "\"A\""
print(str2)
str3='"A"'
print(str3)

##-------------------
print("---------------------")
num1=5
num2=3
print("5+3",num1+num2)
##字符串格式化

"""
 字符串格式化，多行注释
"""
num4=5
num3=7
print("5+3={1},5+3={0}".format(num1+num2,num3+num4))
print("5+3=%i"%(num1+num2))
print("=====================================")
str4 = "sdlfssnfsnssgnsogn"
## 切片
print(str4[0:4])
print(str4[:5])
print(str4[1:])
print(str[:])# 所有
print(str4[:-2])#反向索引

print(str4*5)## 重复

print("---------------------")
str5 = " python "

print(str5.strip())
print(str5.rstrip())
print(str5.lstrip())
print("---------------------")
str6=r"c:\a\b\c.txt" ### 抑制转译  文件操作
print(str6)
print(str6)
print("---------------------")
num6 = "2"
num7=3
print(int(num6)+num7)
## print(str(num7)+num6)  ## 强制类型转换

num8=2 ## 隐士转换  2向下取
num9=3.1
print(num8+num9)
print("---------------------")

ls=[5,True,"34343"]
print(ls)
ls.append("找")
print(ls)
ls2=[1,2,3]
ls.extend(ls2)
print(ls)