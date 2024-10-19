# Lambda function in Python


# This is an normal function ~
"""
def double(x):
    return x * 2

print(double(5))
"""


# This is an lambda funciton ~
double = lambda x : x * 2
print(double(5))


cube = lambda x : x*x*x
print(cube(5))


avg = lambda x, y : (x + y) / 2
print(avg(3, 5))


# We can also pass function ~
def appl(fx, value):
    return 6 + fx(value)

print(appl(cube, 2))