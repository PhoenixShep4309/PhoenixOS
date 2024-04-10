"""
PhoenixOS
"""

import random
import sys
import time
import os

sys_os_version = 5.3
askforhome = True
first_time = False
print("\n" * 100)

#variables for other apps
loaded_music_file = ""

#Find save file
file = os.path.isfile("PhoenixOS_5_3_Save.txt")
file2 = os.path.isfile("PhoenixOS_Contacts.txt")
file3 = os.path.isfile("PhoenixOS_Reminders.txt")
if file == False or file2 == False or file3 == False:
    print("\n" * 100)

    if not file:
        print("! Main Save File Missing (PhoenixOS_5_3_Save.txt)")
    if not file2:
        print("! Contacts Save File Missing (PhoenixOS_Contacts.txt)")
    if not file3:
        print("! Reminders Save File Missing (PhoenixOS_Reminders.txt)")
    print()
    
    missing = input("One or more save files were not found. Press enter to create the missing files or enter QUIT to exit: ")
    if missing == "QUIT" or missing == "quit" or missing == "Quit":
        print("Closing PhoenixOS")
        sys.exit()
    else: #create save file
        if not file:
            file = open("PhoenixOS_5_3_Save.txt", "w")
            file.write("NONE\nNONE\nON\nON\n\nON\n100\nNONE")
            file.close()
        if not file2:
            file = open("PhoenixOS_Contacts.txt", "w")
            file.write("")
            file.close()
        if not file3:
            file = open("PhoenixOS_Reminders.txt", "w")
            file.write("")
            file.close()
        input("Save files ready. Press enter to continue ")
        print("\n" * 100)

#functions
def LinePrint():
    print("\n" * Line_amount)
def DateAndTime():
    t = time.localtime()
    hour = int(time.strftime("%H", t))
    if hour > 12:
        hour -= 12
    day = time.strftime("%D", t)
    minute = time.strftime("%M")
    current_time = (day + "  " + str(hour) + ":" + minute)
    return current_time
def read_line(line):
    file = open("PhoenixOS_5_3_Save.txt", "r")
    file = file.readlines()
    text = file[line-1]
    text = text.replace("\n", "")
    return text
def write_line(line, text):
    file = open("PhoenixOS_5_3_Save.txt", "r")
    file = file.readlines()
    file[line-1] = text + "\n"
    old_file = open("PhoenixOS_5_3_Save.txt", "w")
    old_file.writelines(file)
    old_file.close()
    
command = read_line(8)
if command != "NONE":
    os.system(command)

try: #pygame
    import pygame
    pygame.init()
    pygame_installed = True
    print("\n" * 100)
except ImportError as e:
    pygame_installed = False

#check reduce blanks
line_file = read_line(7)
if line_file == "100":
    Line_amount = 100
elif line_file == "10":
    Line_amount = 10
else:
    Line_amount = 100

#check user data
name = read_line(1)
password = read_line(2)

#setup software
if name == "NONE" and password == "NONE":
    print("PhoenixOS " + str(sys_os_version) + " Setup")
    print("---------------------")
    name_input = input("Please enter your name. This can be changed later: ")
    while name_input == "NONE":
        name_input = input("Name not allowed. Enter a new name: ")
    password_input = input("Enter a password. This can be changed later: ")
    while password_input == "NONE":
        password_input = input("Password not allowed. Enter a new password: ")
    write_line(1, name_input)
    write_line(2, password_input)
    password = password_input
    name = name_input
    first_time = True
    while not pygame_installed:
        print("\n" * 100)
        print("Aditional files need to be installed.")
        package_action = input("Press enter to download, Enter SKIP to continue with limited functionality, Enter VIEW for more details: ")
        if package_action == "VIEW" or package_action == "view":
            print("\n" * 100)
            print("To install: Pygame")
            print("If you skip the download you wont be able to access the timer")
            print("You can always skip and do the download later in settings")
            input("Press enter to return ")
        if package_action == "":
            os.system("pip install pygame")
            time.sleep(2)
            try:
                import pygame
                pygame.init()
                pygame_installed = True
            except ImportError as e:
                input("Error occoured. Try again later")
            print("\n" * 100)
        if package_action == "SKIP" or package_action == "skip":
            pygame_installed = False
            break
    print()
    print("Setup Complete")
    print("Welcome to PhoenixOS")
    input("Press enter")
    LinePrint()
    print("Welcome to the home screen. Enter a code on the left of the app to open it.")
    print("Press enter with a blank terminal input to close PhoenixOS. this message will not show up again")
    print("----------")
    print()
    print()
    #end of setup

#login
login = read_line(3)
if login == "ON" and first_time == False:
    print("PhoenixOS\n")
    print("Welcome back " + name)
    pass_guess = input("Enter your password to begin: ")
    while pass_guess != password:
        pass_guess = input("Try again: ")
    LinePrint()

#Custom App
try:
    import PhoenixOS_App
    custom_app_name = PhoenixOS_App.Name()
    app_display = ("15 - " + custom_app_name)
    custom_app = True
except:
    app_display = ""
    custom_app = False


#MAIN LOOP
while True:
    print(name)
    print(DateAndTime())
    print()

    #alerts
    if not pygame_installed:
        print("! Libraries Missing. Go to settings for more info.\n")

    #note on home
    note_home = read_line(6)
    if note_home == "ON":
        note_file = read_line(5)
        if note_file == "":
            note_file = "None"
        print("Note: " + note_file)
        print()

    #reminders on home
    remind_home = read_line(4)
    if remind_home == "ON":
        reminders = open("PhoenixOS_Reminders.txt", "r")
        reminders = reminders.read()
        if reminders == "":
            print("Reminders: None")
            print()
        else:
            print("Reminders: ")
            print(reminders)
            print()
    print(" 1 - Calculator             6 - Paintball     11 - Contacts")
    print(" 2 - Guess The Num/Word     7 - TicTacToe     12 - Music Player")
    print(" 3 - Rock Paper Scissors    8 - Match         13 - Encryption")
    print(" 4 - Password Generator     9 - Note          14 - Settings")
    print(" 5 - Timer                  10 - Reminders    " + app_display) 
    print()
    app_open = input("Enter an app number: ")
    LinePrint()

    #CALCULATOR
    if app_open == "A1" or app_open == "a1" or app_open == "1":
        askforhome = False
        while 1 == 1:
            print("Calculator")
            print("Enter 2 numbers to see posible outcomes\n")
            #num1
            num1 = input("Enter the first number or press enter to leave: ")
            if num1 == "":
                break
            else:
                num1 = float(num1)
            #num2
            num2 = input("Enter the second number or press enter to leave: ")
            if num2 == "":
                break
            else:
                num2 = float(num2)
            print()
            print(str(num1) + " + " + str(num2) + " = " + str(num1+num2))
            print(str(num1) + " - " + str(num2) + " = " + str(num1-num2))
            print(str(num1) + " * " + str(num2) + " = " + str(num1*num2))
            print(str(num1) + " / " + str(num2) + " = " + str(num1/num2) + "\n")
            input("Press enter to continue ")
            LinePrint()
            #END OF CALCULATOR

    #GUESS NUM/WORD
    elif app_open == "A2" or app_open == "a2" or app_open == "2":
        print("Guess the Number/Word")
        print("This app requires 2 players\n")
        app_guessnumorword_type = input("Are you guessing a number or word: ")
        #NUMBER
        if app_guessnumorword_type == "number" or app_guessnumorword_type == "NUMBER" or app_guessnumorword_type == "num":
            print()
            app_guessnumorword_num = input("What is the maximum the number could be: ")
            app_guessnumorword_player1 = input("Pick your number on a scale of 1 to " + app_guessnumorword_num + ": ")
            while (int(app_guessnumorword_player1) < 1) or (int(app_guessnumorword_player1) > int(app_guessnumorword_num)):
                app_guessnumorword_player1 = input("Pick your number on a scale of 1 to " + app_guessnumorword_num + ": ")
            print("\n" * 100)
            app_guessnumorword_player2 = input("Player2, guess the number on a scale of 1 to " + app_guessnumorword_num + ": ")
            print()
            if app_guessnumorword_player1 == app_guessnumorword_player2:
                print("Congrats player2 you win!")
            elif app_guessnumorword_player1 != app_guessnumorword_player2:
                print("Sorry Player2 you lost. the number was " + app_guessnumorword_player1)
        #WORD
        elif app_guessnumorword_type == "word" or app_guessnumorword_type == "WORD" or app_guessnumorword_type == "Word":
            print()
            app_guessnumorword_player1 = input("Player1 enter a word: ")
            app_guessnumorword_player1_hint = input("Enter the hint: ")
            print("\n" * 100)
            print("Hint: " + app_guessnumorword_player1_hint)
            app_guessnumorword_player2 = input("Player2 enter a word: ")
            print()
            if app_guessnumorword_player1 == app_guessnumorword_player2:
                print("Congrats Player2 you win")
            elif app_guessnumorword_player1 != app_guessnumorword_player2:
                print("Sorry Player2 you lost. The word was " + app_guessnumorword_player1)
        else:
            print("Your input did not match an acceptable answer")
            #END OF GUESS NUM/WORD


    #ROCK PAPER SCI
    elif app_open == "A3" or app_open == "a3" or app_open == "3":
        print("Rock Paper Scissors")
        leave_rpc = input("This is a 2 player game. To start press enter. To leave enter LEAVE: ")
        if leave_rpc != "Leave" and leave_rpc != "LEAVE" and leave_rpc != "leave":
            print()
            app_rpc_player1 = input("Player1 enter rock, paper, or scissors. Your answer must be lowercase: ")
            while app_rpc_player1 != "rock" and app_rpc_player1 != "paper" and app_rpc_player1 != "scissors":
                app_rpc_player1 = input("Player1 enter rock, paper, or scissors. Your answer must be lowercase: ")
            print("\n" * 100)
            app_rpc_player2 = input("Player2 enter rock, paper, or scissors. Your answer must be lowercase: ")
            while app_rpc_player2 != "rock" and app_rpc_player2 != "paper" and app_rpc_player2 != "scissors":
                app_rpc_player2 = input("Player2 enter rock, paper, or scissors. Your answer must be lowercase: ")
            #check p1
            app_rpc_rock_beats_scissors = app_rpc_player1 == "rock" and app_rpc_player2 == "scissors"
            app_rpc_scissors_beats_paper = app_rpc_player1 == "scissors" and app_rpc_player2 == "paper"
            app_rpc_paper_beats_rock = app_rpc_player1 == "paper" and app_rpc_player2 == "rock"
            #check p2
            app_rpc_rock_beats_scissors2 = app_rpc_player2 == "rock" and app_rpc_player1 == "scissors"
            app_rpc_scissors_beats_paper2 = app_rpc_player2 == "scissors" and app_rpc_player1 == "paper"
            app_rpc_paper_beats_rock2 = app_rpc_player2 == "paper" and app_rpc_player1 == "rock"
            print("\n" * 100)
            if app_rpc_rock_beats_scissors or app_rpc_scissors_beats_paper or app_rpc_paper_beats_rock:
                print(app_rpc_player1 + " > " + app_rpc_player2)
                print("Player1 wins!\n")
            elif app_rpc_rock_beats_scissors2 or app_rpc_scissors_beats_paper2 or app_rpc_paper_beats_rock2:
                print(app_rpc_player1 + " < " + app_rpc_player2)
                print("Player2 wins!\n")
            elif app_rpc_player1 == app_rpc_player2:
                print(app_rpc_player1 + " = " + app_rpc_player2)
                print("Tie")
            else:
                print("Error")
        else:
            askforhome = False
        #END OF RPC

    #PASSWORD CREATOR
    elif app_open == "A4" or app_open == "a4" or app_open == "4":
        app_pass_choose = input("Enter 1 for a code. Enter 2 for a password. Or press enter to leave: ")
        if app_pass_choose == "1":
            app_pass_digits = int(input("How many digits long: "))
            app_pass_num = random.randint(int("9" * (app_pass_digits - 1)) + 1, int("9" * app_pass_digits))
            print("Code: " + str(app_pass_num))
        elif app_pass_choose == "2":
            app_pass_name = input("What is your name: ")
            app_pass_favnum = input("What is your favorite number: ")
            app_pass_wordrand = random.randint(100, 999)
            print("Your password can be: " + str(app_pass_wordrand) + app_pass_name + "?!" + app_pass_favnum)
        elif app_pass_choose == "":
            askforhome = False
        else:
            print("I didnt understand")
        #END OF PASSWORD CREATOR

    #TIMER
    elif app_open == "A5" or app_open == "a5" or app_open == "5":
        
        if pygame_installed:
            app_time_sec = input("Enter how many seconds will the timer be. Or press enter to leave: ")
            if app_time_sec == "":
                askforhome = False
            else:
                
                ticks_diff = int(app_time_sec) * 1000
                input("Starting timer when you press enter  ")
                print("Timer Started")
                
                time_per_unit = ticks_diff / 10
                time_at_unit = pygame.time.get_ticks()
                units = 1
                
                start_timer = pygame.time.get_ticks()
                print("#---------")
                while True:
                    if ticks_diff <= pygame.time.get_ticks() - start_timer:
                        break
                    if time_at_unit <= pygame.time.get_ticks() - time_per_unit:
                        LinePrint()
                        units += 1
                        print("#" * units, end="")
                        print("-" * (10-units))
                        time_at_unit = pygame.time.get_ticks()
                           
                print("Timer Ended")

        else:
            print("This app is disabled because the needed libraries are not installed. View settings for more info.")
        #END OF TIMER

    #Paintball
    elif app_open == "A6" or app_open == "a6" or app_open == "6":
        app_paint_heart1 = 3
        app_paint_heart2 = 3
        app_paint_break = False
        LinePrint()
        app_paint_player = input("To start the 2 player version enter 2. to start the 1 player version enter 1. To leave press enter: ")
        LinePrint()
        #2 player
        if app_paint_player == "2":
            print("Welcome to Paintball")
            print("Each player has 3 spots to hide")
            print("players choose where to hide each round and guess where the other player hid")
            print("The first to run out of hearts looses")
            print()
            input("press enter to start ")
            while 1 == 1:
                print("\n" * 100)
                print("Player 1 you have " + str(app_paint_heart1) + " hearts. Player 2 has " + str(app_paint_heart2) + " hearts")
                app_paint_spot1 = input("Player 1 will you hide in spot 1, 2, or 3: ")
                if app_paint_spot1 != "1" and app_paint_spot1 != "2" and app_paint_spot1 != "3":
                    print("Your spot was automaticly set to 1")
                    app_paint_spot1 = "1"
                app_paint_fire1 = input("Player 1 where will you shoot 1, 2, or 3: ")
                if app_paint_fire1 != "1" and app_paint_fire1 != "2" and app_paint_fire1 != "3":
                    print("You will fire at spot 1")
                    app_paint_fire1 = "1"
                input("Player 1 your turn has finished press enter to switch to player 2. Do not show your answers")
                print("\n" * 100)
                print("Player 2 you have " + str(app_paint_heart2) + " hearts. Player 1 has " + str(app_paint_heart1) + " hearts")
                app_paint_spot2 = input("Player 2 will you hide in spot 1, 2, or 3: ")
                if app_paint_spot2 != "1" and app_paint_spot2 != "2" and app_paint_spot2 != "3":
                    print("Your spot was automaticly set to 1")
                    app_paint_fire2 = "1"
                app_paint_fire2 = input("Player 2 where will you shoot 1, 2, or 3: ")
                if app_paint_fire2 != "1" and app_paint_fire2 != "2" and app_paint_fire2 != "3":
                    print("You will fire at spot 1")
                    app_paint_fire2 = "1"
                input("time for the results press enter and bring player 1")
                print("\n" * 100)
                print("RESULTS")
                print("Player 1 fired at spot " + app_paint_fire1)
                print("Player 1 hid in spot " + app_paint_spot1)
                print("Player 2 fired at spot " + app_paint_fire2)
                print("Player 2 hid in spot " + app_paint_spot2)
                if app_paint_fire1 == app_paint_spot2:
                    print("Player 1 shot Player 2")
                    app_paint_heart2 -= 1
                if app_paint_fire2 == app_paint_spot1:
                    print("Player 2 shot Player 1")
                    app_paint_heart1 -= 1
                if app_paint_heart1 <= 0 and app_paint_heart2 <= 0:
                    print("Player 1 and Player 2 both ran out of hearts")
                    print("There is no winner this time")
                    app_paint_break = True
                elif app_paint_heart1 <= 0:
                    print("Player 1 ran out of hearts")
                    print("Player 2 wins")
                    app_paint_break = True
                elif app_paint_heart2 <= 0:
                    print("Player 2 ran out of hearts")
                    print("Player 1 wins")
                    app_paint_break = True
                if app_paint_break:
                    break
                input("Press enter to continue")
        elif app_paint_player == "1":
            print("Welcome to Paintball")
            print("You have 3 spots to hide")
            print("You will choose where to hide each round and guess where the computer hid")
            print("The first to run out of hearts will loose")
            print()
            input("press enter to start")
            while 1 == 1:
                LinePrint()
                print("Player 1 you have " + str(app_paint_heart1) + " hearts. The computer has " + str(app_paint_heart2) + " hearts")
                app_paint_spot1 = input("Player 1 will you hide in spot 1, 2, or 3: ")
                if app_paint_spot1 != "1" and app_paint_spot1 != "2" and app_paint_spot1 != "3":
                    print("Your spot was automaticly set to 1")
                    app_paint_spot1 = "1"
                app_paint_fire1 = input("Player 1 where will you shoot 1, 2, or 3: ")
                if app_paint_fire1 != "1" and app_paint_fire1 != "2" and app_paint_fire1 != "3":
                    print("You will fire at spot 1")
                    app_paint_fire1 = "1"
                input("The computer finshed making decisions press enter to see the results")
                app_paint_spot2 = str(random.randint(1, 3))
                app_paint_fire2 = str(random.randint(1, 3))
                LinePrint()
                print("RESULTS")
                print("You fired at spot " + app_paint_fire1)
                print("You hid in spot " + app_paint_spot1)
                print("The computer fired at spot " + app_paint_fire2)
                print("The computer hid in spot " + app_paint_spot2)
                if app_paint_fire1 == app_paint_spot2:
                    print("you shot the computer")
                    app_paint_heart2 -= 1
                if app_paint_fire2 == app_paint_spot1:
                    print("the computer shot you")
                    app_paint_heart1 -= 1
                if app_paint_heart1 <= 0 and app_paint_heart2 <= 0:
                    print("You and the computer both ran out of hearts")
                    print("There is no winner this time")
                    app_paint_break = True
                elif app_paint_heart1 <= 0:
                    print("You ran out of hearts")
                    print("The computer wins")
                    app_paint_break = True
                elif app_paint_heart2 <= 0:
                    print("The computer ran out of hearts")
                    print("you win")
                    app_paint_break = True
                if app_paint_break:
                    break
                input("Press enter to continue")
        elif app_paint_player == "":
            askforhome = False
                #END OF PAINTBALL

    #TICTACTOE
    elif app_open == "A7" or app_open == "a7" or app_open == "7": #tictactoe
        print("Welcome to TicTacToe")
        ttt_action = input("This is a 2 player game. Press enter to continue or enter LEAVE to leave: ")
        if ttt_action == "LEAVE" or ttt_action == "leave" or ttt_action == "Leave":
            askforhome = False
        else:
            askforhome = True
            spot_1, spot_2, spot_3, spot_4, spot_5 = " ", " ", " ", " ", " "
            spot_6, spot_7, spot_8, spot_9 = " ", " ", " ", " "
            winner = " "
            x_turn = True
            skip_add = False
            while True:
                print("\n" * 100)
                print(" " + spot_1 + "|" + spot_2 + "|" + spot_3 + "   1|2|3")
                print(" " + spot_4 + "|" + spot_5 + "|" + spot_6 + "   4|5|6")
                print(" " + spot_7 + "|" + spot_8 + "|" + spot_9 + "   7|8|9")
                print()

                if winner == "X":
                    print("X Wins!")
                    break
                if winner == "O":
                    print("O Wins!")
                    break
                if winner == "Tie":
                    print("Tie!")
                    break

                if x_turn:
                    player = "x"
                else:
                    player = "o"

                if x_turn:
                    number = 0
                    while number < 1 or number > 9:
                        number = int(input("Player X what number are you going in: "))
                if not x_turn:
                    number = 0
                    while number < 1 or number > 9:
                        number = int(input("Player O what number are you going in: "))

                if number == 1 and spot_1 != " ":
                    x_turn = not x_turn
                    skip_add = True
                if number == 2 and spot_2 != " ":
                    x_turn = not x_turn
                    skip_add = True
                if number == 3 and spot_3 != " ":
                    x_turn = not x_turn
                    skip_add = True
                if number == 4 and spot_4 != " ":
                    x_turn = not x_turn
                    skip_add = True
                if number == 5 and spot_5 != " ":
                    x_turn = not x_turn
                    skip_add = True
                if number == 6 and spot_6 != " ":
                    x_turn = not x_turn
                    skip_add = True
                if number == 7 and spot_7 != " ":
                    x_turn = not x_turn
                    skip_add = True
                if number == 8 and spot_8 != " ":
                    x_turn = not x_turn
                    skip_add = True
                if number == 9 and spot_9 != " ":
                    x_turn = not x_turn
                    skip_add = True

                if skip_add == False:
                    if number == 1:
                        spot_1 = player
                    elif number == 2:
                        spot_2 = player
                    elif number == 3:
                        spot_3 = player
                    elif number == 4:
                        spot_4 = player
                    elif number == 5:
                        spot_5 = player
                    elif number == 6:
                        spot_6 = player
                    elif number == 7:
                        spot_7 = player
                    elif number == 8:
                        spot_8 = player
                    elif number == 9:
                        spot_9 = player
                skip_add = False

                if (spot_1 == "x" and spot_2 == "x" and spot_3 == "x") or (spot_4 == "x" and spot_5 == "x" and spot_6 == "x") or (spot_7 == "x" and spot_8 == "x" and spot_9 == "x"):
                    winner = "X"
                if (spot_1 == "x" and spot_4 == "x" and spot_7 == "x") or (spot_2 == "x" and spot_5 == "x" and spot_8 == "x") or (spot_3 == "x" and spot_6 == "x" and spot_9 == "x"):
                    winner = "X"
                if (spot_1 == "x" and spot_5 == "x" and spot_9 == "x") or (spot_3 == "x" and spot_5 == "x" and spot_7 == "x"):
                    winner = "X"

                if (spot_1 == "o" and spot_2 == "o" and spot_3 == "o") or (spot_4 == "o" and spot_5 == "o" and spot_6 == "o") or (spot_7 == "o" and spot_8 == "o" and spot_9 == "o"):
                    winner = "O"
                if (spot_1 == "o" and spot_4 == "o" and spot_7 == "o") or (spot_2 == "o" and spot_5 == "o" and spot_8 == "o") or (spot_3 == "o" and spot_6 == "o" and spot_9 == "o"):
                    winner = "O"
                if (spot_1 == "o" and spot_5 == "o" and spot_9 == "o") or (spot_3 == "o" and spot_5 == "o" and spot_7 == "o"):
                    winner = "O"

                if (spot_1 != " " and spot_2 != " " and spot_3 != " " and spot_4 != " " and spot_5 != " " and spot_6 != " " and spot_7 != " " and spot_8 != " " and spot_9 != " "):
                    if winner != "X" and winner != "O":
                        winner = "Tie"

                x_turn = not x_turn
        #END OF TICTACTOE

    #Match
    elif app_open == "A8" or app_open == "a8" or app_open == "8": #FINISH TESTING AT CARDS HIDDEN
        print("Match")
        start = input("Press enter to start or enter LEAVE to leave: ")
        if pygame_installed:
            start_time = pygame.time.get_ticks()
            recording_time = True
        else:
            recording_time = False
        if start != "leave" and start != "LEAVE" and start != "Leave":
        
            cl = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            random.shuffle(cl)
            row1 = [cl[0], cl[1], cl[2], cl[3], cl[4], cl[5]]
            row2 = [cl[6], cl[7], cl[8], cl[9], cl[10], cl[11]]
            row3 = [cl[12], cl[13], cl[14], cl[15], cl[16], cl[17]]
            row4 = [cl[18], cl[19], cl[20], cl[21], cl[22], cl[23]]
            
            display1 = [False, False, False, False, False, False]
            display2 = [False, False, False, False, False, False]
            display3 = [False, False, False, False, False, False]
            display4 = [False, False, False, False, False, False]
    
            found1 = [False, False, False, False, False, False]
            found2 = [False, False, False, False, False, False]
            found3 = [False, False, False, False, False, False]
            found4 = [False, False, False, False, False, False]
                    
            cards_displayed = 0    
            matches = 0
            seen1 = 999 #must be diff nums than seen2 and not possible in game
            seen2 = 888
            
            while True:
                
                print("\n" * 100)
                
                if matches >= 12:
                    print("ALL CARDS FOUND")
                    if recording_time:
                        time_used = (pygame.time.get_ticks() - start_time) / 1000
                        print("Time: " + str(time_used) + " Seconds")
                    else:
                        print("Time was not recorded because pygame is not installed. View settings for more info")
                    break
                
                print("   1  2  3  4  5  6")
                print("   -- -- -- -- -- --")
                index = 0
                while index < 6: #ROW1
                    if index == 0:
                        print("1| ", end="")
                    if not display1[index]:
                        print("[] ", end="")
                    else:
                        if found1[index]:
                            print("   ", end="")
                        else:
                            if len(str(row1[index])) == 1:
                                print(str(row1[index]) + "  ", end="")
                            else:
                                print(str(row1[index]) + " ", end="")
                    index += 1
                print()
                index = 0
                while index < 6: #ROW2
                    if index == 0:
                        print("2| ", end="")
                    if not display2[index]:
                        print("[] ", end="")
                    else: 
                        if found2[index]:
                            print("   ", end="")
                        else:
                            if len(str(row2[index])) == 1:
                                print(str(row2[index]) + "  ", end="")
                            else:
                                print(str(row2[index]) + " ", end="")
                    index += 1
                print()
                index = 0
                while index < 6: #ROW3
                    if index == 0:
                        print("3| ", end="")
                    if not display3[index]:
                        print("[] ", end="")
                    else:  
                        if found3[index]:
                            print("   ", end="")
                        else:
                            if len(str(row3[index])) == 1:
                                print(str(row3[index]) + "  ", end="")
                            else:
                                print(str(row3[index]) + " ", end="")
                    index += 1
                print()
                index = 0
                while index < 6: #ROW4
                    if index == 0:
                        print("4| ", end="")
                    if not display4[index]:
                        print("[] ", end="")
                    else:  
                        if found4[index]:
                            print("   ", end="")
                        else:
                            if len(str(row4[index])) == 1:
                                print(str(row4[index]) + "  ", end="")
                            else:
                                print(str(row4[index]) + " ", end="")
                    index += 1
                    
                print("\n" * 2)
                
                if cards_displayed == 2:
                    
                    if seen1 == seen2:
                        matches += 1
                        index = 0
                        while index <= 5:
                            if row1[index] == seen1:
                                found1[index] = True
                            index += 1
                        index = 0
                        while index <= 5:
                            if row2[index] == seen1:
                                found2[index] = True
                            index += 1
                        index = 0
                        while index <= 5:
                            if row3[index] == seen1:
                                found3[index] = True
                            index += 1
                        index = 0
                        while index <= 5:
                            if row4[index] == seen1:
                                found4[index] = True
                            index += 1
    
                    index = 0
                    while index <= 5:
                        if found1[index]:
                            display1[index] = True
                            row1[index] = 999
                        else:
                            display1[index] = False
                        if found2[index]:
                            display2[index] = True
                            row2[index] = 999
                        else:
                            display2[index] = False
                        if found3[index]:
                            row3[index] = 999
                            display3[index] = True
                        else:
                            display3[index] = False
                        if found4[index]:
                            row4[index] = 999
                            display4[index] = True
                        else:
                            display4[index] = False
                        index += 1
    
    
                    if matches >= 1:
                        print(("[" * (matches * 2)) + "]")
                    print("Matches: " + str(matches))
                    input("Press continue ")
                    cards_displayed = 0
                    
                else:
                    if matches >= 1:
                        print(("[" * (matches*2)) + "]")
                    print("Matches: " + str(matches))
                    row = int(input("Enter a number (left and right): "))
                    while row < 1 or row > 6:
                        row = int(input("Enter a number (left and right): "))
                    column = int(input("Enter a number (up and down): "))
                    while column < 1 or column > 4:
                        column = int(input("Enter a number (up and down): "))
                        
                    if column == 1 and found1[row-1]:
                        row = int(input("Card not found. Enter a new number (left and right): "))
                        column = int(input("Enter a number (up and down): "))
                    elif column == 2 and found2[row-1]:
                        row = int(input("Card not found. Enter a new number (left and right): "))
                        column = int(input("Enter a number (up and down): "))
                    elif column == 3 and found3[row-1]:
                        row = int(input("Card not found. Enter a new number (left and right): "))
                        column = int(input("Enter a number (up and down): "))
                    elif column == 4 and found4[row-1]:
                        row = int(input("Card not found. Enter a new number (left and right): "))
                        column = int(input("Enter a number (up and down): "))
                            
                
                    cards_displayed += 1
                    
                    if column == 1:
                        display1[row-1] = True
                        if cards_displayed == 1:
                            seen1 = row1[row-1]
                        elif cards_displayed == 2:
                            seen2 = row1[row-1]
                    elif column == 2:
                        display2[row-1] = True
                        if cards_displayed == 1:
                            seen1 = row2[row-1]
                        elif cards_displayed == 2:
                            seen2 = row2[row-1]
                    elif column == 3:
                        display3[row-1] = True
                        if cards_displayed == 1:
                            seen1 = row3[row-1]
                        elif cards_displayed == 2:
                            seen2 = row3[row-1]
                    elif column == 4:
                        display4[row-1] = True
                        if cards_displayed == 1:
                            seen1 = row4[row-1]
                        elif cards_displayed == 2:
                            seen2 = row4[row-1]
        else:
            askforhome = False

    #note
    elif app_open == "A9" or app_open == "a9" or app_open == "9":
        note_file = read_line(5)
        if note_file != "":
            print("You have a note written down:")
            print(note_file)
            print()
        elif note_file == "":
            print("You dont have a note")
        change_note = input("Enter text to change it, enter REMOVE to clear the note, and press enter to go back: ")
        if change_note != "" and change_note != "remove" and change_note != "REMOVE":
            write_line(5, change_note)
            input("Note changed press enter to go back")
        if change_note == "REMOVE" or change_note == "remove":
            write_line(5, "")
        askforhome = False
    #end of notes

    #reminders
    elif app_open == "A10" or app_open == "a10" or app_open == "10":
        while True:
            reminders = open("PhoenixOS_Reminders.txt", "r")
            reminders = reminders.read()
            if reminders != "":
                print("Here are your reminders:")
            print(reminders)
            print()
            add_reminders = input("Enter text to add a reminder, enter REMOVE to remove a reminder or press enter to go home: ")
            if add_reminders == "":
                askforhome = False
                break
            elif add_reminders != "" and add_reminders != "REMOVE" and add_reminders != "remove":
                if reminders != "":
                    append_reminders = open("PhoenixOS_Reminders.txt", "a")
                    append_reminders.write("\n")
                    append_reminders.close()
                append_reminders = open("PhoenixOS_Reminders.txt", "a")
                append_reminders.write(add_reminders)
                append_reminders.close()
                askforhome = False
            elif add_reminders == "REMOVE" or add_reminders == "remove":
                remove_reminders = input("Enter the reminders line number: ")
                old_reminders = open("PhoenixOS_Reminders.txt", "r")
                old_reminders = old_reminders.read()
                line = int(remove_reminders)
                text = ""
                file = open("PhoenixOS_Reminders.txt", "r")
                file = file.readlines()
                file[line-1] = text + ""
                old_file = open("PhoenixOS_Reminders.txt", "w")
                old_file.writelines(file)
                old_file.close()
                result = ""
                with open("./PhoenixOS_Reminders.txt", "r") as file:
                    for line in file:
                        if not line.isspace():
                            result += line
                reminders = open("PhoenixOS_Reminders.txt", "w")
                reminders.write(result)
                reminders.close()
                askforhome = False
            LinePrint()
        #END OF REMINDERS

    #contacts
    elif app_open == "A11" or app_open == "a11" or app_open == "11":
        while True:
            contacts_file = open("PhoenixOS_Contacts.txt", "r")
            contacts_file = contacts_file.read()
            if contacts_file != "":
                print("Here are your contacts:")
            print(contacts_file)
            print()
            name_add = input("Enter a name to make a new contact. enter ERASE to remove a contact. or press enter to exit: ")

            if name_add != "" and name_add != "ERASE" and name_add != "erase":
                email_add = input("Enter the email or press enter if you dont have one: ")
                phone_add = input("Enter the phone number or press enter if you dont have one: ")
                if email_add != "" and phone_add != "":
                    contact_add = (name_add + ", " + email_add + ", " + phone_add)
                if email_add != "" and phone_add == "":
                    contact_add = (name_add + ", " + email_add)
                if email_add == "" and phone_add != "":
                    contact_add = (name_add + ", " + phone_add)
                if email_add == "" and phone_add == "":
                    contact_add = name_add
                if contacts_file != "":
                    contacts_file = open("PhoenixOS_Contacts.txt", "a")
                    contacts_file = contacts_file.write("\n")
                contacts_file = open("PhoenixOS_Contacts.txt", "a")
                contacts_file = contacts_file.write(contact_add)
                input("Added. press enter to go back")
                LinePrint()

            elif name_add == "ERASE" or name_add == "erase":
                erase_contact = input("Enter the line number the contact is on. or press enter to cancel: ")
                if erase_contact != "":
                    old_contacts = open("PhoenixOS_Contacts.txt", "r")
                    old_contacts = old_contacts.read()
                    line = int(erase_contact)
                    text = ""
                    file = open("PhoenixOS_Contacts.txt", "r")
                    file = file.readlines()
                    file[line-1] = text + ""
                    old_file = open("PhoenixOS_Contacts.txt", "w")
                    old_file.writelines(file)
                    old_file.close()
                    result = ""
                    with open("./PhoenixOS_Contacts.txt", "r") as file:
                        for line in file:
                            if not line.isspace():
                                result += line
                    contacts = open("PhoenixOS_Contacts.txt", "w")
                    contacts.write(result)
                    contacts.close()
                LinePrint()

            else:
                askforhome = False
                break
            #END OF CONTACTS
    
    elif app_open == "A12" or app_open == "a12" or app_open == "12":
        askforhome = False
        if not pygame_installed:
            input("This app requires a missing library. View settings for more info. Press enter to go home ")
        else:
            print("Music Player (Beta)")
            print("Supported file types: WAV MP3 OGG\n")
            print("Loaded file: " + loaded_music_file)
            print()
            if loaded_music_file == "":
                loaded_music_file = input("Enter your music's file path: ")
                sound = pygame.mixer.Sound(loaded_music_file)
                sound.play()
                music_end_time = pygame.time.get_ticks() + (sound.get_length() * 1000)
            elif pygame.time.get_ticks() < music_end_time:
                end_action = input("Enter STOP to end your music. Enter a file path to play that audio or press enter to leave: ")
                if end_action == "STOP" or end_action == "Stop" or end_action == "stop":
                    sound.stop()
                    music_end_time = 0
                elif end_action == "":
                    1 == 1
                else:
                    sound.stop()
                    loaded_music_file = end_action
                    sound = pygame.mixer.Sound(loaded_music_file)
                    sound.play()
                    music_end_time = pygame.time.get_ticks() + (sound.get_length() * 1000)
            else:
                play_action = input("Enter PLAY to play your music. Enter a file path to change audio or press enter to leave: ")
                if play_action == "PLAY" or play_action == "play" or play_action == "Play":
                    sound.play()
                    music_end_time = pygame.time.get_ticks() + (sound.get_length() * 1000)
                elif play_action == "":
                    1 == 1
                else:
                    sound.stop()
                    loaded_music_file = play_action
                    sound = pygame.mixer.Sound(loaded_music_file)
                    sound.play()
                    music_end_time = pygame.time.get_ticks() + (sound.get_length() * 1000)
    #ENCRYPTION
    elif app_open == "A13" or app_open == "a13" or app_open == "13":

        # This function gets a number at index from key
        def get_letter_at_index(input_string, index):
            if 0 <= index < len(input_string):
                return input_string[index]
            else:
                return "Index out of range"
        # This function gets a number from the encrypted data
        def get_num_from_en(text, index):
            numbers = text.split('-')
            if 0 <= index < len(numbers) and numbers[index] != '':
                return int(numbers[index])
            else:
                return "Index out of range"
        def encrypt(unencrypted):
            index = 0
            key = ""
            encrypted = ""
            while True:
                letter = get_letter_at_index(unencrypted, index)
                if letter == "Index out of range":
                    break
                ascii_value = ord(letter)
                key_new_num = random.randint(1, 9)
                key += str(key_new_num)
                encrypted = encrypted + str(ascii_value + key_new_num) + "-"
                index += 1
            return encrypted, key
        def decrypt(encrypted, key_input):
            key = [int(k) for k in key_input]  # Convert each character to an integer
            index = 0
            unencrypted = ""
            while True:
                encrypted_value = get_num_from_en(encrypted, index)
                if encrypted_value == "Index out of range":
                    break
                decrypted_ascii = encrypted_value - key[index]
                unencrypted += chr(decrypted_ascii) # Convert decrypted ASCII value to character and append to the result
                index += 1
            return unencrypted

        while True:
            print("Welcome to Encryption")
            print("To use this app enter text you would like to encrypt. You will then be given encrypted text and an encryption key.")
            print("This key will be required to decrypt your text later. Text and keys are not saved or sent to any servers so make sure to store your data.\n")
            encrypt_or_decrypt = input("Enter encrypt to encrypt your text. Enter decrypt to decrypt your text. Or press enter to leave: ")

            if encrypt_or_decrypt == "":
                askforhome = False
                break

            elif encrypt_or_decrypt == "encrypt" or encrypt_or_decrypt == "Encrypt":
                to_encrypt = input("Enter the text you would like to encrypt: ")
                encrypted_text, key = encrypt(to_encrypt)
                print("\nHere is your encrypted text: " + encrypted_text)
                print("Here is your key: " + key)
                print()
                input("Press enter to return to the menu ")
                LinePrint()

            elif encrypt_or_decrypt == "decrypt" or encrypt_or_decrypt == "Decrypted":
                encrypted = input("Enter the encrypted text: ")
                key = input("Enter the key that matches with your text: ")
                decrypted_text = decrypt(encrypted, key)
                print("\nHere is your decrypted text: " + decrypted_text)
                print()
                input("Press enter to return to the menu ")
                LinePrint()

            else:
                input("Unrecognized input. Please respond with encrypt or decrypt. Press enter to return")
                LinePrint()
            #END OF ENCRYPTION

    #SETTINGS
    elif app_open == "A14" or app_open == "a14" or app_open == "14":
        settings_lock = True
        while settings_lock:
            login = read_line(3)
            note_home = read_line(6)
            home_reminders = read_line(4)
            if Line_amount == 100:
                reduce_blank_status = "OFF"
            elif Line_amount == 10:
                reduce_blank_status = "ON"
            LinePrint()
            print("Settings\n")
            print("1. About")
            print("2. Reduce Blanks: " + reduce_blank_status)
            print("3. Show note on home: " + note_home)
            print("4. Show reminders on home: " + home_reminders)
            print("5. Require login on start: " + login)
            print("6. Change name")
            print("7. Change password")
            print("8. Manage downloaded librarys")
            print("9. Custom Apps")
            print("10. Factory reset")
            print()
            Setting_num = input("Enter a setting number or press enter to leave: ")
            LinePrint()
            #DISABLE RETURN LOOP
            if Setting_num == "":
                settings_lock = False
            #EXTRA
            if Setting_num == "dev":
                print("Extra information. Settings in this menu are not designed to be needed.")
                print("This menu is accessed by typing dev in settings")
                print()
                print("1. Read Save Files")
                print("2. Write Save Files")
                print("3. Run commands on start")
                dev_settings = input("Enter: ")
                if dev_settings == "1":
                    LinePrint()
                    file = open("PhoenixOS_5_3_Save.txt")
                    text = file.read()
                    file2 = open("PhoenixOS_Reminders.txt")
                    text2 = file2.read()
                    file3 = open("PhoenixOS_Contacts.txt")
                    text3 = file3.read()
                    print("PhoenixOS_5_3_Save.txt")
                    print("---")
                    print(text)
                    print("---\n")
                    print("PhoenixOS_Reminders.txt")
                    print("---")
                    print(text2)
                    print("---\n")
                    print("PhoenixOS_Contacts.txt")
                    print("---")
                    print(text3)
                    print("---")
                    file_name = input("Press enter to leave or enter a file name to read: ")
                    if file_name != "":
                        LinePrint()
                        file = open(file_name)
                        text = file.read()
                        print(file_name)
                        print("---\n" + text + "\n---")
                        input("Press enter ")
                if dev_settings == "2":
                    LinePrint()
                    print("System Files: PhoenixOS_5_3_Save.txt, PhoenixOS_Contacts.txt, PhoenixOS_Reminders.txt")
                    file_name = input("File Name: ")
                    print()
                    file = open(file_name)
                    text = file.read()
                    print(file_name)
                    print("---")
                    print(text)
                    print("---\n")
                    to_write = input("Enter text to write to the file: ")
                    file = open(file_name, "w")
                    file.write(to_write)
                    file.close()
                if dev_settings == "3":
                    start_line = read_line(8)
                    if start_line == "NONE":
                        start_line = ""
                    LinePrint()
                    print("This will run a command on start in the terminal using os.system()")
                    print("Current command: " + start_line)
                    start_line = input("Enter a command to have run on start, Enter ERASE to remove the command or press enter to leave: ")
                    if start_line == "ERASE" or start_line == "erase" or start_line == "Erase":
                        write_line(8, "NONE")
                    elif start_line == "":
                        1 == 1
                    else:
                        write_line(8, start_line)
    
            #ABOUT
            if Setting_num == "1":
                print("Coded in python by Phoenix")
                print("System version: " + str(sys_os_version))
                print()
                input("Press enter to go back")
            #toggle lines
            elif Setting_num == "2":
                if Line_amount == 10:
                    Line_amount = 100
                elif Line_amount == 100:
                    Line_amount = 10
                write_line(7, str(Line_amount))
            #note on home
            elif Setting_num == "3":
                if note_home == "ON":
                    write_line(6, "OFF")
                elif note_home == "OFF":
                    write_line(6, "ON")

            #reminders on home
            elif Setting_num == "4":
                if home_reminders == "ON":
                    write_line(4, "OFF")
                elif home_reminders == "OFF":
                    write_line(4, "ON")

            #login on start
            elif Setting_num == "5":
                pass_attempt = input("Enter your password: ")
                if pass_attempt == password:
                    if login == "ON":
                        write_line(3, "OFF")
                    elif login == "OFF":
                        write_line(3, "ON")
                else:
                    input("Verification failed. press enter to go back")

            #name change
            elif Setting_num == "6":
                pass_guess = input("Enter your password to change your name: ")
                if pass_guess == password:
                    new_name = input("Enter a new name: ")
                    write_line(1, new_name)
                    name = read_line(1)
                else:
                    input("password verification failed press enter to go back")
            #password change
            elif Setting_num == "7":
                pass_guess = input("Enter your current password: ")
                if pass_guess == password:
                    new_pass = input("Enter a new password: ")
                    write_line(2, new_pass)
                    password = read_line(2)
                else:
                    input("password verification failed press enter to go back")
                print("password")

            #manage librays
            elif Setting_num == "8":
                if pygame_installed:
                    print("Pygame: Installed")
                    input("Press enter to return to settings ")
                else:
                    print("Pygame: Uninstalled")
                    install_pygame = input("Press enter to return to settings, Enter INSTALL to install pygame: ")
                    if install_pygame == "INSTALL" or install_pygame == "install" or install_pygame == "Install":
                        print()
                        os.system("pip install pygame")
                        time.sleep(2)
                        try:
                            import pygame
                            pygame.init()
                            pygame_installed = True
                        except ImportError as e:
                            pygame_installed = False
                            print("Error. Try again later.")
                            print("You may want to try to manually install pygame using (pip install pygame) in your terminal for more information.")
                            input("Press enter to return ")

            #custom apps
            elif Setting_num == "9":
                if not custom_app:
                    print("No custom apps were found.")
                else:
                    print("Custom App Found")
                    print()
                    print("Name: " + PhoenixOS_App.Name())
                    print("Version: " + str(PhoenixOS_App.Version()))
                    print("Dev: " + PhoenixOS_App.Dev())
                    print()

                app_info = input("To return to settings press enter. For more info on custom apps enter INFO: ")
                if app_info == "info" or app_info == "INFO" or app_info == "Info":
                    LinePrint()
                    print("Custom apps are apps that can be made through other developers and can be ran through PhoenixOS")
                    print("For PhoenixOS to run a custom app (Python code) your .py file must be named PhoenixOS_App.py")
                    print("Your code must also have these functions:")
                    print()
                    print("Main() - This is the main code for your app")
                    print("Name() - This returns your app name when called")
                    print("Version() - This returns your app version when called")
                    print("Dev() - This returns the developers name / organization when called")
                    print()
                    print("If your app is not detected try running your code or making sure it is in the same directory as PhoenixOS\n")
                    input("Press enter to return to settings ")


            #factory reset
            elif Setting_num == "10":
                print("This will reset all user data")
                print("once reset finishes you can open PhoenixOS with a fresh start")
                reset_pass = input("enter your password to confirm a factory reset: ")
                if reset_pass == password:
                    default_save = "NONE\nNONE\nON\nON\n\nON\n100\nNONE"
                    contacts_write = open("PhoenixOS_5_3_Save.txt", "w")
                    contacts_write.write(default_save)
                    contacts_write.close()
                    contacts_write = open("PhoenixOS_Contacts.txt", "w")
                    contacts_write.write("")
                    contacts_write.close()
                    rem_write = open("PhoenixOS_Reminders.txt", "w")
                    rem_write.write("")
                    rem_write.close()
                    print("RESET COMPLETE")
                    sys.exit()
                else:
                    print("password verification failed")
                    input("press enter to go back")
            askforhome = False
    #END OF SETTINGS

    #CUSTOM APP
    elif app_open == "A15" or app_open == "a15" or app_open == "15":
        if custom_app:
            PhoenixOS_App.Main()
            askforhome = False
        else:
            print("The application was unable to launch. " + app_open + " could not be found")

    #Shutdown
    elif app_open == "" or app_open == " ":
        break

    #terminal
    elif app_open[0] == "*":
        first_letter_index = 1
        new_command = ""
        while first_letter_index < len(app_open):
            new_command += app_open[first_letter_index]
            first_letter_index += 1

        print("Running command (" + new_command + ") In the terminal\n------")
        os.system(new_command)
        terminal_input = input("------\nRun complete. Press enter to go home or enter HELP for more info: ")
        if terminal_input == "HELP" or terminal_input == "help" or terminal_input == "Help":
            LinePrint()
            print("Terminal commands in PhoenixOS")
            print("-----------------------------------------")
            print("To run a terminal command in PhoenixOS from the home")
            print("screen enter * then your command")
            print("Commands are run using os.system() in python")
            input("Press enter to go home")
        askforhome = False

    #UNFOUND PROGRAM
    else:
        print("The application was unable to launch. " + app_open + " could not be found")

    if askforhome == True:
        input("Press enter to return home")
    askforhome = True
    LinePrint()

#on shutdown
LinePrint()
print("Closing PhoenixOS")
