# Walrus Operator in Python


a = True
# print(a)

# print(a=False) # It's shows error cause python doesn't allow to change like this
# print(a:=False) # It's print `False` cause this is walrus operator to change like this

"""
numbers = [1, 2, 3, 4, 5]
while (n := len(numbers)) > 0:
    print(numbers.pop())
"""

"""
happy = False
print(happy)
print(happy := True)
"""

"""
foods = list()
while True:
    food = input("What food do you like? : ")
    if food == "quit":
        break
    foods.append(food)
"""

foods = list()
while (food := input("What food do you like? : ")) != "quit":
    foods.append(food)
