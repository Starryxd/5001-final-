# Final Project Report

* Student Name: Xin Deng
* Github Username: Starryxd
* Semester: Fall 2023
* Course: CS5001



## Description 
For my final project, I am planning to use Python to create a game that includes three levels, each featuring a different mini-game. The first mini-game will be about guessing animals from ASCII Art, the second will be a classic rock-paper-scissors game, and the final mini-game will involve guessing numbers. 


## Key Features
* ASCII Art
* boolean
* while/for loop
* function

## Guide
There will have a file of the three mini-games and a main file to run the game. The client will use the main file to playing this game.


## Installation Instructions
If we wanted to run this project locally, what would we need to do?  If we need to get API key's include that information, and also command line startup commands to execute the project. If you have a lot of dependencies, you can also include a requirements.txt file, but make sure to include that we need to run `pip install -r requirements.txt` or something similar.

## Code Review
This is the function of first game ASCII game. It will ask user to guess the name of the animal it randomly shows.
```python
def ascii_game(guess= None) -> bool:
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
```
This is the function of second game. It will ask user to enter paper, rock,or scissors to play the game with computer.
```python
def rock_paper_scissors(user_choice: str, attempt_limit: int = 3) -> tuple:
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

    return f"You've run out of attempts", computer_choice
```
This is the function of third game. It will ask user to guess number in range of 1 to 100.
```python
def guess_number(min_num: int = 1, max_num: int = 100, max_attempts: int = 7) -> bool:      
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
```

### Major Challenges
Key aspects could include pieces that your struggled on and/or pieces that you are proud of and want to show off.
Different games might have different requirement for input validation and error handling. I need to consider as much as possible the user might be entered. The strategy I adopt is to print error message to user if they type in invalidation input. For example, in rock_paper_scissors game, if the user's input isn't paper, rock or scissors, it will print "Invalid input. Please choose either rock, paper, or scissors." In guess number game, if the user's input is not an integer, it will print "Invalid input: Please enter a valid number."

## Example Runs
Explain how you documented running the project, and what we need to look for in your repository (text output from the project, small videos, links to videos on youtube of you running it, etc)
Guess what the animal is in the picture

                        |\    o
                       |  \    o
                   |\ /    .\ o
                   | |       (
                   |/ \     /
                       |  /
                        |/
            
Please enter your guess: fish
You're correct!
Congratulations on passing the ASCII game!

Please enter your choice from rock, paper, and scissors: paper
Well done on winning Rock-Paper-Scissors!

Attempt 1/7 - Enter your guess between 1 and 100: 50
Higher: The number is higher than your guess.
Attempt 2/7 - Enter your guess between 1 and 100: 75
Lower: The number is lower than your guess.
Attempt 3/7 - Enter your guess between 1 and 100: 63
Lower: The number is lower than your guess.
Attempt 4/7 - Enter your guess between 1 and 100: 56
Higher: The number is higher than your guess.
Attempt 5/7 - Enter your guess between 1 and 100: 60
Higher: The number is higher than your guess.
Attempt 6/7 - Enter your guess between 1 and 100: 62
Congrats! You guessed the correct number 62 in 6 attempts.
Great job on guessing the number!

## Testing
How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission.
I write a test file for the function named test_three_level_game.py. And the main file is invoked the game.

The test of ascii_game. 
```python
def test_ascii_game():
    test_cases = ["rabbit", "dog", "fish", "cat"]
    for guess in test_cases:
        print(f"Testing with guess: '{guess}'")
        result = ascii_game(guess)
        print(f"Result: {'Correct' if result else 'Incorrect'}\n")
```
The test of rock_paper_scissors.
```python
def test_rock_paper_scissors():
    test_cases = ["rock", "paper", "scissors", "dfjdsf"]
    for user_choice in test_cases:
        print(f"Testing with user choice: '{user_choice}'")
        result, computer_choice = rock_paper_scissors(user_choice)
        print(f"Computer's choice: '{computer_choice}'")
        print(f"Result: {result}\n")
```
The test of guess number game.
```python
def test_guess_number():
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
```

## Missing Features / What's Next
Due to limitations in knowledge, many ideas have not yet been realized. Currently, the games I design use relatively basic Python syntax and methods. How to further upgrade the game is something I would like to explore in the future. In terms of game upgrades, perhaps some dynamic games can be added. Increase the playability and fun of the game. In addition, in terms of appearance, some design animations can be added, such as an interesting start button. It also can add some background music to the game, etc.

## Final Reflection
In this intensive course, I learned a lot about the basics of Python. I gained a deeper understanding of Python's syntax and fundamental concepts, such as the types of variables, the application of functions, and the basic structure of data. The weekly assignments were particularly helpful in reinforcing the content covered each week. Among everything I learned, I believe the most significant change was in my programming mindset. I realized that what seems like a large project is actually composed of many small modules. Breaking down large problems into smaller ones and connecting them together is the way of thinking I learned in this course. This will help me to think about problems more rationally and calmly in my future learning.