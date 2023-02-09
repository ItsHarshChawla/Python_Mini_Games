name = input("\nType your name: ")
print("\nWelcome", name, "to this Adventure!")

answer = input(
    "\nYou are on a dirt road, it has come to an end and you can either go left or right. Which way would you like to go? (left/right): ").lower()

if answer == "left":
    answer = input(
        "\nYou have reached a river, you can either walk around it or swim accross? Type walk to walk around or swim to swim accross: ")

    if answer == "swim":
        print("You were eaten by an alligator while swimming, You Lost.")
    elif answer == "walk":
        print("You walked for many miles and ran out of water, You lost the game.")
    else:
        print('Not a valid option. You lose.')

elif answer == "right":
    answer = input(
        "\nYou come to a bridge, it looks wobbly, Do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You choose back, Hence lost.")
    elif answer == "cross":
        answer = input(
            "You crossed the bridge and meet a stranger. Do you want to talk to them (yes/no)? ")

        if answer == "yes":
            print("You spoke to the stanger and they gave you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and You lost!.")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

print("\nThank you for trying", name)