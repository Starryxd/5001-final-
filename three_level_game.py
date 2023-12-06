"""
This file is code of Fisrt game ASCII Arts.
============================
Course: CS 5001
Semester: Fall 2023
Student: Xin Deng
"""
import random

ascii_art = {
    "rabbit": """
                        //
                       ('>
                       /rr
                      *\))_
             """,
    "dog": """
                   o'')}____//
                    `_/      )
                    (_(_/-(_/
            """,
    "fish": """
                        |\    o
                       |  \    o
                   |\ /    .\ o
                   | |       (
                   |/ \     /
                       |  /
                        |/
            """
}


def ascii_game(guess=None) -> bool:
    """
        This function is select ASCII art from ascii_art randomly.
        It requires user to guess what animal is it of the ASCII art.

    Example:
        >>> ascii()
            Guess what the animal is in the picture: rabbit
                    //
                    ('>
                    /rr
                    *\))_
            Please enter your guess: rabbit
            You're correct!
            Congratulations on passing the ASCII game!

    Args:
        guess (): This is for user to enter their guess.

    Returns:
        bool: True the user's guess the is the name of the animal.
    """
    dic = list(ascii_art.items())
    random_art = random.choice(dic)
    name = random_art[0]
    art = random_art[1]
    print("Guess what the animal is in the picture")
    print(art)
    if not guess:
        guess = input("Please enter your guess: ").lower()
    else:
        guess = guess.lower()
    if guess == name:
        print("You're correct!")
        return True
    else:
        print("Sorry, you're wrong.")
        return False


def rock_paper_scissors(user_choice: str, attempt_limit: int = 3) -> tuple:
    """
        This function is the game of rock_paper_scissors.
        It requires user to choose from rock, papar and scissors.
        And this is the game that user against computer.

    Example:
        >>> rock_paper_scissors()
            Please enter your choice from rock, paper, and scissors: paper
            Lose: scissors beats paper. Try again.
            Please enter your choice from rock, paper, and scissors: paper
            Well done on winning Rock-Paper-Scissors!

    Args:
        user_choice (str): This is for user to enter their choice.
        attempt_limit (int): The limit of attempt is default to 3.

    Returns:
        tuple: True the user's guess is the name of the animal.
    """
    choices = ["rock", "paper", "scissors"]
    attempts = 0
    computer_choice = None
    while attempts < attempt_limit:
        computer_choice = random.choice(choices)
        attempts += 1

        if user_choice not in choices:
            return "Invalid input,please enter your choice from rock, paper and scissor", computer_choice

        if user_choice == computer_choice:
            return f"It's a tie: Both chose {user_choice}", computer_choice
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            return f"You are Winner: {user_choice} beats {computer_choice}", computer_choice
        else:
            return f"Sorry, you lose: {computer_choice} beats {user_choice}", computer_choice

    return "You've run out of attempts", computer_choice 


def guess_number(min_num: int = 1, max_num: int = 100, max_attempts: int = 7) -> bool:
    """
        This is a function of guessing number game in range of 1 to 100.
        There are 7 attempts chance for user.
        This is also a game guarantee win if the user choose binary way to solve it.
    Example:
        Attempt 1/7 - Enter your guess between 1 and 100: 50
        Higher: The number is higher than your guess.
        Attempt 2/7 - Enter your guess between 1 and 100: 75
        Lower: The number is lower than your guess.
        Attempt 3/7 - Enter your guess between 1 and 100: 63
        Higher: The number is higher than your guess.
        Attempt 4/7 - Enter your guess between 1 and 100: 69
        Higher: The number is higher than your guess.
        Attempt 5/7 - Enter your guess between 1 and 100: 72
        Lower: The number is lower than your guess.
        Attempt 6/7 - Enter your guess between 1 and 100: 70
        Congrats! You guessed the correct number 70 in 6 attempts.
        Great job on guessing the number!

    Args:
        min_num (int): The lower bound of the range. Default is 1.
        max_num (int): The upper bound of the range. Default is 100.
        max_attempts (int): The maximum number of attempts the user is allowed. Default is 7.

    Returns:
        bool: True if the user guesses the number correctly within the allowed attempts, False otherwise.
    """
    secret_num = random.randint(min_num, max_num)
    attempts = 0

    while attempts < max_attempts:
        attempts += 1
        try:
            guess = int(input(f"Attempt {attempts}/{max_attempts} - Enter your guess between {min_num} and {max_num}: "))
        except ValueError:
            print("Invalid input: Please enter a valid number.")
            continue

        if guess < secret_num:
            print("Higher: The number is higher than your guess.")
        elif guess > secret_num:
            print("Lower: The number is lower than your guess.")
        else:
            print(f"Congrats! You guessed the correct number {secret_num} in {attempts} attempts.")
            return True

    print(f"No more attempts. The correct number was {secret_num}.")
    return False
