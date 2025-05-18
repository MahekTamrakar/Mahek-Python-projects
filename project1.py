#project 1 mini calculator
print("----- MINI CALCULATOR -----")
#giving numbers 
num1=float(input("Enter First Number: "))
num2=float(input("Enter Second Number: "))
#giving operators
print("!!!!! Choose Operation !!!!!")
print("Press 1:- ADDITION")
print("Press 2:- SUBTRACTION")
print("Press 3:- MULTIPLICATION")
print("Press 4:- DIVISION")
#ask for choice
choice=int(input("Enter Your Choice: "))
#choice=addition
if choice == 1:
    summ=num1+num2
    print("Addition is: ")
    print(summ)
#choice = subtraction
elif choice == 2:
    sub=num1-num2
    print("Subtraction is: ")
    print(sub)
#choice = multiplication
elif choice == 3:
    multi=num1*num2
    print("Product is: ")
    print(multi)
#choice=division
elif choice == 4:
    div=num1/num2
    print("Division is: ")
    print(div)
#when input is wrong
else:
    print("INVALID INPUT")
#code completed