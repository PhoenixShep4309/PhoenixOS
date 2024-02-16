"""PhoenixOS"""


#Variable Setup
import pygame
import random
import sys
import time
pygame.init()
sys_os_version = 3.0
askforhome = True
PhoenixOS_power = True
print("\n" * 100)
login = True
#Variable Setup End




#check line amount
line_file = open("line.txt", "r")
line_file = line_file.read()
if line_file == "100":
    Line_amount = 100
elif line_file == "10":
    Line_amount = 10
else:
    Line_amount = 100


def LinePrint():
    print("\n" * Line_amount)


def DateAndTime():
    t = time.localtime()
    current_time = time.strftime("%D  %H:%M", t)
    return current_time


#check user data
name = open("name.txt", "r")
name = name.read()
password = open("password.txt", "r")
password = password.read()


#setup software
if name == "NONE" and password == "NONE":
    print("PhoenixOS")
    
    name_input = input("Please enter your name: ")
    name_write = open("name.txt", "w")
    name_write.write(name_input)
    
    password_input = input("Enter a password: ")
    pass_write = open("password.txt", "w")
    pass_write.write(password_input)
    
    pass_write.close()
    name_write.close()
    password = password_input
    name = name_input
    login = False
    
    print()
    print("PhoenixOS is ready")
    print("A guide is avalible in settings")
    print("to open the guide enter A9 on the home screen")
    print("then enter 2 in the text field")
    input("Press enter to open PhoenixOS")
    LinePrint()
    print("Welcome to the home screen. Enter a code on the left of the app to open it. this message will not show up again")
    print("----------")
    print()
    print()


if login:
    print("Welcome back " + name)
    pass_guess = input("Enter your password to begin: ")
    while pass_guess != password:
        pass_guess = input("Try again: ")
    LinePrint()
    
        
while PhoenixOS_power:
    #Display Home
    print(name)
    date_and_time = DateAndTime()
    print(date_and_time)
    print()
    note_home = open("Note_home.txt", "r")
    note_home = note_home.read()
    if note_home == "ON":
        note_file = open("note.txt", "r")
        note_file = note_file.read()
        if note_file == "":
            note_file = "None"
        print("Note: " + note_file)      
        print()
    print("A1 - Calculator")
    print("A2 - Guess The Num/Word")
    print("A3 - Rock Paper Scissors")
    print("A4 - Password Generator")
    print("A5 - Timer")
    print("A6 - Paintball")
    print("A7 - Note")
    print("A8 - Contacts")
    print("A9 - Settings")
    print("off - Shutdown")
    app_open = input("Enter an app code: ")
    LinePrint()
    #Display Home End
    
    
    #CALCULATOR START
    if app_open == "A1" or app_open == "a1":
        app_calc_type = input("Enter A for addition, S for subtraction, M for multiplication, D for division: ")
        app_calc_num1 = float(input("Enter the first number: "))
        app_calc_num2 = float(input("Enter the second number: "))
        if app_calc_type == "A" or app_calc_type == "a":
            app_calc_num1 += app_calc_num2  
            print("Your number is: " + str(app_calc_num1))
        elif app_calc_type == "S" or app_calc_type == "s":
            app_calc_num1 -= app_calc_num2
            print("Your number is: " + str(app_calc_num1))
        elif app_calc_type == "M" or app_calc_type == "m":
            app_calc_num1 *= app_calc_num2
            print("Your number is: " + str(app_calc_num1))
        elif app_calc_type == "D" or app_calc_type == "d":
            app_calc_num1 /= app_calc_num2
            print("Your number is: " + str(app_calc_num1))
        else:
            print("That is not a valid option")
        #END OF CALCULATOR
            
        
    #GUESS NUM/WORD
    elif app_open == "A2" or app_open == "a2":
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
                print("Player 1 you have " + str(app_paint_heart1) + " hearts. Player 2 has " + str(app_paint_heart2) + " herats")
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
                print("Player 2 you have " + str(app_paint_heart2) + " hearts. Player 1 has " + str(app_paint_heart1) + " herats")
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
                print("Player 1 you have " + str(app_paint_heart1) + " hearts. The computer has " + str(app_paint_heart2) + " herats")
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
     
    #contacts
    elif app_open == "A8" or app_open == "a8":
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
            
        
    
    #SETTINGS
    elif app_open == "A9" or app_open == "a9":
        
        settings_lock = True        
        while settings_lock:  
            note_home = open("Note_home.txt", "r")
            note_home = note_home.read()
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
            print("5. Change name")
            print("6. Change password")
            print("7. Factory reset")
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
                print("PhoenixOS guide for version " + str(sys_os_version))
                print("""
Reduce Blanks: reduce blanks is a feature that can lower 
the amount of lines printed if your computer starts to slow down
the lines printed will go from 100 to 10. when you are playing
any 2-player games 100 lines will still print to stop the other
player from seeing inputs


Save data: while you are running the program python will add or remove
values from these text files, line.txt, name.txt, note.txt, password.txt,
contacts.txt do not edit these values outside of the prorgram


Opening apps: when on the home screen launch apps by using the shortcut code
on the left side of the app name. the app launcher is not caps sensitive


Factory reset: in the settings app you can factory reset to return PhoenixOS to
the default settings. this will wipe memory of the users name, password, contacts
and note. reduce blanks will be set to off and you will have to redo setup


Changing name and password: in the settings app you can reset your name and
your password. to change them you will need to know your current password.
the settings wont update until you restart PhoenixOS
                """)
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


            #name change
            elif Setting_num == "5":
                pass_guess = input("Enter your password to change your name: ")
                if pass_guess == password:
                    new_name = input("Enter a name and restart for the update to apply: ")
                    name_write = open("name.txt", "w")
                    name_write.write(new_name)
                    name_write.close()
                else:
                    input("password verification failed press enter to go back")
            #password change
            elif Setting_num == "6":
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
            elif Setting_num == "7":
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
                    print("RESET COMPLETE")
                    sys.exit()
                else:
                    print("password verification failed")
                    input("press enter to go back")
                    
                
            askforhome = False
    #END OF SETTINGS
    
    
    #Shutdown
    elif app_open == "off":
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