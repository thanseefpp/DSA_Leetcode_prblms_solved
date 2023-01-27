


class base_1:
    def __init__(self, a):
        self.a = a
        self.c = 5 * a

class base_2:
    def __init__(self, b):
        super(base_2, self).__init__()
        self.b = b
        self.d = 10 * b

class Derived(base_1, base_2):
    def __init__(self, a, b):
        base_1.__init__(self,a=a)
        base_2.__init__(self,b=b)

# class Base:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

# class Derived(Base):
#     def __init__(self, a, b):
#         super().__init__(a, b)
#         self.c = a + b
#         self.d = a * b
        
# creating a derived class object
obj = Derived(a = 2,b = 3)

# printing the new variables
print(obj.c)
print(obj.d)

