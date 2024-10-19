# read(), readlines() and other methods in Python

"""
with open("my_file.txt", "r") as f:
    i = 0
    while True:
        i+=1
        line = f.readline()
        if not line:
            # print(line, type(line))
            break
        m1 = int(line.split(",")[0])
        m2 = int(line.split(",")[1])
        m3 = int(line.split(",")[2])
        print(f"Marks of students {i} in maths is: {m1 * 2}")
        print(f"Marks of students {i} in english is: {m2 * 2}")
        print(f"Marks of students {i} in science is: {m3 * 2}")
        print(line)

        print(line)
"""

# ___________________


with open("myfile.txt", "w") as f:
    lines = ['line 1\n', 'line 2\n', 'line 3\n']
    f.writelines(lines)