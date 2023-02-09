'''
In this game user has to enter the max range, within that a number has to be predicted by the user.
Then user has to make guess by entering a guessed number.
If the guessed number is matching with the randomly created number. The user Wins! 
'''
print("\n")
print('--------------------------------------------')
print("      Welcome To Number Guessing Game       ")
print('--------------------------------------------\n')

playing = input("      Do You Wish To Play? (Yes/No): ")

if playing.lower() != "yes":
    quit()

print("\n      Great! Let's Begin")

import random

top_of_range = input("\nType a Number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range) # Converting the string num to int num

    if top_of_range <= 0: # This is to check whether num entered is less than 0
        print("Please Enter a Number which is greater than zero(0)")
        print("Please Try Again")
        quit()

else: # This is to check whether entered no. is num or not
    print("\nAs this is a Number game, Please Type a Digit")
    print("Please Try Again...\n")
    quit()

random_number = random.randint(0 , top_of_range) # randint takes in 2 arguments min & max no.
guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess the Number: ")
    print('\n')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please Enter a Number Only")

    if user_guess == random_number:
        print("You Have Guessed it Correctly :)\nCONGRATS!!!\n")
        break

    elif user_guess > random_number:
         print("You have guessed above the Number!\nPlease Try Again...\n")
    else:
        print("You have guessed below the Number!\nPlease Try Again...\n")

print("You got it in", guesses , "guesses.\n")