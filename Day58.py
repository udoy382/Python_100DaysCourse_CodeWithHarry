# Constructors in Python


class Person:
    def __init__(self, name, occ):
        self.name = name
        self.occ = occ


    def info(self):
        print(f"{self.name} is a {self.occ}")


a = Person("Udoy", "Developer")
b = Person("Sara", "Enginner")
c = Person(1, 2)


a.info()
b.info()
c.info()