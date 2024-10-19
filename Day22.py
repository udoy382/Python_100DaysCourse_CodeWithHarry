# Introduction to List in Python


l = [3, 5, 6, 65, 346, 2299, 6, 3, "Udoy", True]
print(l)
print(type(l))

# print(l[0])
# print(l[1])
# print(l[2])
# print(l[3])
# print(l[4])

# print(l[-3]) # Negative index
# print(l[len(l)-3]) # Positive index
# print(l[5-3]) # Positive index
# print(l[2]) # Positive index

"""
if 7 in l:
    print("Yes")
else:
    print("No")


if "Udoy" in l:
    print("Yes")
else:
    print("No")


if "man" in "SaifurRahmanUdoy":
    print("Yes")
else:
    print("No")
"""

# print(l[:])
# print(l[1:-1])
# print(l[1:4])
# print(l[1:10:2])
# print(l[1:10:3])


# lst = [i for i in range(4)]
# lst = [i*i for i in range(4)]
lst = [i*i for i in range(10) if i % 2 == 0]
print(lst)
