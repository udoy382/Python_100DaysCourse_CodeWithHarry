# Access Modifiers in Python

# Types of access specifiers~
# 1. Public access modifiers
# 2. Private access modifiers
# 3. Protected access modifiers


# Public~
"""
class Employee:
    def __init__(self):
        self.name = "Udoy"

a = Employee()
print(a.name)
"""

# Private~
"""
class Employee:
    def __init__(self):
        self.__name = "Udoy"

a = Employee()
# print(a.__name) # Cannot be accessed directly because this is private.

print(a._Employee__name) # Can be accessed indirectly
# print(a.__dir__())
"""

# Protected~


class Student:
    def __init__(self):
        self._name = "Sara"

    def _funName(self):  # protected method
        return "Dipty Shopnil Sara"


class Subject(Student):  # inherited class
    pass


obj = Student()
obj1 = Subject()
print(dir(obj))

# Calling by object of `Student` class
print(obj._name)
print(obj._funName())

# Calling by object of `Subject` class
print(obj1._name)
print(obj1._funName())
