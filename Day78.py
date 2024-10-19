# Single Inheritance in Python


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")


class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark!")


d = Dog("Dog", "Doggerman")
d.make_sound()


a = Animal("Dog", "Dog")
a.make_sound()


# Quic Quiz: Implement a `Cat` class by using the animal class. Add some methods specific to cat :


class Cat(Animal):
    def __init__(self, name, x):
        Animal.__init__(self, name, species="Cat")
        self.x = x

    def Cat_sound(self):
        print("This is a cat sound!")


c = Cat("Cat", "This is an x value")
c.Cat_sound()