import random

# 快速排序
def fast_sort(array):
    array_size = len(array)
    if (array_size < 2):
        return array
    else:
        # 选取基数
        base = array[random.randint(0, array_size - 1)]
        left = []
        right = []
        for i in array[0:]:
            if (i < base):
                left.append(i)
            elif (i > base):
                right.append(i)
        # 递归 合并数据
        return fast_sort(left) + [base] + fast_sort(right)


bytearray = [45, 53, 33, 27, 90, 12, 71, 84, 6]
print(fast_sort(bytearray))

