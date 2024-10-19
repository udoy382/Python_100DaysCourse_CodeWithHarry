# Inheritance in Python


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")


class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")


class Hacker(Programmer):
    def heyHacker(self):
        print("Hey! I am a Ethical Hacker")


# e = Employee("Rohan Das", 400)
# e.showDetails()

# ee = Employee("Harry", 4100)
# ee.showDetails()

# eee = Programmer("Udoy", 436)
# eee.showLanguage()
# eee.showDetails()


eeee = Hacker("Mariyam", 4949)
eeee.heyHacker()
eeee.showDetails()
eeee.showLanguage()