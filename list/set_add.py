my_set={1,2,3,4,5}
my_set.add(5)
print(my_set) # {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set) # {1, 2, 3, 4, 5, 6}

another_set={1,2,3}
another_set.update([4,5,6])
print(another_set) # {1, 2, 3, 4, 5, 6}