import random

computer = random.choice([1,2,3])
you = int(input("Enter 1 for rock \n Enter 2 for scissor \n Enter 3 for paper \n Enter ur no."))
dict = {1: "rock", 2: "scissor", 3: "paper"}

if you not in dict:
    print("Invalid input")
else:
     print(f"You choose {dict[you]} \n Computer choose {dict[computer]}")

if(computer == you):
    print(" Its draw!!")

else:
    if(computer == 1 and you == 2):
        print("You LOSE!!")
    
    elif(computer == 1 and you == 3):
        print("You WIN!!")

    elif(computer == 2 and you == 1):
        print("You WIN!!")

    elif(computer == 2 and you == 3):
        print("You LOSE!!")

    elif(computer == 3 and you == 1):
        print("You LOSE!!")

    elif(computer == 3 and you == 2):
        print("You WIN!!")


