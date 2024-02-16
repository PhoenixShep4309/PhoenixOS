
"""PhoenixOS"""

#Variable Setup
import pygame
import random
import sys
import time
import os
pygame.init()

sys_os_version = 3.5
askforhome = True
PhoenixOS_power = True
first_time = False
print("\n" * 100)
#Variable Setup End

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

#setup files if not found
file1 = os.path.isfile("Note_home.txt")
file2 = os.path.isfile("card.txt")
file3 = os.path.isfile("contacts.txt")
file4 = os.path.isfile("line.txt")
file5 = os.path.isfile("login.txt")
file6 = os.path.isfile("name.txt")
file7 = os.path.isfile("note.txt")
file8 = os.path.isfile("password.txt")
file9 = os.path.isfile("reminders.txt")
file10 = os.path.isfile("reminders_home.txt")
if file1 and file2 and file3 and file4 and file5 and file6 and file7 and file8 and file9 and file10:
    files_ready = "ALL"
elif file1 == False and file2 == False and file3 == False and file4 == False and file5 == False and file6 == False and file7 == False and file8 == False and file9 == False and file10 == False:
    files_ready = "NONE"
else:
    print("NOT ALL SAVE FILES FOUND. PLEASE REMOVE ALL THE SAVE FILES IN THE PROGRAM TO CONTINUE")
    sys.exit()
    
if files_ready == "NONE":
    missing = input("Save files missing. Press enter to create save files or enter QUIT to exit: ")
    if missing == "QUIT" or missing == "quit":
        sys.exit()
    file = open("Note_home.txt", "w")
    file.write("ON")
    file.close()
    file = open("card.txt", "w")
    file.close()
    file = open("contacts.txt", "w")
    file.close()
    file = open("line.txt", "w")
    file.write("100")
    file.close()
    file = open("login.txt", "w")
    file.write("ON")
    file.close()
    file = open("name.txt", "w")
    file.write("NONE")
    file.close()
    file = open("note.txt", "w")
    file.close()
    file = open("password.txt", "w")
    file.write("NONE")
    file.close()
    file = open("reminders.txt", "w")
    file.close()
    file = open("reminders_home.txt", "w")
    file.write("ON")
    file.close()
    print("\n" * 100)
    input("Files Ready. Press enter to start setup")
    
#check line amount
line_file = open("line.txt", "r")
line_file = line_file.read()
if line_file == "100":
    Line_amount = 100
elif line_file == "10":
    Line_amount = 10
else:
    Line_amount = 100

#check user data
name = open("name.txt", "r")
name = name.read()
password = open("password.txt", "r")
password = password.read()

#setup software
if name == "NONE" and password == "NONE":
    print("PhoenixOS " + str(sys_os_version) + " Setup")
    print("---------------------")
    
    name_input = input("Please enter your name. This can be changed later: ")
    while name_input == "NONE":
        name_input = input("Username not allowed. Enter a new username: ")
    name_write = open("name.txt", "w")
    name_write.write(name_input)
    
    password_input = input("Enter a password. This can be changed later: ")
    while password_input == "NONE":
        password_input = input("Password not allowed. Enter a new password: ")
    pass_write = open("password.txt", "w")
    pass_write.write(password_input)
    
    pass_write.close()
    name_write.close()
    password = password_input
    name = name_input
    first_time = True
    
    print()
    print("Setup Complete")
    input("Press enter to open PhoenixOS")
    LinePrint()
    print("Welcome to the home screen. Enter a code on the left of the app to open it. this message will not show up again")
    print("----------")
    print()
    print()

login_home = open("login.txt", "r")
login = login_home.read()
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
    note_home = open("Note_home.txt", "r")
    note_home = note_home.read()
    if note_home == "ON":
        note_file = open("note.txt", "r")
        note_file = note_file.read()
        if note_file == "":
            note_file = "None"
        print("Note: " + note_file)      
        print()
        
    #reminders on home
    remind_home = open("reminders_home.txt", "r")
    remind_home = remind_home.read()
    if remind_home == "ON":
        reminders = open("reminders.txt", "r")
        reminders = reminders.read()
        if reminders == "":
            print("Reminders: None")
            print()
        else:
            print("Reminders: ")      
            print(reminders)
            print()
    
    print("A1 - Calculator")
    print("A2 - Guess The Num/Word")
    print("A3 - Rock Paper Scissors")
    print("A4 - Password Generator")
    print("A5 - Timer")
    print("A6 - Paintball")
    print("A7 - Note")
    print("A8 - Reminders")
    print("A9 - Contacts")
    print("A10 - Payment Card")
    print("A11 - Settings")
    print("off - Shutdown")
    app_open = input("Enter an app code: ")
    LinePrint()
    #Display Home End
    
    
    #CALCULATOR START
    if app_open == "A1" or app_open == "a1":
        askforhome = False
        while 1 == 1:
            #num1
            num1 = input("Enter a number or press enter to leave: ")
            if num1 == "":
                break
            else:
                num1 = float(num1)
            #symbol
            symbol = input("Enter one of the following symbols ( + - / * ) or press enter to leave: ")
            if symbol == "":
                break
            #num2
            num2 = input("Enter a number or press enter to leave: ")
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
    elif app_open == "A2" or app_open == "a2":
        print("this app requires 2 players")
        app_guessnumorword_type = input("will you guess the number or word? ")
        #NUMBER
        if app_guessnumorword_type == "number":
            print()
            app_guessnumorword_num = input("what is the maximum the number could be: ")
            app_guessnumorword_player1 = input("pick your number on a scale of 1 to " + app_guessnumorword_num + ": ")
            print("\n" * 100)
            app_guessnumorword_player2 = input("Player2, guess the number on a scale of 1 to " + app_guessnumorword_num + ": ")
            print()
            if app_guessnumorword_player1 == app_guessnumorword_player2:
                print("Congrats player2 you win!")
            elif app_guessnumorword_player1 != app_guessnumorword_player2:
                print("Sorry player2 you lost the number was " + app_guessnumorword_player1)
        #WORD
        elif app_guessnumorword_type == "word":
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
                print("sorry player2 you loose")
        else:
            print("that is not a choice")
            #END OF GUESS NUM/WORD
            
    
    #ROCK PAPER SCI
    elif app_open == "A3" or app_open == "a3":
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
    elif app_open == "A4" or app_open == "a4":
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
    elif app_open == "A5" or app_open == "a5":
        app_time_sec = int(input("How many seconds will the timer be: "))
        input("Starting timer when you press enter  ")
        print("Timer Started")
        pygame.time.wait(app_time_sec * 1000)
        print("Timer ended")
            
    #Paintball
    elif app_open == "A6" or app_open == "a6":
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
    #note
    elif app_open == "A7" or app_open == "a7":        
        note_file = open("note.txt", "r")
        note_file = note_file.read()
        if note_file != "":
            print("You have a note written down:")
            print(note_file)
            print()
        elif note_file == "":
            print("You dont have a note")
        change_note = input("Enter text to change it or press enter to go back: ")
        if change_note != "":
            note_write = open("note.txt", "w")
            note_write.write(change_note)
            note_write.close()
            input("Note changed press enter to go back")
        askforhome = False   
    #end of notes
    
    #reminders
    elif app_open == "A8" or app_open == "a8":
        reminders = open("reminders.txt", "r")
        reminders = reminders.read()
        if reminders != "":
            print("Here is your reminders:")
        print(reminders)
        print()
        add_reminders = input("Enter text to add a reminder, enter REMOVE to remove a reminder or press enter to go home: ")
        if add_reminders == "":
            askforhome = False
        elif add_reminders != "" and add_reminders != "REMOVE":
            if reminders != "":
                append_reminders = open("reminders.txt", "a")
                append_reminders.write("\n")
                append_reminders.close()
            append_reminders = open("reminders.txt", "a")
            append_reminders.write(add_reminders)
            append_reminders.close()
            input("Reminder added press enter to go home")
            askforhome = False
        elif add_reminders == "REMOVE":
            remove_reminders = input("enter exactly what the reminder says to delete it: ")
            old_reminders = open("reminders.txt", "r")
            old_reminders = old_reminders.read()
            new_reminders = old_reminders.replace(remove_reminders, "")
            reminders = open("reminders.txt", "w")
            reminders.write(new_reminders)
            reminders.close()
            result = ""
            with open("./reminders.txt", "r") as file:
                for line in file:
                    if not line.isspace():
                        result += line
            reminders = open("reminders.txt", "w")
            reminders.write(result)
            reminders.close()
            input("removed. press enter to go home")
            askforhome = False
            
    #contacts
    elif app_open == "A9" or app_open == "a9":
        contacts_file = open("contacts.txt", "r")
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
                contacts_file = open("contacts.txt", "a")
                contacts_file = contacts_file.write("\n")
            contacts_file = open("contacts.txt", "a")
            contacts_file = contacts_file.write(contact_add)
            input("Added. press enter to go home")
            askforhome = False
            
        elif name_add == "ERASE":
            erase_contact = input("press enter to erase all contacts or enter any text to cancel  ")
            if erase_contact == "":
                contacts_write = open("contacts.txt", "w")
                contacts_write.write("")
                contacts_write.close()
                input("Contacts erased press enter to go home")
                askforhome = False
            else:
                input("Erase canceled press enter to go home")
                askforhome = False
        else:
            askforhome = False
            
    #card
    elif app_open == "A10" or app_open == "a10":
        askforhome = False
        card = open("card.txt", "r")
        card = card.read()
        if card != "":
            card = open("card.txt", "r")
            card.seek(12)
            card = card.read(4)
            print("Saved card:")
            print("---- ---- ---- " + str(card))
            card_action = input("Press enter to exit or enter VIEW to view the details or enter EDIT to edit the details: ")
            if card_action == "VIEW" or card_action == "view":
                LinePrint()
                password_attempt = input("Enter your password: ")
                if password_attempt == password:
                    LinePrint()
                    card = open("card.txt", "r")
                    card = card.read()
                    print(card)
                    input("press enter to go back")
                else:
                    input("password verification failed. press enter to go home")
            elif card_action == "EDIT" or card_action == "edit":
                LinePrint()
                password_attempt = input("Enter your password: ")
                if password_attempt == password:
                    card_num = input("Enter the card number: ")
                    card_month = input("Enter the experation month: ")
                    card_year = input("Enter the experation year: ")
                    card_digits = input("Enter the 3 digits on the back of the card: ")
                    card_data = (card_num + "  " + card_month + "/" + card_year + "  " + card_digits)
                    card_file = open("card.txt", "w")
                    card_file.write(card_data)
                    card_file.close()
                    input("Saved. press enter to go back home")
                else:
                    input("password verification failed. press enter to go home")
        else:
            card_setup = input("To save card details press enter to go home enter 'QUIT': ")
            if card_setup != "QUIT" and card_setup != "quit":
                card_num = input("Enter the card number: ")
                card_month = input("Enter the experation month: ")
                card_year = input("Enter the experation year: ")
                card_digits = input("Enter the 3 digits on the back of the card: ")
                card_data = (card_num + "  " + card_month + "/" + card_year + "  " + card_digits)
                card_file = open("card.txt", "w")
                card_file.write(card_data)
                card_file.close()
                input("Saved. press enter to go back home")


    
    #SETTINGS
    elif app_open == "A11" or app_open == "a11":
        
        settings_lock = True        
        while settings_lock:  
            login_home = open("login.txt", "r")
            login = login_home.read()
            note_home = open("Note_home.txt", "r")
            note_home = note_home.read()
            home_reminders = open("reminders_home.txt", "r")
            home_reminders = home_reminders.read()
            if Line_amount == 100:
                reduce_blank_status = "OFF"
            elif Line_amount == 10:
                reduce_blank_status = "ON"
            LinePrint()
            print("Settings")
            print("1. About")
            print("2. Help")
            print("3. Reduce Blanks: " + reduce_blank_status)
            print("4. Show note on home: " + note_home)
            print("5. Show remindners on home: " + home_reminders)
            print("6. Require login on start: " + login)
            print("7. Change name")
            print("8. Change password")
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
            #HELP
            elif Setting_num == "2":
                print("Guide avalible at bit.ly/PhoenixOSguide")
                input("Press enter to go back")
            #toggle lines
            elif Setting_num == "3":
                if Line_amount == 10:
                    Line_amount = 100
                elif Line_amount == 100:
                    Line_amount = 10
                line_file = open("line.txt", "w")
                line_file.write(str(Line_amount))
                line_file.close()
            #note on home
            elif Setting_num == "4":
                if note_home == "ON":
                    Note_home = open("Note_home.txt", "w")
                    Note_home.write("OFF")
                    Note_home.close()
                elif note_home == "OFF":
                    Note_home = open("Note_home.txt", "w")
                    Note_home.write("ON")
                    Note_home.close()
            #reminders on home
            elif Setting_num == "5":
                if home_reminders == "ON":
                    reminders_home = open("reminders_home.txt", "w")
                    reminders_home.write("OFF")
                    reminders_home.close()
                elif home_reminders == "OFF":
                    reminders_home = open("reminders_home.txt", "w")
                    reminders_home.write("ON")
                    reminders_home.close()
                    
            #login on start    
            elif Setting_num == "6":
                pass_attempt = input("Enter your password: ")
                if pass_attempt == password:
                    if login == "ON":
                        login_home = open("login.txt", "w")
                        login_home.write("OFF")
                        login_home.close()
                    elif login == "OFF":
                        login_home = open("login.txt", "w")
                        login_home.write("ON")
                        login_home.close()
                        
                else:
                    input("Verification failed. press enter to go back")

            #name change
            elif Setting_num == "7":
                pass_guess = input("Enter your password to change your name: ")
                if pass_guess == password:
                    new_name = input("Enter a name and restart for the update to apply: ")
                    name_write = open("name.txt", "w")
                    name_write.write(new_name)
                    name_write.close()
                else:
                    input("password verification failed press enter to go back")
            #password change
            elif Setting_num == "8":
                pass_guess = input("Enter your current password: ")
                if pass_guess == password:
                    new_pass = input("Enter a password and restart for the update to apply: ")
                    pass_write = open("password.txt", "w")
                    pass_write.write(new_pass)
                    pass_write.close()
                else:
                    input("password verification failed press enter to go back")
                print("password")
            #factory reset
            elif Setting_num == "9":
                print("This will reset all user data")
                print("once reset finishes you can open PhoenixOS with a fresh start")
                reset_pass = input("enter your password to confirm a factory reset: ")
                if reset_pass == password:
                    contacts_write = open("contacts.txt", "w")
                    contacts_write.write("")
                    contacts_write.close()
                    pass_write = open("password.txt", "w")
                    pass_write.write("NONE")
                    pass_write.close()
                    name_write = open("name.txt", "w")
                    name_write.write("NONE")
                    name_write.close()
                    line_write = open("line.txt", "w")
                    line_write.write("100")
                    line_write.close()
                    note_write = open("note.txt", "w")
                    note_write.write("")
                    note_write.close()
                    Note_home = open("Note_home.txt", "w")
                    Note_home.write("ON")
                    Note_home.close()
                    login_home = open("login.txt", "w")
                    login_home.write("ON")
                    login_home.close()
                    reminders = open("reminders.txt", "w")
                    reminders.write("")
                    reminders.close()
                    home_reminders = open("reminders_home.txt", "w")
                    home_reminders.write("ON")
                    home_reminders.close()
                    card = open("card.txt", "w")
                    card.write("")
                    card.close()
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