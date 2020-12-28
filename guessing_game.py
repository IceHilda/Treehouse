"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    print("Welcome to the guessing game!")
    answer = random.randint(1, 10)
    guessing = True
    guess_count = 1
    while guessing is True:
        try:
            guess = int(input("What is your guess? (1-10)  "))
            if guess < answer:
                print("It's higher")
                guess_count += 1
            elif guess > answer:
                print("It's lower")
                guess_count += 1
            else:
                guessing = False
                print("Got it, you win! It took you {} guesses! Thanks for playing! Game over.".format(guess_count))
        except:
            pass


# Kick off the program by calling the start_game function.
start_game()