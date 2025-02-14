# 定义一个列表
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

slice_1 = numbers[2:5] # 输出：[2, 3, 4]
print(slice_1)

# 提取从开始到索引 4（不包括 4）的元素
slice_2 = numbers[:4]
print(slice_2)

# 提取从索引 6 到末尾的元素
slice_3 = numbers[6:]
print(slice_3)

# 提取整个列表
slice_4 = numbers[:]
print(slice_4)