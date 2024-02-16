
""" Phoenix OS """
 
 
sys_os_version = 1.0
 
 
print("Welcome To Phoenix OS")
 
 
print("pick one of these applications: ")
print()
print("quit --- close software")
print()
print("sys --- system")
print()
print("Application:")
print("A1 --- 2 by 2 multiplucation calculator")
print("A2 --- 2 by 2 division calculator")
print("A3 --- tell me a joke")
print("A4 --- padlock")
print("A5 --- guess the number/word")
app_open = input()
 
print()
print()
print()
print("-----launching-----")
print()
 
 
 
#quit
if app_open == "quit" or app_open == "QUIT":
    print()
    print("System Quit>>>>>")
 
 
 
 
#about
elif app_open == "sys" or app_open == "SYS":
    print("OS Version " + str(sys_os_version))
    print("bit.ly/phoenixoswebsite")
    print("Coded in Python By Phoenix Shepherd")
 
 
 
# 2 by 2 multi calculator
elif app_open == "A1" or app_open == "a1":
    app_2x2_num1 = input("Enter your 1st number: ")
    app_2x2_num2 = input("Enter your 2nd number: ")
    app_2x2_solve = int(app_2x2_num1) * int(app_2x2_num2)
    print("you number is: " + str(app_2x2_solve))
    print()
    print("APPLICATION CLOSED>>>>>>>")
 
 
 
# 2 by 2 division calculator
elif app_open == "A2" or app_open == "a2":
    app_2d2_num1 = input("Enter your 1st number: ")
    app_2d2_num2 = input("Enter your 2nd number: ")
    app_2d2_solve = int(app_2d2_num1) / int(app_2d2_num2)
    print("you number is: " + str(app_2d2_solve))
    print()
    print("APPLICATION CLOSED>>>>>>>")
    
    
    
    
#tell me a joke
elif app_open == "A3" or app_open == "a3":
    app_joke_pick = input("pick a joke 1/2/3  ")
    
    if app_joke_pick == "1":
        input("what did one traffic light say to the other? (press ENTER) ")
        print("stop looking im changing!")
    
    elif app_joke_pick == "2":
        input("what do you call a boomerang that wont come back? (press ENTER) ")
        print("a stick")
        
    elif app_joke_pick == "3":
        input("what do you call a fake noodle? (press ENTER) ")
        print("an impasta!")
        print()
        print("APPLICATION CLOSED>>>>>>>")
    
    else:
        input("what did the program say to the user? (press ENTER) ")
        print("That is not a valid joke")
 
 
 
#pad lock
elif app_open == "A4" or app_open == "a4":
    print("welcome to pad lock")
    print()
    print("while strolling through the city you notice a mini safe and think what could be inside it?")
    print("lock proggress: ????")
    app_pad_firstguess = input("you try the first number: ")
    if app_pad_firstguess == "1":
        print("the lock starts becoming loose")
        print("lock proggress: 1???")
        print()
        app_pad_secondguess = input("try a second number: ")
        if app_pad_secondguess == "8":
            print("the lock becomes loose you gain hope")
            print("lock proggress: 18??")
            print()
            app_pad_thirdguess = input("try a third number: ")
            if app_pad_thirdguess == "6":
                print("the lock is almost out and you are determend to find whats inside")
                print("lock proggress: 186?")
                print()
                app_pad_fourthguess = input("try the final number: ")
                if app_pad_fourthguess == "4":
                    print("the lock is open and you find...")
                    print("nothing")
                else:
                    print("the lock wont work and you give up")
            else:
                print("the lock wont work and you give up")
        else:
            print("the lock wont work and you give up")
    else:
              print("the lock wont work and you give up")
 
 
 
 
#guess the number
elif app_open == "A5" or app_open == "a5":
    print("this app requires 2 players")
    app_guessnumorword_type = input("number or word? ")
    if app_guessnumorword_type == "number":
        print()
        app_guessnumorword_num = input("what number will you go to: ")
        app_guessnumorword_player1 = input("pick your number on a scale of 1 to " + app_guessnumorword_num + ": ")
        app_guessnumorword_player2 = input("guess the number on a scale of 1 to " + app_guessnumorword_num + ": ")
        print()
        if app_guessnumorword_player1 == app_guessnumorword_player2:
            print("Congrats player2 you win!")
        elif app_guessnumorword_player1 != app_guessnumorword_player2:
            print("Sorry player2 you lost the number was " + app_guessnumorword_player1)
    
    elif app_guessnumorword_type == "word":
        print()
        print("words:  (funny) (happy) (dog) (cat) (water) (camera)")
        app_guessnumorword_player1 = input("pick a word: ")
        print()
        app_guessnumorword_player2 = input("player2 pick a word: (funny) (happy) (dog) (cat) (water) (camera) ")
        print()
        if app_guessnumorword_player1 == app_guessnumorword_player2:
            print("congrats player2 you win")
        elif app_guessnumorword_player1 != app_guessnumorword_player2:
            print("sorry player2 you loose")
 
    else:
        print("that is not a choice")
 
 
 
 
 
# secret code
elif app_open == "never gonna give you up":
    print("never gonna let you down never gonna run around and desert you")
    print("never gonna make you cry never gonna say goodbye")
    print(":)")
    
elif app_open == "school sucks":
    print("i know its so long")
        
else:
    print()
    print("That is not a valid application>>>>>>>>>")