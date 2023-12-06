"""
This file is a test file of three_level_game.py.
============================
Course: CS 5001
Semester: Fall 2023
Student: Xin Deng
"""
from three_level_game import ascii_game, rock_paper_scissors, guess_number
from unittest.mock import patch


def test_ascii_game():
    """test ascii with hypothetical input that user will type in.

    Returns:
        None
    """
    test_cases = ["rabbit", "dog", "fish", "cat"]
    for guess in test_cases:
        print(f"Testing with guess: '{guess}'")
        result = ascii_game(guess)
        print(f"Result: {'Correct' if result else 'Incorrect'}\n")


def test_rock_paper_scissors():
    """test the rock_paper_scissors with hypothetical input that user will type in.

    Returns:
        None
    """
    test_cases = ["rock", "paper", "scissors", "dfjdsf"]
    for user_choice in test_cases:
        print(f"Testing with user choice: '{user_choice}'")
        result, computer_choice = rock_paper_scissors(user_choice)
        print(f"Computer's choice: '{computer_choice}'")
        print(f"Result: {result}\n")


def test_guess_number():
    """test the guess_number with hypothetical input that user will type in.

    Returns:
        None
    """
    # Test with correct guess in the range of attempts limit.
    with patch('builtins.input', side_effect=['50', '75', '87', '93', '96', '97']), \
         patch('random.randint', return_value=97):
        assert guess_number() == True, "Test failed: Correct guess should return True"

    # Test with incorrect guesses in all 7 attempts
    with patch('builtins.input', side_effect=['10', '20', '30', '40', '50', '60', '70']), \
         patch('random.randint', return_value=97):
        assert guess_number() == False, "Test failed: Incorrect guesses should return False"

    # Test for handling non-integer input, then correct guess on 7th attempt
    with patch('builtins.input', side_effect=['invalid', '10', '20', '30', '40', '50', '97']), \
         patch('random.randint', return_value=97):
        assert guess_number() == True, "Test failed: Should handle non-integer input and continue"


if __name__ == "__main__":
    test_ascii()
    test_rock_paper_scissors()
    test_guess_number()
