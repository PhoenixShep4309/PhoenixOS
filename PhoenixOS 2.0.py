
"""PhoenixOS"""
import random
import pygame
pygame.init()
phoenixos_power = True
sys_os_version = 2.0
print("----------------------------------------")
input("PhoenixOS is ready to run press ENTER    ")
print("\n" * 100)


while phoenixos_power:
    print("Welcome Back")
    print()
    print(" System Applications  ")
    print(" --------------------------------------------")
    print("| about ~~~~~~~~~~~~~~~~~~ OS information    |")
    print("| help ~~~~~~~~~~~~~~~~~~~ OS tips           |")
    print("| dev ~~~~~~~~~~~~~~~~~~~~ developer credits |")
    print(" --------------------------------------------")
    print()
    print(" Your Apps  ")
    print(" -----------------------------------------------")
    print("| A1 ~~~~~~~~~ 2 by 2 addition calcuator        |")
    print("| A2 ~~~~~~~~~ 2 by 2 subtraction calculator    |")
    print("| A3 ~~~~~~~~~ 2 by 2 multiplucation calculator |")
    print("| A4 ~~~~~~~~~ 2 by 2 division calculator       |")
    print("| A5 ~~~~~~~~~ Padlock                          |")
    print("| A6 ~~~~~~~~~ Guess the number/word            |")
    print("| A7 ~~~~~~~~~ Rock paper scissors              |")
    print("| A8 ~~~~~~~~~ Password generator               |")
    print(" -----------------------------------------------")
    print()
    print(" Commands    ")
    print(" -----------------------------")
    print("| C1 ~~~~~~~~~ Flip a coin    |")
    print("| C2 ~~~~~~~~~ Random number  |")
    print("| C3 ~~~~~~~~~ Timer          |")
    print(" -----------------------------")
    print()
    app_open = input("Please enter an app shortcut code: ")
    print("\n" * 100)
    
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print()
    
    
    
    


    #quit
    if app_open == "":
        print("PhoenixOS has been shutdown")
        phoenixos_power = False
    


    
    #about
    elif app_open == "about" or app_open == "ABOUT" or app_open == "About":
        print("OS Version " + str(sys_os_version))
        print("bit.ly/phoenixoswebsite")
    
    


    #guide
    elif app_open == "help" or app_open == "HELP" or app_open == "Help":
        print("PhoenixOS tips for version " + str(sys_os_version))
        print()
        print("1. in the home screen click the enter key in the app launcher and the software will close")
        print("2. updated versions of PhoenixOS are avalible at bit.ly/phoenixoswebsite")
        print("3. applications can not be launched by their name but they can by their shortcut(on the left of the app name)")
        print("4. app shortcuts are cap sensitive you can use all upercase the first letter upercase and all lowercase words")
        print("5. some people may find newer verions of PhoenixOS hard to use.")
        print("   old versions of PhoenixOS are avalible at bit.ly/phoenixoswebsite")
        print("6. during 2 player games 100 lines may be printed to reduce cheating")
    
    
    


    #credit
    elif app_open == "dev" or app_open == "DEV" or app_open == "Dev":
        print("developer credits for version " + str(sys_os_version))
        print("Phoenix Shepherd --- Main Coder")
    
    


    
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
    
    
    


    #pad lock
    elif app_open == "A5" or app_open == "a5":
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
    elif app_open == "A6" or app_open == "a6":
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
    elif app_open == "A7" or app_open == "a7":
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
        #tie
        
        
        if app_rpc_rock_beats_scissors or app_rpc_scissors_beats_paper or app_rpc_paper_beats_rock:
            print("player1 wins")
        elif app_rpc_rock_beats_scissors2 or app_rpc_scissors_beats_paper2 or app_rpc_paper_beats_rock2:
            print("player2 wins")
        elif app_rpc_player1 == app_rpc_player2:
            print("Tie")
        else:
            print()
            print("someone cheated nobody wins")
    




    #password
    elif app_open == "A8" or app_open == "a8":
        app_pass_choose = input("Enter 1 for a 4 digit code. Or enter the letter A for a password:  ")
        if app_pass_choose == "1":
            app_pass_num = random.randint(1000, 9999)
            print("4 digit code: " + str(app_pass_num))
        elif app_pass_choose == "a" or app_pass_choose == "A":
            app_pass_name = input("What is your name: ")
            app_pass_favnum = input("What is your favorite number: ")
            app_pass_wordrand = random.randint(100, 999)
            print("Your password can be: " + str(app_pass_wordrand) + app_pass_name + "?!" + app_pass_favnum)
        else:
            print("Sorry try again")








    #flip a coin
    elif app_open == "c1" or app_open == "C1":
        app_flipacoin_coin = random.randint(1, 2)
        if app_flipacoin_coin == 1:
            print("HEADS")
        elif app_flipacoin_coin == 2:
            print("TAILS")
    
    elif app_open == "c2" or app_open == "C2":
        app_randnum_digit = input("do you want 1 digit 2 digits 3 digits or 4 digits: ")
        if app_randnum_digit == "1":
            app_randnum_num = random.randint(1, 9)
        elif app_randnum_digit == "2":
            app_randnum_num = random.randint(10, 99)
        elif app_randnum_digit == "3":
            app_randnum_num = random.randint(100, 999)
        elif app_randnum_digit == "4":
            app_randnum_num = random.randint(1000, 9999)
        print("Your random number is: " + str(app_randnum_num))
    
    elif app_open == "c3" or app_open == "C3":
        app_time_zero = 000
        print("the timers maximum seconds is curently 60")
        print("1 second = 1000 milliseconds")
        app_time_sec = int(input("How many milliseconds will the timer take: "))
        if app_time_sec > 60000:
            app_time_sec = 60000
            print("The timer was changed to 60 seconds")
        if app_time_sec < 60001:
            input("Starting timer when you press enter    ")
            print("Timer Started")
            pygame.time.wait(app_time_sec)
            print("Timer ended")
    
    
    
    
    
    else:
        print("The application was unable to launch. " + app_open + " could not be found")




    print()
    print("Press ENTER to retern home")
    input()
    print("\n" * 100)