import random


# Make a dice throw game
# test comment to show a change...

def main():
    # get input from a keyboard: input("Some kind of prompt: ")
    name = input("What is your name?: ")
    print(f"Hello, {name}!")
    
    # make two individual die rolls
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    
    print(f"You rolled a {dice1} and a {dice2}!")


main()

