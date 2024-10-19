# Map, Filter and Reduce in Python


# MAP ~
"""
def cube(x):
    return x*x*x

print(cube(2))

l = [1, 2, 4, 6, 4, 3]


# newl = []
# for item in l:
#     newl.append(cube(item))


# We can also pass lambda funciton there ~
newl = list(map(cube, l))

# newl = (lambda x: x*x*x, l)
print(newl)
"""
# _____________________________
# FILTER ~
"""
def filter_function(a):
    return a>4

newnewl = list(filter(filter_function, l))
print(newnewl)
"""
# _____________________________

# REDUCE ~

# We can first of all import reduce function ~
"""
from functools import reduce

numbers = [1, 2, 3, 4, 5]

sum = reduce(lambda x, y: x + y, numbers)

print(sum)
"""