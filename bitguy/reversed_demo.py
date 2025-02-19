my_list=[1,2,3,4,5]
reversed_list = reversed(my_list)
print(reversed_list) # <list_reverseiterator object at 0x000001E0B0EB0E80>
for i in reversed_list:
    print(i)


my_str = 'hello'
reversed_str = reversed(my_str)
print(reversed_str)     # <list_reverseiterator object at 0x000001E0B0EB0E80>
print(''.join(reversed_str)) # olleh