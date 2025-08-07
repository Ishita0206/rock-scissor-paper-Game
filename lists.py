import random

computer = random.choice([1,2,3])
you = int(input("Enter 1 for rock \n Enter 2 for scissor \n Enter 3 for paper \n Enter ur no."))
list = ["rock", "scissor", "paper"]

if(you<1 or you>3):
    print("Invalid input")
else: 
    print(f"You choose {list[you-1]} \n Computer choose {list[computer-1]}")

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

