"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

"""Psuedo-code Hints

When the program starts, we want to:
------------------------------------
1. Display an intro/welcome message to the player.
2. Store a random number as the answer/solution.
3. Continuously prompt the player for a guess.
  a. If the guess greater than the solution, display to the player "It's lower".
  b. If the guess is less than the solution, display to the player "It's higher".

4. Once the guess is correct, stop looping, inform the user they "Got it"
     and show how many attempts it took them to get the correct number.
5. Let the player know the game is ending, or something that indicates the game is over.

( You can add more features/enhancements if you'd like to. )
"""
# write your code inside this function.

def start_game():
    while True:
        try:
            guessing_question = input("Please enter a number from 0 to 10:   ")
            int(guessing_question)
        except ValueError:
            print("Teaser! That's not a valid value. Try again!")
            continue   
        if int(guessing_question) < 0 or int(guessing_question) > 10:
            print("Oops!... We did it again! The number must be from 0 to 10.")
            continue
        else:
            guessing_number = int(guessing_question)
            return guessing_number

# Kick off the program by calling the start_game function.

print("*** WELCOME TO THE GUESSING GAME ***")
import random
number = random.randint(0,10)
attempt = 0
score_list = []
    
while True:
    
    x = start_game()

    if x > number:
        print("Oh no! It's lower. Please try again!")
        attempt += 1        
        continue        
        
    if x < number:
        print("Oops! It's higher. Please try again!")
        attempt += 1
        continue 

    else:     
        print("Congratulations! You are correct!")
        attempt += 1
        print("You have tried {} times.".format(attempt))
        score_list.append(attempt)
        restart = input("Do you want to restart again?(y/n) ")
        if restart.lower() == "y":
            attempt = 0
            import random
            number = random.randint(0,10)
            print("The High Score is {}".format(min(score_list))) 
            continue           
        else:
            print("Endgame. Thank you for playing!")         
            break
    






