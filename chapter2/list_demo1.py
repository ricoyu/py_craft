lst = [1,2,3,4]
print("原始列表: ", lst)

del lst[0]
print("删除第一个元素: ", lst)

lst = [1,2,3,4]
lst.pop(0)
print("删除第一个元素: ", lst)

lst = [1,2,3,4]
lst = lst[1:]
print("切片后的列表: ", lst)