"""
John Widner
06-05-18

"""

from random import randint  # importing random number library for the guessing game

"""
Reverse Your Name
"""
# user input of first name
firstName = input("What is your First Name?: ")
# user input of second name
lastName = input("What is your Last Name?: ")
# outputs the entered name backwards
print("Your name backward is " + firstName[::-1] + " " + lastName[::-1])
"""
END of Reverse Your Name
"""
"""
Guessing Game
"""
# Welcomes the user
print("Welcome! I have a number in mind between 1 and 10. Care to take a guess? ")
# Generate the winning number
win = randint(1, 10)
# User inputs their guess
guess = int(input("What number am I thinking of?"))
# While loop continues until you have guessed correctly
while win != guess:
    guess = int(input("Guess Again? "))
# When guess is correct, Program is ended
print("Great! You guessed it! Thanks for playing.")
exit(0)
