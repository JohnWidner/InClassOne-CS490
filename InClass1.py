"""
John Widner
06-05-18

"""

from random import randint  # importing random number library for the guessing game

"""
Reverse Your Name
"""
firstName = input("What is your First Name?: ")  # user input of first name
lastName = input("What is your Last Name?: ")  # user input of second name
print("Your name backward is " + firstName[::-1] + " " + lastName[::-1])

print("Welcome! I have a number in mind between 1 and 10. Care to take a guess? ")

win = randint(1, 10)
guess = int(input("What number am I thinking of?"))

while win != guess:
    guess = int(input("Guess Again? "))

print("Great! You guessed it! Thanks for playing.")
