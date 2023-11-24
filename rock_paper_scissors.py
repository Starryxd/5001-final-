"""
This file is code of the Second game Rock-Paper-Scissors.
============================
Course: CS 5001
Student: Xin Deng
"""
import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        attempts += 1
        computer_choice = random.choice(choices)
        user_choice = input(f"{attempts} out of {max_attempts}.Please enter your choice from rock, paper and scissors: ").lower()

        if user_choice not in choices:
            print("Invalid input, please enter your choice from rock, paper and scissors.")

        if user_choice == computer_choice:
            print(f"It's a tie! Both are choose {user_choice}.")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
             print(f"You are Winner! User choice {user_choice} beats computer choice {computer_choice}")
             return True
        else:
            print(f"Sorry, you lose. Computer choice {computer_choice} beats user choice {user_choice}")
    
    print("You've run out of attempts.")
    return False

