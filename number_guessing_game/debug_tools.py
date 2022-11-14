#Creator: Derek So

#Title: Guess That Number

#Description: A Python Based Number Guessing Game.
#A Random Number Between 1-30 Will Auto Generated.
#While User Will Have 5 Guesses/Lives.
#Scores Playback Is Avaliable With Local File Storage.

#Version: 0.0.1

#Release Date: 8/18/2022

#Game Setting Menu Module & Debugging Toolset
#Reset Score
#Enable/ Disable Testing Mode
#View Local File


#Game Settings Menu
def setting_menu():
    
    #Initialize Variable
    setting_choice = 0
    setting = 0

    #Testing Mode On
    if setting == 1:
        
        #Display Testing Mode Message
        print("\n WARNING, Testing Mode Is On \n")
        
    
    #Display Game Menu
    print ("\n Game Settings \n\n"\
           " 1 - Enable Testing Mode \n"\
           " 2 - Disable Testing Mode \n"\
           " 3 - View Local Score File \n"\
           " 4 - Reset Scores \n"\
           " 5 - Return to Main Menu \n")


    #Input Validation Loop
    while True:

        #User Input
        setting_choice = input("Please Select An Option: ")

     
        try:

            #Interger Validation
            setting_choice = int(setting_choice)

        #Error Message
        except:

            #Display Error Message
            print("Invalid Input, Please Enter An Option (1-5) \n")
            
            continue

        #Value Validation Loop
        if setting_choice > 5 or setting_choice < 1:

            #Display Error Message
            print("Invalid Input, Please Enter An Option (1-5) \n")
            
            continue
        
        #Break Loop
        break
        
    #Menu Choice 1 (Enable Testing Mode)
    if setting_choice == 1:

        #Start Game Function
        setting = 1
    
        #Testing Mode On
        if setting == 1:
        
            #Display Testing Mode Message
            print("\n WARNING: Testing Mode Is Now On \n")
        
        #Return to Game Settings Menu
        setting_menu()


    #Menu Choice 2 (Start Game)
    if setting_choice == 2:

        #Start Game Function
        setting = 0

         
        #Display Testing Mode Message
        print("\n WARNING: Testing Mode Is Now Off \n")

        #Return to Game Settings Menu
        setting_menu()
        
        
    #Menu Choice 3 (Read Local File)
    elif setting_choice == 3:

        #File Validation Check
        try:

            #Open File In Read Mode
            f = open('gameHistory.txt', 'r')

        #File Not Exist Error Message
        except IOError:

            #Display IO Error
            print("File Error, File Does Not Exist \n")

            
        else:

            #Display Message
            print("\nThe Content In The Text File Are: ")

            #Display File Contents
            print(f.read())

        #Close File
        f.close()

        #Return to Game Settings Menu
        setting_menu()
        
        
    #Menu Choice 4 (Reset Scores)
    elif setting_choice == 4:

        #View Game Instructions Function
        reset_score()

        #Game Settings Menu
        setting_menu()


    return setting



#Reset Score
def reset_score():

        #Initialize Values
        reset = 0

        #Display Reset Score Menu
        print ("\nDo You Wish to Reset The Scores?\n"\
            "1 - Reset Score \n"\
            "2 - Return To Menu \n")
        
        #Input Validation Loop
        while True:

            #User Input
            reset = input("Please Select An Option: ")

            #Error Checking
            try:

                #Interger Validation
                reset = int(reset)

            #Override Error Message   
            except:

                #Display Error Message
                print("Invalid Input, Please Enter An Option (1-2) \n")
                continue
            
            #Value Validation
            if reset > 2 or reset < 1:

                #Display Error Message
                print("Invalid Input, Please Enter An Option (1-2) \n")
                
                continue

            #Break Loop
            break


        #Execute Reset Score 
        if reset == 1:

            #Open File In Write Mode
            f = open('gameHistory.txt', 'w')

            #Default Null Values
            default_values = [0, 0, 0, 0]

            #Write Values to File By Line
            for line in default_values:
                f.write(str(line))
                f.write('\n')

            #Close File
            f.close()

            #Display Warning Message
            print("\n WARNING: Scores Reset \n")       


#Settings Update
def new_settings():
    
    #Initialize Value
    new_settings = 0

    #Apply New Settings
    new_settings = para

    return new_settings


#Load Game Settings Menu
para = setting_menu()
