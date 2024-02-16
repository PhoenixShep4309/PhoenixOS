
"""PhoenixOS"""

#Variable Setup
import random
import sys
import time
import os

sys_os_version = 3.8
askforhome = True
PhoenixOS_power = True
first_time = False
print("\n" * 100)
#Variable Setup End

#Find save file
file = os.path.isfile("PhoenixOS_Save.txt")
file2 = os.path.isfile("PhoenixOS_Contacts.txt")
file3 = os.path.isfile("PhoenixOS_Reminders.txt")
if file == False or file2 == False or file3 == False:
    print("\n" * 100)
    missing = input("Save file not found. Press enter to create a save file in the current directory or enter QUIT to exit: ")
    if missing == "QUIT" or missing == "quit" or missing == "Quit":
        print("Closing PhoenixOS")
        sys.exit()
    else: #create save file
        file = open("PhoenixOS_Save.txt", "w")
        file.write("NONE\nNONE\nON\nON\n\nON\n100\nFALSE")
        file.close()
        file = open("PhoenixOS_Reminders.txt", "w")
        file.write("")
        file.close()
        file = open("PhoenixOS_Contacts.txt", "w")
        file.write("")
        file.close()
        input("Save file ready. Press enter to continue ")
        print("\n" * 100)

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
    file = open("PhoenixOS_Save.txt", "r")
    file = file.readlines()
    text = file[line-1]
    text = text.replace("\n", "")
    return text

def write_line(line, text):
    file = open("PhoenixOS_Save.txt", "r")
    file = file.readlines()
    file[line-1] = text + "\n"
    old_file = open("PhoenixOS_Save.txt", "w")
    old_file.writelines(file)
    old_file.close()
    
pygame_installed = read_line(8)
if pygame_installed == "TRUE":
    import pygame
    pygame.init()
    print("\n" * 100)

#check line amount
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
    
    pygame_installed = read_line(8)
    
    while pygame_installed != "TRUE":
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
            import pygame
            pygame.init()
            write_line(8, "TRUE")
            print("\n" * 100)
            pygame_installed = "TRUE"
        if package_action == "SKIP" or package_action == "skip":
            write_line(8, "FALSE")
            break
            
    
    print()
    print("Setup Complete")
    input("Press enter to open PhoenixOS")
    LinePrint()
    print("Welcome to the home screen. Enter a code on the left of the app to open it. this message will not show up again")
    print("----------")
    print()
    print()

login = read_line(3)
if login == "ON" and first_time == False:
    print("Welcome back " + name)
    pass_guess = input("Enter your password to begin: ")
    while pass_guess != password:
        pass_guess = input("Try again: ")
    LinePrint()

while PhoenixOS_power: #Home
    #Display Home
    print(name)
    print(DateAndTime())
    print()
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

    print("1 - Calculator")
    print("2 - Guess The Num/Word")
    print("3 - Rock Paper Scissors")
    print("4 - Password Generator")
    print("5 - Timer")
    print("6 - Paintball")
    print("7 - TicTacToe")
    print("8 - Note")
    print("9 - Reminders")
    print("10 - Contacts")
    print("11 - Settings")
    print("off - Shutdown")
    app_open = input("Enter the code on the left of the app you want to open: ")
    LinePrint()
    #Display Home End


    #CALCULATOR START
    if app_open == "A1" or app_open == "a1" or app_open == "1":
        askforhome = False
        while 1 == 1:
            #num1
            num1 = input("Enter the first number or press enter to leave: ")
            if num1 == "":
                break
            else:
                num1 = float(num1)
            #symbol
            symbol = input("Enter one of the following symbols ( + - / * ) or press enter to leave: ")
            if symbol == "":
                break
            #num2
            num2 = input("Enter the second number or press enter to leave: ")
            if num2 == "":
                break
            else:
                num2 = float(num2)
            #plus
            if symbol == "+":
                result = (num1 + num2)
            #minus
            if symbol == "-":
                result = (num1 - num2)
            #division
            if symbol == "/":
                result = (num1 / num2)
            #multiplication
            if symbol == "*":
                result = (num1 * num2)
            print()
            calc_end = input("Here is the result: " + str(result) + "  Press enter to start again or enter QUIT to leave: ")
            if calc_end == "QUIT" or calc_end == "quit":
                break
            else:
                LinePrint()
            #END OF CALCULATOR


    #GUESS NUM/WORD
    elif app_open == "A2" or app_open == "a2" or app_open == "2":
        print("this app requires 2 players")
        app_guessnumorword_type = input("Are you guessing a number or word? ")
        #NUMBER
        if app_guessnumorword_type == "number" or app_guessnumorword_type == "NUMBER" or app_guessnumorword_type == "num":
            print()
            app_guessnumorword_num = input("what is the maximum the number could be: ")
            app_guessnumorword_player1 = input("pick your number on a scale of 1 to " + app_guessnumorword_num + ": ")
            print("\n" * 100)
            app_guessnumorword_player2 = input("Player2, guess the number on a scale of 1 to " + app_guessnumorword_num + ": ")
            print()
            if app_guessnumorword_player1 == app_guessnumorword_player2:
                print("Congrats player2 you win!")
            elif app_guessnumorword_player1 != app_guessnumorword_player2:
                print("Sorry player2 you lost. the number was " + app_guessnumorword_player1)
        #WORD
        elif app_guessnumorword_type == "word" or app_guessnumorword_type == "WORD" or app_guessnumorword_type == "Word":
            print()
            app_guessnumorword_player1 = input("Enter a word: ")
            app_guessnumorword_player1_hint = input("Enter the hint: ")
            print("\n" * 100)
            print("Hint: " + app_guessnumorword_player1_hint)
            app_guessnumorword_player2 = input("player2 enter a word: ")
            print()
            if app_guessnumorword_player1 == app_guessnumorword_player2:
                print("congrats player2 you win")
            elif app_guessnumorword_player1 != app_guessnumorword_player2:
                print("sorry player2 you lost. The word was " + app_guessnumorword_player1)
        else:
            print("that is not a choice")
            #END OF GUESS NUM/WORD


    #ROCK PAPER SCI
    elif app_open == "A3" or app_open == "a3" or app_open == "3":
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
    elif app_open == "A4" or app_open == "a4" or app_open == "4":
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
            print("I didnt understand")

    #TIMER
    elif app_open == "A5" or app_open == "a5" or app_open == "5":
        pygame_installed = read_line(8)
        if pygame_installed == "TRUE":
            app_time_sec = int(input("How many seconds will the timer be: "))
            input("Starting timer when you press enter  ")
            app_time_sec *= 1000
            print("Timer Started")
            pygame.time.wait(app_time_sec)
            print("Timer Ended")

        else:
            print("This app is disabled because the needed files were not installed during setup")
    
    #Paintball
    elif app_open == "A6" or app_open == "a6" or app_open == "6":
        app_paint_heart1 = 3
        app_paint_heart2 = 3
        app_paint_break = False
        LinePrint()
        app_paint_player = input("To start the 2 player version enter 2. to start the 1 player version enter 1")
        LinePrint()
        #2 player
        if app_paint_player == "2":
            print("Welcome to paintball")
            print("Each player has 3 spots to hide")
            print("players choose where to hide each round and guess where the other player hid")
            print("The first to run out of hearts will loose")
            input("press enter to start")
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
            print("Welcome to paintball")
            print("You have 3 spots to hide")
            print("You will choose where to hide each round and guess where the computer hid")
            print("The first to run out of hearts will loose")
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
                    #end of 1 player paintball
                    
    elif app_open == "A7" or app_open == "a7" or app_open == "7": #tictactoe
        print("Welcome to TicTacToe")
        ttt_action = input("This is a 2 player game. Press enter to continue or enter LEAVE to leave: ")
        if ttt_action == "LEAVE" or ttt_action == "leave" or ttt_action == "Leave":
            askforhome = False
        else:
            askforhome = True
            spot_1 = " "
            spot_2 = " "
            spot_3 = " "
            spot_4 = " "
            spot_5 = " "
            spot_6 = " "
            spot_7 = " "
            spot_8 = " "
            spot_9 = " "
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
          
    #note
    elif app_open == "A8" or app_open == "a8" or app_open == "8":
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
    elif app_open == "A9" or app_open == "a9" or app_open == "9":
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

    #contacts
    elif app_open == "A10" or app_open == "a10" or app_open == "10":
        contacts_file = open("PhoenixOS_Contacts.txt", "r")
        contacts_file = contacts_file.read()
        if contacts_file != "":
            print("Heres your contacts:")
        print(contacts_file)
        print()
        name_add = input("Enter a name to make a new contact. enter ERASE to remove all contacts. or press enter to exit: ")

        if name_add != "" and name_add != "ERASE":
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
            input("Added. press enter to go home")
            askforhome = False

        elif name_add == "ERASE":
            erase_contact = input("press enter to erase all contacts or enter any text to cancel  ")
            if erase_contact == "":
                contacts_write = open("PhoenixOS_Contacts.txt", "w")
                contacts_write.write("")
                contacts_write.close()
                input("Contacts erased press enter to go home")
                askforhome = False
            else:
                input("Erase canceled press enter to go home")
                askforhome = False
        else:
            askforhome = False

    #SETTINGS
    elif app_open == "A11" or app_open == "a11" or app_open == "11":

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
            print("Settings")
            print("1. About")
            print("2. Reduce Blanks: " + reduce_blank_status)
            print("3. Show note on home: " + note_home)
            print("4. Show remindners on home: " + home_reminders)
            print("5. Require login on start: " + login)
            print("6. Change name")
            print("7. Change password")
            print("8. Manage downloaded librarys")
            print("9. Factory reset")
            print()
            Setting_num = input("Enter a setting number or press enter to leave: ")
            LinePrint()
            #DISABLE RETURN LOOP
            if Setting_num == "":
                settings_lock = False
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
                if read_line(8) == "TRUE":
                    print("Pygame: Installed")
                    input("Press enter to return to settings ")
                else:
                    print("Pygame: Uninstalled")
                    install_pygame = input("Press enter to return to settings, Enter INSTALL to install pygame: ")
                    if install_pygame == "INSTALL" or install_pygame == "install" or install_pygame == "Install":
                        print()
                        os.system("pip install pygame")
                        time.sleep(2)
                        import pygame
                        pygame.init()
                        write_line(8, "TRUE")
                    
            #factory reset
            elif Setting_num == "9":
                print("This will reset all user data")
                print("once reset finishes you can open PhoenixOS with a fresh start")
                reset_pass = input("enter your password to confirm a factory reset: ")
                if reset_pass == password:
                    default_save = "NONE\nNONE\nON\nON\n\nON\n100\nFALSE"
                    contacts_write = open("PhoenixOS_Save.txt", "w")
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


    #Shutdown
    elif app_open == "off" or app_open == "OFF" or app_open == "Off":
        break

    #UNFOUND PROGRAM
    else:
        print("The application was unable to launch. " + app_open + " could not be found")

    if askforhome == True:
        input("Press ENTER to return home")
    askforhome = True
    LinePrint()

#on shutdown
LinePrint()
print("PhoenixOS is closing")