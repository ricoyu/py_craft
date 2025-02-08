names = ['俞雪华', '三少爷']
print(repr(names))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return 'Person(%s, %s)' % (self.name, self.age)

p = Person('俞雪华', 18)
print(repr(p)) # Person(俞雪华, 18)

s = "hello\nworld"
print(str(s))
print(repr(s))