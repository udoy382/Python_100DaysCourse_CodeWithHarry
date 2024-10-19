# Exercise 4 - Secret Code Language


import random

user = input("Enter your message: ")
number = ("1", "2", "3", "4", "5")

def secriteCode():
    # return user[::-1]
    y = user[::-1]
    return y + random.choice(number)

x = secriteCode()
print(x)