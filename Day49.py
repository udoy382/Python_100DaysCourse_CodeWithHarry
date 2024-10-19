# File I/O in Python 


"""
a = Append
r = Read
w = Write
t = Text
b = Binary

[a, r, w, rt, rb, wt, wb]
"""


"""
# f = open("my_file.txt", "r")
# f = open("my_file.txt", "w")
f = open("my_file.txt", "a")

f.write("This is Saifur Rahman Udoy")

# text = f.read()
# print(text)

# print(f)
f.close()
"""

# Best way to file i/o 

with open("my_file.txt", "a") as f:
    f.write("hello there ")