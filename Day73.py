# Magic/Dunder Methods in Python


class Employee:
    def __init__(self, name):
        self.name = name

    # name = "Udoy"

    # This is a magic or dunder methods
    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i
    
    def __str__(self):
        return f"The name of the employee is: str {self.name}"


    def __repr__(self):
        return f"The name of the employee is: repr {self.name}"


e = Employee("Sara")
print(e.name)
print(len(e))
