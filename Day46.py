# os Module in Python

import os


# Check folder already existe or not ~
# if (not os.path.exists["data"]):
#     os.mkdir("data")



# Make a new folder with `os.mkdir` function ~
# os.mkdir("data")



# Make a range of folder with this `for loop` and `os.mkdir` ~
# for i in range(0, 100):
#     os.mkdir(f"data/Day{i+1}")



# Rename any folder with `os.rename` method ~
# for i in range(0, 100):
#     os.rename(f"data/Day{i+1}", f"data/Tutorial{i+1}")



# Print all folders and see all files on folders ~
# folders = os.listdir("data")
# # print(folders)

# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))



# See current path/location ~
# print(os.getcwd())


# Change directory ~
# os.chdir("#")
# print(os.getcwd())