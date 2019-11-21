# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: Working with exception class and structured errors,
#              When the program starts, user should guess a number
#              if guessed number is larger or smaller than chosen number
#              by code, user receives an error message and code asks
#              user to keep guessing till he/she guess correct number"
# <Mazyar Kazemi>,<11/19/2019> assignment 07
# ------------------------------------------------------------------------ #

# custom exceptions define
class Error(Exception):
    """Base class for other exceptions"""
    pass
class SmallValue(Error):
    """this error happens when value is less than what is expected"""
    pass
class LargeValue(Error):
    """This error happens when value is larger than what is expected"""
    pass
# user guesses numbers
# the expected number is:
number = 13
while True:
    try:
        guess = int(input("Enter a number: "))
        if guess < number:
            raise SmallValue
        elif guess > number:
            raise LargeValue
        break
    except SmallValue:
        print("This value is smaller than our number, try another one")
        print()
    except LargeValue:
        print("This value is larger than our number, try another one!")
        print()
print("this is the correct number!")

