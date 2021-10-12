# The Number Guessing Game
 A fun number guessing game to help you get better chance at gambling

code adapted from https://teamtreehouse.com/community/how-to-check-if-input-is-int-and-not-string-or-float
by Joey Bruijns
try:
     number = input("Please enter a number: ")
     int(number)
except ValueError:
     print("That's not a number..")
else:
     print(number)
