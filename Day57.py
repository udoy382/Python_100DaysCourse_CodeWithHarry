# Classes and Objects in Python


class Person:
    name = "Saifur Rahman Uody"
    occupation = "Ethical Hacker"
    networth = 10000

    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person()
# Change object ~
# a.name = "Hamim"
# a.occupation = "Teacher"


b = Person()
# Created a new object ~
# b.name = "Dipty Shopnil Sara"
# b.occupation = "Robotic Enginner"


# It is print default value in class
c = Person()

print(a.name, a.occupation)

# Call function ~
a.info()
b.info()
c.info()