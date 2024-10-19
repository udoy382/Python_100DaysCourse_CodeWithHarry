# break and continue in python


"""
for i in range(15):
    if (i == 10):
        break
    print("5 X ", i+1, " = ", 5 * (i+1))

print("Loop ko chodkar nikal gaya")
"""


"""
for i in range(15):
    if (i == 10):
        print("Skip the iteration")
        continue
    print("5 X ", i+1, " = ", 5 * (i+1))
"""

i = 0
while True:
    print(i)
    i += 1
    if (i%100 == 0):
        break