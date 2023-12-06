"""
This file is to invoke the three_level_game.
============================
Course: CS 5001
Semester: Fall 2023
Student: Xin Deng
"""
from three_level_game import ascii_game, rock_paper_scissors, guess_number

def main():
    """
    Main driver for the three_level_game.
    1. first play the ASCII game, have 1 chance.
    2. second play the rock_paper_scissors game, have 3 chances.
    3. third play the guess number game, have 7 chances.

    """
    # Play ASCII game
    if ascii_game():
        print("Congratulations on passing the ASCII game!\n")
    else:
        print("Game over in ASCII game. Try again later.")
        return

    # Play Rock-Paper-Scissors
    for attempt in range(3): 
        user_choice = input("Please enter your choice from rock, paper, and scissors: ").lower()
        result, computer_choice = rock_paper_scissors(user_choice)
        if "Invalid input" in result:
            print("Invalid input. Please choose either rock, paper, or scissors.")
            continue
        elif "Win" in result:
            print("Well done on winning Rock-Paper-Scissors!\n")
            break
        elif attempt < 2:
            print(f"Lose: {computer_choice} beats {user_choice}. Try again.")
        else:
            print(f"Lose: {computer_choice} beats {user_choice}. Game over in Rock-Paper-Scissors.")
            return

    # Play the Guess Number game
    if guess_number():
        print("Great job on guessing the number!")
    else:
        print("Game over in Guess the Number. Try again later.")

if __name__ == "__main__":
    main()
