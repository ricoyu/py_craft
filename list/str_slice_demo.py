text = "Hello, World!"

# 基本切片：从头到尾
print(text[:]) # prints: Hello, World!

# 指定开始和结束位置
print(text[0:5]) # prints: Hello

# 从开头到指定位置
print(text[:7]) # prints: Hello,

# 从指定位置到结尾
print(text[7:]) # prints: World!

# 使用步长 (step)
print(text[::2]) # prints: Hlo ol!