# Raising custom errors in Python

"""
a = int(input("Enter any value between 5 and 9: "))

if (a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")
"""


# Quick Quize

user = input("Enter any value between 10 and 20: ")

if (int(user) < 10 or int(user) < 20):
    print("You are enter correct number.")
elif user == "quit":
    print("it is quit")
else:
    raise ValueError("ERROR! value should be between 10 and 20")
