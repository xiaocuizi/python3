import numpy as np

# print(np.__version__)

print("生成列表一维数组")

data = [1, 2, 3, 4, 5, 6]

x = np.array(data)
print(x.dtype)  # 数值类型
print(x.shape)
print(x.ndim)  # 维度

print("生成列表二维维数组")
data = [[1, 2], [3, 4], [5, 6]]

x = np.array(data)
print(x)
print(x.ndim)  # 维度
print(x.shape)  # TODO 从外往内数（形状）核心
print(x.size)  # 从外往内数（形状）
print(x.dtype)  # 数值类型

print("使用zeros/ons生成列表二维维数组")

x = np.zeros((2, 3, 4))  # 必须给形状
print(x)

print(x.dtype)
print(x.ndim)
print(x.shape)

x = np.ones((2, 3), dtype=np.int8)
print(x.shape)

print("使用arange生成连续的元素")
print(np.arange(6))

print("数组复制")
x = np.array([1, 2, 3, 4, 5], dtype=np.float32)

y = x.astype(dtype=np.int8)
print(y)

print("字符串转数字")
x = np.array(['1', '2', '3'], dtype=np.string_)
y = x.astype(np.int8)
print(y)
print("使用其他数组的数据类型作为参数")
x = np.array([1, 2, 3, 4], dtype=np.float64)
y = np.array(3, dtype=np.int32)
print(y.astype(x.dtype))

x = np.array([1, 2, 3])
print(x * 2)
print(x > 2)

y = np.array([2, 3, 4])
print(x * y)

print("基本索引")
x = np.array([[1, 2], [3, 4], [5, 6]])
