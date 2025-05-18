#project 4 ROCK PAPER SCISSOR GAME 
#importing random module
import random
#making list 
glist=["R","P","S"]
#asking for name
print("###### WELCOME TO THE ROCK PAPER SCISSOR GAME ######")
user_name=input("Enter Your Name:")
#asking for user choice
print("Your Turn--")
print("Press R For Rock")
print("Press P For Paper")
print("Press S For Scissor")
user_input=input("Enter Your Choice:")
#system generating random item from list
sys_input=random.choice(list(glist))
print("Computer Choice=",sys_input)
#condition for rock
if user_input == glist[0]:
    if sys_input == glist[1]:
        print("Computer Won!!!!!")
    elif sys_input == glist[2]:
        print(user_name,"Won!!!!!")
    elif sys_input == glist[0]:
        print("Draw")
    else:
        print("Wrong Input...")
#condition for paper
elif user_input == glist[1]:
    if sys_input == glist[0]:
        print(user_name,"Won!!!!!")
    elif sys_input == glist[2]:
        print("Computer Won!!!!!")
    elif sys_input == glist[1]:
        print("Draw")
    else:
        print("Wrong Input...")
#condition for scissor
elif user_input == glist[2]:
    if sys_input == glist[0]:
        print("Computer Won!!!!!")
    elif sys_input == glist[1]:
        print(user_name,"Won!!!!!")
    elif sys_input == glist[2]:
        print("Draw")
    else:
        print("Wrong Input...")
else:
    print("Wrong Input...")
#code completed
