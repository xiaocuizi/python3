import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # 三维空间

# 实时画图

# ax = []
# ay = []
# plt.ion()
# for i in range(100):
#     ax.append(i)
#     ay.append(i ** 2)
#     plt.clf()
#     plt.plot(ax, ay)
#     plt.pause(1)
# plt.ioff()
# plt.show()

# 正太分步，散点图

# n = 1024
#
# x = np.random.normal(0, 1, n)
# y = np.random.normal(0, 1, n)
# color = np.arctan2(y,x)
# plt.scatter(x, y, c=color, alpha=0.5)
# plt.show()
# # 坐标轴
#
# plt.xlim(-1.5,1.5)
# plt.xlim(-1.5,1.5)
# # 不显示坐标轴
# plt.xticks(())
# plt.yticks(())
#
# plt.show()

x = np.random.normal(0, 1, 100)
y = np.random.normal(0, 1, 100)
z = np.random.normal(0, 1, 100)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x, y, z)
plt.show()
