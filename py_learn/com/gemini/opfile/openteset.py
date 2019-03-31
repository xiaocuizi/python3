import os
# file = open("test.txt","r",encoding="gbk")
# try:
#     file.write("hello,world,好python")
# except:
#     pass
# #str = file.read()
# print(str)
# #str = file.readline()
# print(str)
# str = file.readlines()
# print(str)
#
path =r"d://test/test.txt" # 抑制转译
file_path,file_name = os.path.split(path)
print(file_path)
print(file_name)

if not os.path.exists(file_path):
    os.makedirs(file_path)
file = open(path,"w")
file.write("Python是一门很好的语言")

file = open(path,"r")
for i in file:
    print(i)
