
""" Phoenix OS """

sys_os_version = 1.3

print("Welcome To Phoenix OS")
print()
print("SYSTEM")
print("---------------")
print("about --- OS information")
print("help --- OS tips")
print()
print()
print("APPLICATION")
print("---------------")
print("A1 --- 2 by 2 addition calcuator")
print("A2 --- 2 by 2 subtraction calculator")
print("A3 --- 2 by 2 multiplucation calculator")
print("A4 --- 2 by 2 division calculator")
print("A5 --- tell me a joke")
print("A6 --- padlock")
print("A7 --- guess the number/word")
print("A8 --- rock paper scissors")
print()
app_open = input("Please select an app: ")


print("<<<launching>>>")
print()
print()





#quit
if app_open == "":
    print("System Quit>>>>>")




#about
elif app_open == "about" or app_open == "ABOUT":
    print("OS Version " + str(sys_os_version))
    print("bit.ly/phoenixoswebsite")
    print("Coded in Python By Phoenix Shepherd")



#guide
elif app_open == "help" or app_open == "HELP":
    print("PhoenixOS tips for version " + str(sys_os_version))
    print()
    print("1. in the home screen click the enter key in the app launcher and the software will close")
    print()
    print("2. updated versions of PhoenixOS are avalible at bit.ly/phoenixoswebsite")
    print()
    print("3. applications can not be launched by their name but by their shortcut(on the left of the app name)")
    print()
    print("4. an apps shortcut is cap sensitive you can only use all upercase or all lowercase words")
    print()
    print("5. some people may find newer verions of PhoenixOS hard to use.")
    print("  Old versions of PhoenixOS are avalible at bit.ly/phoenixoswebsite")
    print()
    print("6. during 2 player games 100 lines may be printed to reduce cheating but this may reduse performance")




# 2 by 2 addition
elif app_open == "A1" or app_open == "a1":
    app_2plus2_num1 = float(input("Enter your 1st number: "))
    app_2plus2_num2 = float(input("What will you add that to: "))
    app_2plus2_solve = (app_2plus2_num1) + (app_2plus2_num2)
    print("you number is: " + str(app_2plus2_solve))



# 2 by 2 subtraction
elif app_open == "A2" or app_open == "a2":
    app_2sub2_num1 = float(input("Enter your 1st number: "))
    app_2sub2_num2 = float(input("What will you subtract from that number: "))
    app_2sub2_solve = (app_2sub2_num1) - (app_2sub2_num2)
    print("you number is: " + str(app_2sub2_solve))





# 2 by 2 multi calculator
elif app_open == "A3" or app_open == "a3":
    app_2x2_num1 = input("Enter your 1st number: ")
    app_2x2_num2 = input("What will you multiply this by: ")
    app_2x2_solve = float(app_2x2_num1) * float(app_2x2_num2)
    print("you number is: " + str(app_2x2_solve))



# 2 by 2 division calculator
elif app_open == "A4" or app_open == "a4":
    app_2d2_num1 = input("Enter your 1st number: ")
    app_2d2_num2 = input("what will you divide that by: ")
    app_2d2_solve = float(app_2d2_num1) / float(app_2d2_num2)
    print("you number is: " + str(app_2d2_solve))




#tell me a joke
elif app_open == "A5" or app_open == "a5":
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
elif app_open == "A6" or app_open == "a6":
    print("welcome to pad lock")
    app_pad_error = "the lock wont work and you give up"
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
                    print(app_pad_error)
            else:
                print(app_pad_error)
        else:
            print(app_pad_error)
    else:
        print(app_pad_error)





#guess the number/word
elif app_open == "A7" or app_open == "a7":
    print("this app requires 2 players")
    app_guessnumorword_type = input("will you guess the number or word? ")
    if app_guessnumorword_type == "number":
        print()
        app_guessnumorword_num = input("what number will you go to: ")
        app_guessnumorword_player1 = input("pick your number on a scale of 1 to " + app_guessnumorword_num + ": ")
        print("\n" * 100)
        app_guessnumorword_player2 = input("guess the number on a scale of 1 to " + app_guessnumorword_num + ": ")
        print()
        if app_guessnumorword_player1 == app_guessnumorword_player2:
            print("Congrats player2 you win!")
        elif app_guessnumorword_player1 != app_guessnumorword_player2:
            print("Sorry player2 you lost the number was " + app_guessnumorword_player1)
    
    elif app_guessnumorword_type == "word":
        print()
        print("words:  (funny) (happy) (dog) (cat) (water) (camera) (or your own)")
        app_guessnumorword_player1 = input("pick a word: ")
        print("\n" * 100)
        print("(funny) (happy) (dog) (cat) (water) (camera) (or your own)")
        app_guessnumorword_player2 = input("player2 pick a word: ")
        print()
        if app_guessnumorword_player1 == app_guessnumorword_player2:
            print("congrats player2 you win")
        elif app_guessnumorword_player1 != app_guessnumorword_player2:
            print("sorry player2 you loose")
    else:
        print("that is not a choice")




#rpc
elif app_open == "A8" or app_open == "a8":
    print("This is a 2 player game")
    print("remember your answer must be lowercase")
    app_rpc_player1 = input("rock,paper,scissors: ")
    print("\n" * 100)
    print("remember your answer must be lowercase")
    app_rpc_player2 = input("rock,paper,scissors: ")
    
    #check p1
    app_rpc_rock_beats_scissors = app_rpc_player1 == "rock" and app_rpc_player2 == "scissors"
    app_rpc_scissors_beats_paper = app_rpc_player1 == "scissors" and app_rpc_player2 == "paper"
    app_rpc_paper_beats_rock = app_rpc_player1 == "paper" and app_rpc_player2 == "rock"
    #check p2
    app_rpc_rock_beats_scissors2 = app_rpc_player2 == "rock" and app_rpc_player1 == "scissors"
    app_rpc_scissors_beats_paper2 = app_rpc_player2 == "scissors" and app_rpc_player1 == "paper"
    app_rpc_paper_beats_rock2 = app_rpc_player2 == "paper" and app_rpc_player1 == "rock"
    
    if app_rpc_rock_beats_scissors or app_rpc_scissors_beats_paper or app_rpc_paper_beats_rock:
        print("player1 wins")
    elif app_rpc_rock_beats_scissors2 or app_rpc_scissors_beats_paper2 or app_rpc_paper_beats_rock2:
        print("player2 wins")
    else:
        print()
        print("someone cheated nobody wins")


#app unable to open
else:
    print()
    print("The application was unable to launch. " + app_open + " could not be found")