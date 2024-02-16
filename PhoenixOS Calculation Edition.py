
print("Welcome to PhoenixOS")
print()
print("You are running a calculation verion of PhoenixOS for the full version vist bit.ly/phoenixoswebsite")
print()
print("-------------------------")
print("about --- OS about")
print()
print("A1 --- Calculator")
print("-------------------------")
print()
app_open = input("Open an aplication: ")
 
print("<<<OPENING>>>")
print()
print()
 
 
if app_open == "about" or app_open == "ABOUT":
    print("PhoenixOS Calculation edition")
    print("bit.ly/phoenixoswebsite")
    print("Coded in Python By Phoenix Shepherd")
 
 
#calculator
elif app_open == "A1" or app_open == "a1":
    print("Welcome to the Calculator")
    print("In this app you will enter 2 numbers then the software will tell you different answers")
    calc_num1 = input("Enter a number: ")
    calc_num2 = input("Enter another number: ")
    
    #basic math
    calc_sum1 = float(calc_num1) + float(calc_num2)
    calc_sum2 = float(calc_num1) - float(calc_num2)
    calc_sum3 = float(calc_num1) * float(calc_num2)
    calc_sum4 = float(calc_num1) / float(calc_num2)
    print()
    print()
    print()
    print("Answers:")
    print()
    print()
    print("by adding " + str(calc_num1) + " and " + str(calc_num2) + " you get " + str(calc_sum1))
    print()
    print(str(calc_num1) + " take away " + str(calc_num2) + " is " + str(calc_sum2))
    print()
    print("by multiplying " + str(calc_num1) + " and " + str(calc_num2) + " you get " + str(calc_sum3))
    print()
    print("by dividing " + str(calc_num1) + " by " + str(calc_num2) + " you get " + str(calc_sum4))
 
 
 
else:
    print("That is not an application")