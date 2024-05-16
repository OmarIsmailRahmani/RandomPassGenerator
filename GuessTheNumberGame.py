import random

print("----GUESS THE NUMBER----")
print()
print("""Select Difficulty Level
      \nEASY[1-100]...Type (E)\nMEDIUM[1-300]...Type(M)\nHARD[1-500]...Type(H)\nQUIT...Type(Q)""")
def game_starter(): #creating a function which allows the gamer to select level and start the game. 
    
    level_input = input("Type Here: ").lower()
 
    def game(start, end): #This is the actual game in which start and end are the parameters according to the difficulty level. 
        target = random.randint(start,end) #choosing a random number from the range. 

        while True:
            user_input = (input("Guess the number or Type Q to quit: "))
            if (user_input.lower() == "q"): # changing the letter to lower case to avoid case-sensivity. 
                break #if he user wants to quit, game will be over by stoping the program. 
            elif int(user_input) == target: 
                print("Awsm!!...You Guessed the Corrent Number")
                break
            elif int(user_input) < target:
                print("Your Number is Too Small, Guess for a Bigger value... ")
            else:
                print("Your Number is Too Big, Guess for a Smaller value... ")
        print("----GAME OVER----")

    #game level selection:

    if (level_input == "e"):
        game(1,100)
    elif (level_input == "m"):
        game(1,300)
    elif (level_input == "h"):
        game(1,500)
    elif(level_input == "q"):
        print("----GAME OVER----")
    else:
        print("choose correct option!")
        game_starter()
             

game_starter() 

