# 定义一个列表
my_list = [10, 20, 30, 40, 50]

# 尝试查找不存在的元素 60
try:
    index = my_list.index(60)
    print(f"元素 60 的索引为: {index}")
except ValueError:
    print("列表中不存在元素 60")

    index = my_list.index(50)
    print(f"元素 50 的索引为: {index}")
