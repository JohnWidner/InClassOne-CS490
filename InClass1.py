"""
John Widner
06-05-18
"""

import math  # importing math library for Quotient and Remainder
from random import randint  # importing random number library for the guessing game

"""
Problem 2a
Reverse Your Name
"""
# user input of first name
firstName = input("What is your First Name?: ")
# user input of second name
lastName = input("What is your Last Name?: ")
# outputs the entered name backwards
print("Your name backward is " + firstName[::-1] + " " + lastName[::-1])

"""
Problem 2b
Quotient and Remainder
"""

print("Welcome! I can divide integers for you.")
x = int(input("Enter the first number: "))
y = int(input("Enter the number to divide the first by: "))

quotient = int(x / y)
remainder = int(x % y)

print("The Answer is "+str(quotient)+" with a remainder of "+str(remainder))

"""
Problem 3
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
