"""
  切片：numpy
"""
import numpy as np

list = [1, 2, 3, 4, 5]
print(list)
a = np.arange(10)  # 从0-9
print(a)
s = slice(2, 7, 2)
print(a[s])

b = a[2:7:2]
print(b)

b = a[5]
print(b)
print("----------------")

print(a[2:])  # 从数组下标开始到结尾所有数字

print(a[2:5])
print("----------------")
c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(c)
print(c.size)
print(c.ndim)
print(c.shape)
print("---zeros------ones-------")
d = np.zeros((2, 3, 4), dtype=np.int8)  # 必须给出形状
print(d)

print(d.shape)
e = np.ones((2, 3), np.int8)  # 零矩阵，转置  初始化的作用
print(e)
print("-------索引---------")
f = np.array([[1, 2], [3, 4], [5, 6]])
print(f.shape)
print(f[1][0])
print(f[1, 0])

g = np.array([[[1, 2], [3, 4], [5, 6]]])

print(g)
print(g.ndim)
print("-------ndarry切片---------")
h = np.array([1, 2, 3, 4, 5])
print(h[1:4])
print(h[:3])
print(h[1:])
print(h[:])
print(h[0:4:2])

print("-------ndarry 二维切片---------")

i = np.array([[1, 2], [3, 4], [5, 6]])

print(i[:2])
print(i[:2, :1])  # TODO 进入下一个维度进行切片
print(i[:2][:1])  # TODO 在同级别维度切片
# TODO 切对象是二维的，那么切出来的依然是二维，维度不会降低
# TODO 切片跟数组索引不同
i[:2, :1] = 0
print(i)
print("-------ndarry 三维切片---------")

# TODO 重新定义数组维度
j = np.arange(24).reshape(2, 3, 4)
print(j)
print("-------ndarry 四维切片---------")

k = np.arange(24).reshape(1, 2, 3, 4)
print(k)
print(k.ndim)
print(k[:2, :2, :1, :1])
