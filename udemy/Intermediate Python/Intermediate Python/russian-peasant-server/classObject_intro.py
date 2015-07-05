class BaseClass:
    def c(self):
        return 3 # 3 is value given to c in BaseClass. BaseClass can be passed to new classes to inherit values from.

class TestClass(BaseClass):
    def __init__(self):
        self.b = 2 # 2 is default value of b when object is initiated
        self._d = 4 # variables with '_' are private. Not used outside of scope of function etc. This is a convention
    def add(self):
        pass
    def plusOne(self):
        c = self.c
        return self.add()+1

c = TestClass()
c.a = 1 # adds paramater 'a' to object (not defined in TestClass)

print(c.a)
print(c.b)
print(c.c()) # 'c' is inherited from BaseClass and in BaseClass 'c' is defined as function and therefore needs c()
print(c._d) # this is possible but bad form : _d is meant to be private to class definition.