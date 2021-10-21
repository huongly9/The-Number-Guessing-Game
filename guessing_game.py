
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
