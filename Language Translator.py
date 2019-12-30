#Sabrina Turney
#October 22, 2018
#Language Translator
#This program displays a menu of languages and asks for a user input to display
#the text "Good Morning" in the language of their choosing. The program will
#check for validation, and be able to loop and begin again at the menu.


#I make a little intro module to display the hello info.
def intro():
    print("Welcome to my language translator program!")

#I keep the menu in its own module here, and list the menu options. I keep
#number 5 as a menu option, but still allow a loop of the program later.
def menu():
    print("Select a language by number,")
    print("and I will say \"Good Morning\" in that language!")
    print("1. English \n2. Italian \n3. Spanish \n4. German \n5. End the program")

#The main function.    
def main():
    menuChoice = 0 #My menu choices are all numbers, so when declaring, use int.
    loopProgram = "yes" #Set this loop to yes so it'll loop once at least.


    #This while loop runs the program for the user.
    while loopProgram == "yes":
        menuChoice = 0

        #Call two previous modules.
        intro()
        menu()

        #If the menu choice isn't 1-5 (it's set to 0), we get an input here:
        while menuChoice != 1 and menuChoice != 2 and menuChoice != 3 and menuChoice != 4 and menuChoice != 5:
            menuChoice = int(input("Please select a language for me to translate now: "))

            #Our decision structure with all the translations.
            if menuChoice == 1:
                print("Good morning in English is Good morning.")
            elif menuChoice == 2:
                print("Good morning in Italian is Buongiorno.")
            elif menuChoice == 3:
                print("Good morning in Spanish is Buenos dias.")
            elif menuChoice == 4:
                print("Good morning in German is Guten morgen.")
            elif menuChoice == 5:
                print("Thank you for playing! Goodbye!")
                break
            #If the user enters something funny, we ask for a real input.
            else:
                print("Please enter a valid menu option.")

        #We break the loop and ask if they want to play again.
        loopProgram = input("Would you like to play again? Enter \"yes\" or \"no\".")
        #Anything other than "yes" will result in a nice goodbye message.
        if loopProgram != "yes":
            print("Thank you for playing! Goodbye!")

#Call the main program for the user.
main()
