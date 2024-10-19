# Function in Python

a = 9
b = 84
c = 8
d = 7

x = 9
y = 10

"""
gmean =( a * b)/(a + b)
print(gmean)

gmean = (c * d)/(c + d)
print(gmean)
"""

# _________________________

"""
def calculateGmean(x, y):
    mean = (x * y)/(x + y)
    print(mean)


# calculateGmean(10, 20)
calculateGmean(x, y)
"""

# ___________________________

"""
if (a > b):
    print("First number is greater.")
elif (a == b):
    print("First and second number are equal.")
else:
    print("Second number is greater")
"""

def isGreater(a, b):
    if (a > b):
        print("First number is greater.")
    elif (a == b):
        print("First and second number are equal.")
    else:
        print("Second number is greater")

isGreater(a, b)


def isLesser(a, b):
    pass