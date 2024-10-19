# Class Methods as Alternative Constructors in Python

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def formStr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))


e1 = Employee("Udoy", 10000)
print(e1.name)
print(e1.salary)


string = "Sara-10000"
# e2 = Employee(string.split("-")[0], string.split("-")[1])
e2 = Employee.formStr(string)
print(e2.name)
print(e2.salary)
