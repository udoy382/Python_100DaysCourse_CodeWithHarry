# Instance variables vs Class variables


class Employee:
    # This is a class variable ~
    companyName = "Apple"
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02

    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.companyName} is {self.raise_amount}")

emp1 = Employee("Udoy")
emp1.showDetails()
Employee.showDetails(emp1)

emp2 = Employee("Sara")
emp2.raise_amount = 0.3 # We can change this value ~
emp2.companyName = "Google"
# Employee.companyName = "Tesla"
emp2.showDetails()


print(Employee.companyName)