# Kaun Banega Crorepati: Exercise 3 - Solution

questions = [
    ["Which language was used to create facebook?", "Python", "French", "JavaScript", "Php", "None", 4],
    ["Which language was used to create instagram?", "Python", "French", "JavaScript", "Php", "None", 4],
    ["Which language was used to create twitter?", "Python", "French", "JavaScript", "Php", "None", 4],
    ["Which language was used to create linkedine?", "Python", "French", "JavaScript", "Php", "None", 4],
    ["Which language was used to create linkedine?", "Python", "French", "JavaScript", "Php", "None", 4],
    ["Which language was used to create linkedine?", "Python", "French", "JavaScript", "Php", "None", 4]

]

levels = [1000, 2000, 3000, 4000, 5000, 6000, 10000, 20000, 50000]
money = 0

i = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(f"a.{question[1]} - a.{question[2]} - a.{question[3]} - a.{question[4]}")

    reply = int(input("Enter your answer (1-4) : "))
    if (reply == question[-1]):
        print(f"correct answer, you have won Rs. {levels[i]}")
        if (i == 4):
            money = 10000
        elif (i == 9):
            money = 320000
        elif (i == 14):
            money = 140000
    else:
        print("Wrong answer")
        break