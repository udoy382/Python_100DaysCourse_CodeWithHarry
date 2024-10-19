# Function Arguments in Python 

"""
def average(a=9, b=1):
    print("The average is ", (a + b)/2)

# average(4, 6)
# average()
# average(1, 5)
# average(5)
average(b=9)
"""


"""
def name(fname, mname = "Rahman", lname = "Udoy"):
    print("Hello!", fname, mname, lname)

name("Saifur", "jackson", "Justin")
"""

"""
def average(*numbers):
    # print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is: ", sum / len(numbers))

average(5, 6, 7, 1)
"""

# __________________

"""
def name(**name):
    print(type(name))
    print("Hello!", name["fname"], name["mname"], name["lname"])

name(mname="Rahman", lname="Udoy", fname="Saifur")
"""

def average(*numbers):
    # print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)

c = average(5, 6, 7, 1)
print(c)