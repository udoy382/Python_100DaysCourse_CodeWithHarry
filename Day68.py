# Exercise 7 - Clear the Clutter


import os

files = os.listdir("clutterFolder")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)

    os.rename(f"clutterFolder/{file}", f"clutterFolder/{i}.png")
    i += 1
