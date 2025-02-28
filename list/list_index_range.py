# 定义一个列表
my_list = [10, 20, 30, 40, 50, 30, 60]

# 在索引 3 到 6 之间查找元素 30
try:
    index = my_list.index(30, 3, 6)
    print(f"元素 30 的索引为: {index}") # 输出: 元素 30 的索引为: 5
except ValueError:
    print("列表中不存在索引 3 到 6 之间元素 30")
