"""
This file is code of Fisrt game ASCII Arts.
============================
Course: CS 5001
Student: Xin Deng
"""
import random

ascii_art = {
    "rabbit" : """
                        //
                       ('>
                       /rr
                      *\))_
             """,
    "dog" : """
                   o'')}____//
                    `_/      )
                    (_(_/-(_/
            """,
    "fish" : """
                        |\    o
                       |  \    o
                   |\ /    .\ o
                   | |       (
                   |/ \     /
                       |  /
                        |/
            """
}


def ascii():
    """
    This function is design for a ASCII art guessing game.
    It will randomly show the art for client and the client will answer what the animal shows in the art it is.
    """
    dic = list(ascii_art.items())
    random_art = random.choice(dic)
    name = random_art[0]
    art = random_art[1]
    print("Guess what the animal is in the picture")
    print(art)
    guess = input("Please enter your guess: ").lower()
    if guess == name:
        print("You're correct!")
        return True
    else:
        print("Sorry, you're wrong.")
        return False



