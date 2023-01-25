import random
from sys import exit
choice=input("Rock (r), Paper (p) or Scissors (s)? ")
option_list=["Rock","Paper","Scissors"]

if choice not in ["r","p","s"]:
    print("Invalid choice!")
    exit()

for i in range(len(option_list)):
    if choice==["r","p","s"][i]:
        choice=option_list[i]

pc_selected=option_list[random.randint(0, 2)]

print(f"The computer chose {pc_selected}.")

if choice==pc_selected:
    print("Draw")
else:
    if choice=="Rock" and pc_selected=="Scissors" or \
        choice=="Paper" and pc_selected=="Rock" or \
            choice=="Scissors" and pc_selected=="Paper":
                print("You win!")
    else:
        print("You lose!")
