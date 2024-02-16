
"""PhoenixOS"""
#SETUP
print("\n" * 100)
print("SETTING UP")
print("Importing random library")
import random
print("Imported random")
print("Importing time library")
import time
print("Imported time")
print("Importing pygame library")
import pygame
print("Imported pygame")
print("Initializing pygame")
pygame.init()
print("pygame Initialized")
print("checking software version")
sys_os_version = 2.4
print("Software version recognized: " + str(sys_os_version))
print("assigning line amount")
Line_amount = 100
Blank_status = "OFF"
print("line number assigned: " + str(Line_amount))
print("assigning home commands")
phoenixos_power = True
AskForHome = True
print("home commands assigned")
print()
print("READY")
print("\n" * Line_amount)












#START OS
while phoenixos_power:
    t = time.localtime()
    current_time = time.strftime("%D  %H:%M", t)
    print("Current time: " + str(current_time))
    print("------------------------------------------------------------------------------------")
    print()
    print("  A1~calculator    A2~Padlock    A3~Guess the number/word    A4~Rock paper scissors")
    print()
    print("  A5~Password generator    A6~Timer    A7~Settings    off~shutdown")
    print()
    print("------------------------------------------------------------------------------------")
    print()
    app_open = input("Please enter an app shortcut code: ")
    print("\n" * Line_amount)
    print("-----------------")
    print()
    print()


    #SETTINGS
    if app_open == "A7" or app_open == "a7":
        settings_lock = True
        while settings_lock:
            if Line_amount == 100:
                Blank_staus = "OFF"
            if Line_amount == 10:
                Blank_status = "ON"
            print("Settings")
            print("1. About")
            print("2. Help")
            print("3. Reduce Blanks     " + Blank_status)
            print()
            Setting_num = input("Enter a setting number or press enter to leave: ")
            print("\n" * Line_amount)
            #DISABLE RETURN LOOP
            if Setting_num == "":
                settings_lock = False 
            #ABOUT
            if Setting_num == "1":
                print("developer credits for version " + str(sys_os_version))
                print("Phoenix Shepherd --- Main Coder")
                print()
                print("System version: " + str(sys_os_version))
                print()
                input("Press enter to go back")        
            #HELP
            elif Setting_num == "2":
                print("PhoenixOS tips for version " + str(sys_os_version))
                print("1. after a while you might notice slower performance to fix this shutdown and restart PhoenixOS")
                print("2. sometimes PhoenixOS will print 100 blank lines to make reading easier however ")
                print("   this can lower speed. To lower the amount of lines turn ON reduce blanks in settings")
                print("3. the time on the home screen does not have live updates it changes when it is reprinted")
                print()
                input("Press enter to go back") 
            #REDUCE BLANKS
            elif Setting_num == "3":
                print("If this is off during usage of the software 100 blank lines may be printed to make usage and reading easier")
                print("but this may cause low performace resulting in slower load times the longer the software has been running")
                print("if this setting is on only 10 blank lines will be printed however in 2 player games the normall 100 lines will be printed")
                Line_choice = input("Enter OFF to use the default 100 lines or type ON to use 10 lines. to exit press enter")
                if Line_choice == "ON" or Line_choice == "on" or Line_choice == "On":
                    Line_amount = 10
                    Blank_status = "ON"
                    print("Reduce blanks enabled")
                elif Line_choice == "OFF" or Line_choice == "off" or Line_choice == "Off":
                    Line_amount = 100
                    Blank_status = "OFF"
                    print("Reduce blanks disabled")
            print("\n" * Line_amount)
        AskForHome = False
        #END OF SETTINGS
        
        
    #DISABLE HOME LOOP ON SHUTDOWN
    elif app_open == "off" or app_open == "OFF" or app_open == "Off":
        phoenixos_power = False   
        
        
    #CALCULATOR
    elif app_open == "A1" or app_open == "a1":
        app_calc_type = input("Enter 1 for addition or 2 for subtraction or 3 for multiplication or 4 for division: ")
        #ADD
        if app_calc_type == "1":
            app_2plus2_num1 = float(input("Enter your 1st number: "))
            app_2plus2_num2 = float(input("What will you add that to: "))
            app_2plus2_solve = (app_2plus2_num1) + (app_2plus2_num2)
            print("you number is: " + str(app_2plus2_solve))
        #SUBTRACT
        if app_calc_type == "2":
            app_2sub2_num1 = float(input("Enter your 1st number: "))
            app_2sub2_num2 = float(input("What will you subtract from that number: "))
            app_2sub2_solve = (app_2sub2_num1) - (app_2sub2_num2)
            print("you number is: " + str(app_2sub2_solve))
        #MULTI
        if app_calc_type == "3":
            app_2x2_num1 = input("Enter your 1st number: ")
            app_2x2_num2 = input("What will you multiply this by: ")
            app_2x2_solve = float(app_2x2_num1) * float(app_2x2_num2)
            print("you number is: " + str(app_2x2_solve))
        #DIVISION
        if app_calc_type == "4":
            app_2d2_num1 = input("Enter your 1st number: ")
            app_2d2_num2 = input("what will you divide that by: ")
            app_2d2_solve = float(app_2d2_num1) / float(app_2d2_num2)
            print("you number is: " + str(app_2d2_solve))
        else:
            print("Could not find the command")
            #END OF CALCULATOR
            
            
    #PAD LOCK
    elif app_open == "A2" or app_open == "a2":
        print("welcome to pad lock")
        app_pad_error = "the lock wont work and you give up"
        print()
        print("while strolling through the city you notice a mini safe and think what could be inside it?")
        print("lock proggress: ????")
        app_pad_firstguess = input("you try the first number: ")
        if app_pad_firstguess == "4":
            print("the lock starts becoming loose")
            print("lock proggress: 4???")
            print()
            app_pad_secondguess = input("try a second number: ")
            if app_pad_secondguess == "7":
                print("the lock becomes loose you gain hope")
                print("lock proggress: 47??")
                print()
                app_pad_thirdguess = input("try a third number: ")
                if app_pad_thirdguess == "8":
                    print("the lock is almost out and you are determend to find whats inside")
                    print("lock proggress: 478?")
                    print()
                    app_pad_fourthguess = input("try the final number: ")
                    if app_pad_fourthguess == "6":
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
    
    
    #GUESS NUM/WORD
    elif app_open == "A3" or app_open == "a3":
        print("this app requires 2 players")
        app_guessnumorword_type = input("will you guess the number or word? ")
        #NUMBER
        if app_guessnumorword_type == "number":
            print()
            app_guessnumorword_num = input("what is the maximum the number can go to: ")
            app_guessnumorword_player1 = input("pick your number on a scale of 1 to " + app_guessnumorword_num + ": ")
            print("\n" * 100)
            app_guessnumorword_player2 = input("guess the number on a scale of 1 to " + app_guessnumorword_num + ": ")
            print()
            if app_guessnumorword_player1 == app_guessnumorword_player2:
                print("Congrats player2 you win!")
            elif app_guessnumorword_player1 != app_guessnumorword_player2:
                print("Sorry player2 you lost the number was " + app_guessnumorword_player1)
        #WORD
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
            #END OF GUESS NUM/WORD
            
    
    #ROCK PAPER SCI
    elif app_open == "A4" or app_open == "a4":
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
    
    
    #PASSWORD CREATOR
    elif app_open == "A5" or app_open == "a5":
        app_pass_choose = input("Enter 1 for a 4 digit code. Or enter the letter 2 for a password:  ")
        if app_pass_choose == "1":
            app_pass_num = random.randint(1000, 9999)
            print("4 digit code: " + str(app_pass_num))
        elif app_pass_choose == "2":
            app_pass_name = input("What is your name: ")
            app_pass_favnum = input("What is your favorite number: ")
            app_pass_wordrand = random.randint(100, 999)
            print("Your password can be: " + str(app_pass_wordrand) + app_pass_name + "?!" + app_pass_favnum)
        else:
            print("Sorry try again")
            
    #TIMER
    elif app_open == "A6" or app_open == "a6":
        print("the timers maximum seconds is curently 5 minutes (300 seconds)")
        app_time_sec = int(input("How many seconds will the timer be: "))
        if app_time_sec > 300:
            app_time_sec = 10
            print("you passed the maximum time and the timer was changed to 10 seconds")
        if app_time_sec < 301:
            input("Starting timer when you press enter    ")
            print("Timer Started")
            app_time_sec *= 1000
            pygame.time.wait(app_time_sec)
            print("Timer ended")
    
    #UNFOUND PROGRAM
    else:
        print("The application was unable to launch. " + app_open + " could not be found")
        
    #SHUTDOWN
    if phoenixos_power == False:
        print("program loop diabled press enter to end the program or enter ON to go back to PhoenixOS")
        phoenixos_power_switch = input()
        if phoenixos_power_switch == "ON" or phoenixos_power_switch == "on" or phoenixos_power_switch == "On":
            phoenixos_power = True  
            
    #CHECK FOR ASKING TO GO BACK
    if phoenixos_power:
        print()
        if AskForHome == True:
            print("Press ENTER to return home")
            input()
        AskForHome = True
        print("\n" * Line_amount)
        
#WHEN POWER OFF
print("\n" * Line_amount)
print("PhoenixOS closed")