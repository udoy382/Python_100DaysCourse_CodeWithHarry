# Enumerate Function in Python


marks = [12, 56, 45, 47, 34, 65, 45, 4, 1]

"""
index = 0
for mark in marks:
    print(mark)
    if (index == 3):
        print("Harry, Awesome!")
    index += 1
"""


# for index, mark in enumerate(marks, start=1):
for index, mark in enumerate(marks):
    print(mark)
    if (index == 3):
        print("Harry, Awesome!")