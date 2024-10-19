# super keyword in Python

"""
class ParentClass:
    def parent_method(self):
        print("This is the parent methods.")


class ChildClass(ParentClass):
    def child_method(self):
        print("This is the child method.")

    # def parent_method(self):
    #     print("Udoy")
    
        super().parent_method()


chiild_boject = ChildClass()
chiild_boject.child_method()
chiild_boject.parent_method()
"""


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang


rohan = Employee("Rohan Das", "324")
harry = Programmer("Harry", "3444", "Python")

print(harry.name)
print(harry.id)
print(harry.lang)