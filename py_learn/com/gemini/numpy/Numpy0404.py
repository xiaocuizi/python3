import numpy as np

# # numpy的boolean行索引
#
# x =np.array([[1,2],[3,4]])
# print(x[0,1])
#
# # 花式索引：可以使用一个整形数组
# x = np.arange(24).reshape(2,3,4)
# print(x)
#
# # 数组的转置
# print("数组的转置")
# k = np.arange(12).reshape(3,4)
# print(k)
#
# print(k.T)
#
# # 点乘 （内积）  列和行一样  A行 = B列
#
#
# # 高位数组的轴对象  维度   向右旋转90度
# x = np.arange(24).reshape(2,3,4)  # 0,1,2 轴
#
# k = k.transpose(1,0,2)
# print(k.shape)
#
# k = k.swapaxes(0,2)  # 只是调整两个轴
#
#
# # numpy的基本统计方法
#
# k.mean()
#
# k.mean(axis=0)  # 对列求均值， 1= 对每一行求均值
#
#
# # 数组求和
# print(k.sum())
# print(k.sum(axis=0))
#
#
# print(",排序")
# x =  np.array([6,1,3],[1,5,2])
#
# x.sort()
# print(x)

# ndarray的存储

x = np.array([[1, 6, 2], [6, 1, 3], [1, 5, 2]])
np.save("file", x)

y = np.load("file.npy")
print(y)

# 随机数
x = np.random.randint(0, 2, size=10000)

print((x > 2).sum())

print("where 函数")

cond = np.array([True, False, False, False])
u = np.where(cond, -2, 2) # 相当于三木运算符

print(u)
