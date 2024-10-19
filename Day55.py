# Excercise 5 - Snake Water Gun

import random

number = [1, 2 ,3]

def waterGunGame():
    text = "1: Gun\n2: Water\n3: Snake"
    print(text)

    player = int(input("Enter Your Option: "))
    computer = random.choice(number)

    if player == 1:
        if computer == 2:
            print("Oops! Computer is win. (2)")
        elif computer == 3:
            print("Congratulation! You are win. (3)")
        else:
            print("Match drow, try again. (1)")
    elif player == 2:
        if computer == 1:
            print("Congratulation! You are win. (1)")
        elif computer == 3:
            print("Oops! Computer is win. (3)")
        else:
            print("Match drow, try again (2)")

    elif player == 3:
        if computer == 1:
            print("Oops! Computer is win. (1)")
        elif computer == 2:
            print("Congratulation! You are win. (2)")
        else:
            print("Match drow. try again. (3)")

    else:
        print("Something wrong!")


waterGunGame()