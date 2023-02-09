'''
ROCK/PAPER/SCISSOR GAME
How To Play: User has to input his/her name and anyone of the above options, user will be playing against a computer, All The Best, Let the Game Begin!!!
'''
print('\n')
print('***************************************************')
print("    Welcome To The Game Of Rock/Paper/Scissor!     ")
print('***************************************************')

import random

user_wins = 0
computer_wins = 0
tied = 0

options = ["rock","paper","scissor"]

user_name = input("Please enter your Name: ")
print("Hi",user_name + "!")

while True:
    user_input = input("\nType in Rock/Paper/Scissor or Q to Quit: ").lower()
    if user_input == 'q':
        break

    if user_input not in options:
        print("Enter only one option out of ROCK , PAPER , SCISSOR!!!")
        print("Please Try Again...")
        continue
    
    random_number = random.randint(0,2) # Rock=0 , Paper=1 , Scissor = 2
    computer_pick = options[random_number]
    print("Computer Picked:", computer_pick + ".")

    if user_input == 'rock' and computer_pick == 'scissor':
        print("You Win!")
        user_wins += 1

    elif user_input == 'paper' and computer_pick == 'rock':
        print("You Win!")
        user_wins += 1

    elif user_input == 'scissor' and computer_pick == 'paper':
        print("You Win!")
        user_wins += 1

    elif user_input == 'scissor' and computer_pick == 'scissor':
        print("Its a Tie!")
        tied +=1

    elif user_input == 'paper' and computer_pick == 'paper':
        print("Its a Tie!")
        tied +=1

    elif user_input == 'rock' and computer_pick == 'rock':
        print("Its a Tie!")
        tied +=1

    else:
        print("You Lost!")
        computer_wins += 1

print("\n")
print("You Won", user_wins , "times")
print("Computer Won", computer_wins , "times")
print("Tied" , tied , "times")
print("\n")
print("Goodbye!")
print("\n")