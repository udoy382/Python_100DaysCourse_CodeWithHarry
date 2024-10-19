# Class Methods in Python


class Employee:
    company = "Google"
    def show(self):
        print(f"The name of {self.name} and company is {self.company}")

    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany


e1 = Employee()
e1.name = "Udoy"
e1.show()

e1.changeCompany("Tesla")
e1.show()

print(Employee.company)