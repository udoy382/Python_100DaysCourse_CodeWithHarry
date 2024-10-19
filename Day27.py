# Exercise 3

import random

questionList = [
    "Who is prime minister of Bangladesh:\n (a) Sheikh Hasina (b) Obaidul Quader\n (c) Bill Guets (d) Saifur Rahman Udoy",
    "Who is president of Bangladesh:\n (a) Fozlu Mia (b) Jack Ma\n (c) Mohammad Abdul Hamid (d) Joe Biden"
]

def kaunBanegaCrorepati():
    print(random.choice(questionList))
    user = input("Enter Your Answer: ")

    if questionList[0]:
        if user == "a" or user == "Sheikh Hasina".lower():
            print("Correct Answer")
        else:
            print("Oops! Wrong Answer")
    if questionList[1]:
        if user == "c" or user == "Mohammad Abdul Hamid".lower():
            print("Correct Answer")
        else:
            print("Oops! Wrong Answer")

kaunBanegaCrorepati()