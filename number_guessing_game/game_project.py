#Creator: Derek So

#Title: Guess That Number

#Description: A Python Based Number Guessing Game.
#A Random Number Between 1-30 Will Auto Generated.
#While User Will Have 5 Guesses/Lives.
#Scores Playback Is Avaliable With Local File Storage.

#Version: 0.0.1

#Release Date: 8/18/2022


    
#Main Module
def main():
    
    #Initialize Values
    global game_settings
    
    game_settings = 0
    
    #Load Initial Screen
    init_screen()

    #Load Main Menu
    main_menu()



#Initial Display Module
def init_screen():

    #Game Title
    title = "Guess That Number"

    #Game Description    
    description =   " Come Play Our Newest Game \n"\
                    " Guess That Number \n"\
                    " Could You Guess That Magic Number In 5 Attempts? \n"\
                    " And Revisit Your Amazing Gaming Achievement Anytime."

    #Game Creator
    creator = "Derek So"

    #Game Version
    version = "0.0.1"

    
    #Display Game Title
    print("\n", title, "\n")

    #Display Game Description
    print(description, "\n")

    #Display Game Techstack
    print(" Powered by Python 3.10.5")

    #Display Game Version
    print(" Version: ", version)
    
    #Display Game Creator
    print(' Created By:', creator, "\n")
    
    #Continue Button
    continue_button()


#Continue Button Module
def continue_button():

    #Error Checking
    try:
        #User Input (Hit Enter Button)
        input("Press Enter to Continue...")

    #SyntexError Message Override (Empty Input)
    except SyntaxError:

        #Override Error
        pass
    

#Main Menu Module
def main_menu():

    #Initialize Variable
    menu_choice = 0

    global game_settings

    #Testing Mode On
    if game_settings == 1:

        #Display Testing Mode Warning
        print("\n WARNING: Testing Mode Is On \n")
        

    #Display Options Menu
    print ("\n Game Menu \n\n"\
           " 1 - Start Game \n"\
           " 2 - View Game Instructions \n"\
           " 3 - View Game History \n"\
           " 4 - Game Settings \n"\
           " 5 - Exit Game \n")

    #Input Validation Loop
    while True:

        #User Input
        menu_choice = input("Please Select An Option: ")

        #Print Space
        print("\n")

        #Input Validation 
        try:
        
            #Value Type Check
            menu_choice = int(menu_choice)

        #Error Message
        except:

            #Display Error Message
            print("Invalid Input, Please Enter An Option (1-4) \n")
            
            continue

        #Value Check Loop  
        if menu_choice > 5 or menu_choice < 1:

            #Display Error Message
            print("Invalid Input, Please Enter An Option (1-4) \n")
            
            continue

        #Break Loop
        break
        
    #Menu Choice 1 (Start Game)
    if menu_choice == 1:

        #Load Game
        game_handling()

    #Menu Choice 2 (Game Instructions)
    elif menu_choice == 2:

        #View Game Instructions Function
        print("\n The Computer Opponent Will Generate An Number \n"\
              " From 1-30 Every Time You Start A New Game. \n"\
              " Users Have 5 Attempts to Guess The Correct Number. \n"\
              " Users Could Run And Repeat The Game Indefinetly. \n"\
              " Scores And Gaming History Will Be Stored Locally On The Machine. \n"\
              " Gaming History Playback Is Avaliable Through The Game Menu. \n"\
              " Game Settings Avaliable Are Testing Mode, Reset Score & Read Text File \n\n"\
              " For Any Enquiries or Support Info, Please Contact The Developer. \n")
    
        #Continue Button
        continue_button()
    
        #Return To Main Menu 
        main_menu()

    #Menu Choice 3 (Game History)
    elif menu_choice == 3:

        #View Game History
        score_display()

        #Continue Button
        continue_button()
        
        #Return To Main Menu 
        main_menu()
        

    #Menu Choice 4 (Game Settings)
    elif menu_choice == 4:

        #Import Testing Module
        import debug_tools 
        
        #Testing ToolKit Function
        game_settings = debug_tools.new_settings()
        
        #Return To Main Menu 
        main_menu()
        
    
    #Menu Choice 5 (Exit)    
    else:
        #Display Exit Message
        print("Goodbye! Play Again Soon! \n")

        #Exit Screen
        exit()


#Game Handling Module  
def game_handling():

    #Load Game Core
    score, gameplay, wins, lose = game_core()

    #Process Score Handling
    score_handling(score, gameplay, wins,lose)

    #Load Game Menu
    game_menu()



#Game Menu Module
def game_menu():

    #Initialize Values
    game_choice = 0

    #Display Options Menu
    print ("Would You Like To Play Another Round? \n"\
            "1 - Play Another Round \n"\
            "2 - Return To Main Menu \n")
        
    #Input Validation Loop
    while True:

        #User Input
        game_choice = input("Please Select An Option: ")

        #Print Space
        print("\n")

        #Input Validation
        try:
            #Value Type Check
            game_choice = int(game_choice)

        #Error Message Override
        except:

            #Display Error Message
            print("Invalid Input, Please Enter An Option (1-2) \n")
            continue

        #Value Check Loop    
        if game_choice > 2 or game_choice < 1:

            #Display Error Message
            print("Invalid Input, Please Enter An Option (1-2) \n")
            continue

        #Break Loop
        break

    
    #Game Repat Loop
    while game_choice == 1:

        #Restart Game
        game_handling()
        
    else:
        #Return To Main Menu
        main_menu()


#Game Core Module
def game_core():

    #nitialize Values
    value_generated = 0  #Generated Value
    value_guess = 0  #User Input Value
    lives = 5  #Number Of Avalible Attempts
    score = 0  #Store Scores
    wins = 0  #Store Winnings
    lose = 0  #Store Loses
    gameplay = 0  #Store Times Of Games Plays

    #Initialize List
    user_input_values = []  #Store User Guesses

    #Input Random Module
    import random

    #Generate Random Number
    value_generated = random.randint(1, 30)


    #Load Game Setting Value
    global game_settings

    #Testing Mode 
    if game_settings == 1:
        
        #Display Testing Mode Warning
        print("\n WARNING: Testing Mode Is On \n")

        #Display Auto Generated Number
        print("Testing Mode: The Auto Gen Value Is:", value_generated, "\n")

    
    #Attempts Loop   
    for attempts in range (lives):
        
        #Input Validation Loop
        while True:

            #User Input
            value_guess = input("Please Enter Your Guess (1-30)")

            #Input Validation
            try:

                #Value Type Validation
                value_guess = int(value_guess)

            #Error Message Override
            except:
                
                #Display Error Message
                print("Invalid Input, Please Enter An Number (1-30) \n")

                continue
            
            #Value Validation Loop 
            if value_guess > 30 or value_guess < 1:

                #Display Error Message
                print("Invalid Input, Please Enter An Number (1-30) \n")
                
                continue

            #Exit Loop
            break

        #Store User Input Value Into List
        user_input_values.append(value_guess)


        #Compares Numbers (Correct Guess)
        if value_guess == value_generated:

            #Display Game Message
            print("\n Congrats, Your Guess Is Correct \n")

            #Add One to Score
            score += 1

            #Add One to Wins
            wins += 1
            
            break

        #Compares Numbers (High Number)
        elif value_guess > value_generated:

            #Minus One Live
            lives -= 1

            #Display Number Too High Message
            print("Try Again, Number Too High \n")

        #Compares Numbers (Low Number)
        elif value_guess < value_generated:

            #Minus One Live
            lives -= 1

            #Display Number Too Low Message
            print("Try Again, Number Too Low \n")

    #Out of Attempts (Game Over)
    if lives == 0:

        #Display Game Over Message
        print("Game Over \n")

        #Add One to Loses
        lose += 1

    #Display Correct Number
    print("The Correct Number is: ", value_generated)
    
    #Display List Of User Input Guesses
    print("Your Guess Are: ", *user_input_values, sep = ", ")

    #Print Space
    print("\n")

    #Store Counts Of Game Play
    gameplay += 1
    
    return score, gameplay, wins, lose


def score_handling(score, gameplay, wins,lose):

    #Load Text File & Load Stored Values
    total_score, total_gameplay, total_wins, total_lose = file_read()

    #Update New Score to Total Scores
    total_score += score

    #Update New Game Play to Total Game Plays
    total_gameplay += gameplay

    #Update New Winnings to Total Winnings
    total_wins += wins

    #Update New Loses to Total Loses
    total_lose += lose

    #Write New Values to Text File
    file_write(total_score, total_gameplay, total_wins, total_lose) 

    return total_score, total_gameplay, total_wins, total_lose


#Text File Writing Module
def file_write(total_score, total_gameplay, total_wins, total_lose):

    #Validation Check
    try:
        
        #Open Text File In Write Mode
        f = open('gameHistory.txt', 'w')

    #Override File Not Exist Error Message
    except IOError:

        #Display IO Error
        print("File Error, File Does Not Exist \n")
                
    else:

        #Add Values to List
        lines = [total_score, total_gameplay, total_wins, total_lose]

        #Text File Writing Loop
        for line in lines:

            #Write Value by Line
            f.write(str(line))

            #Write Space by Line
            f.write('\n')

        #Close File
        f.close()


#Text File Reading Module
def file_read():

    #Validation Check
    try:
        
        #Open Text File In Read Mode
        file_obj = open('gameHistory.txt', 'r')

    #Override File Not Exist Error Message
    except IOError:

        #Display IO Error
        print("File Error, File Does Not Exists \n")

    #Override Value Error Message
    except ValueError:

        #Display Value Error
        print("Value Error, Data Corrupted or Invalid Value \n")
                
    else:
        #Read File By Line
        obj = file_obj.readline()

        #Remove Space By Line
        obj = obj.rstrip('\n')

        #Intialize List
        file_list = []

        #Add Values To List
        file_list.append (obj)

        #Read File By Line Loop
        while obj != '':

            #Read File By Line
            obj = file_obj.readline()

            #Remove Space By Line
            obj = obj.rstrip('\n')

            #Print Line String
            file_list.append (obj)
        
        #Close File
        file_obj.close()

        
        #File Content Validation & Assign Value Loop
        if len(file_list) > 4:

            #Load Total Score From File
            total_score = int(file_list[0])

            #Store Total Game Play From File
            total_gameplay = int(file_list[1])

            #Store Total Winnings From File
            total_wins = int(file_list[2])

            #Store Total Loses From File
            total_lose = int(file_list[3])

        #Load Default Values   
        else:
            
            #Initialize Values
            total_score = 0
            total_gameplay = 0
            total_wins = 0
            total_lose = 0
        

    return total_score, total_gameplay, total_wins, total_lose 
    

def score_display():

    #Load Scores From Text File
    total_score, total_gameplay, total_wins, total_lose = file_read()

    #Display Total Score
    print("\nTotal Score Is:", total_score)

    #Display Total Game Play
    print("Total Game Play Is:", total_gameplay)

    #Display Total Winings
    print("Total Wins Are:", total_wins)

    #Display Total Loses
    print("Total Loses Are:", total_lose, "\n")



#Execute Main Function
main()


