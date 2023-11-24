"""
This file is code of the Third game Guessing number.
============================
Course: CS 5001
Student: Xin Deng
"""
import random

def guess_number():
    min_num = 1
    max_num = 100
    max_attempts = 5

    secret_num = random.randint(min_num, max_num)
    print(f"Guess the number between {min_num} and {max_num}.")

    attempts = 0

    while attempts < max_attempts:
        attempts += 1
        try:
            guess = int(input("Please enter your guess: "))
        except ValueError:
            print("Please enter a valid numeber.")
            continue
        if guess < secret_num:
            print("The number is lower than secret number. Please try again.")
        elif guess > secret_num:
            print("The number is higher than secret number. Please try again.")
        else:
            print("Congrats! You guessed the correct number!")
            return True
    else:
        print(f"You've run out of attempts. The correct number is {secret_num}")
        return False
    
