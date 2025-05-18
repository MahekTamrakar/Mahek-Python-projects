#project 2 number guessing game
#importing random module
import random
print("----- NUMBER GUESSING GAME -----")
#asking for name
name=input("Enter your Name: ")
#telling about rules
print("----- RULES -----")
print("1. You have to guess any number between 1-10")
print("2. Similarly computer will give any number between 1-10")
print("3. If your number is greater than computer's number you will win and vice versa")
print("If both the numbers are same it's a tie")
print("----- Let's Play -----")
#asking for number
ynum=int(input("Enter your number: "))
#comp will generate number
cnum=random.randint(1,11)
print("Computer number is: %s " %(cnum))
#giving cond user is greater than comp number
if ynum > cnum :
    print( "Congratulations!!! " + name + " You Won")
#giving cond user is lesser than comp number
elif ynum < cnum :
    print("Computer Won")
#if both will have same numbers the else state. will execute
else :
    print("It's a Tie")
#code completed

