# Set Methods in Python


s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
info = {"Carla", 19, False, 5.9}


# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.symmetric_difference(s2)) # This is show umcommon set list
# print(s1.difference(s2))
# print(s1.issuperset(s2))
# print(s1.issuperset(s2))



# s1.update(s2)
# print(s1, s2)


# s1.add(44)
# print(s1)


# s1.remove(5)
# print(s1)


# `remove` show an error if items doesn't exist in sets but `discard` not show an error.
# s1.discard(8)
# print(s1)


# s1.pop()
# print(s1)


# del s2
# print(s2)


if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent")