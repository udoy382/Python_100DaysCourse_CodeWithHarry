# Finally keyword in Python

"""
try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("Some error occurred.")

finally:
    print("I am always excuted.")
"""


def func1():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occurred.")
        return 0

    finally:
        print("I am always excuted.")

x = func1()
print(x)