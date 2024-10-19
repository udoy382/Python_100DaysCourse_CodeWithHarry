# Dictionaries in Python


dic = {
    "Udoy": "Human being",
    "Spon": "Object",
    436: "Udoy",
    222: "Mariyam"
}


# print(dic["Udoy"])
# print(dic[222])


# print(dic)
# print(dic["Spon"])


# if key not exist `print(dic["Spon"])` this programm show an error but `print(dic.get("Udoy"))` this programm doesn't show an error.
# print(dic.get("Udoy"))


# print(dic.keys())
# print(dic.values())
# print(dic.items())


# for key in dic.keys():
#     print(dic[key])


# for key in dic.keys():
#     print(f"The value corresponding to the key {key} is {dic[key]}")


for key, value in dic.items():
    print(f"The value corresponding to the key {key} is {value}")