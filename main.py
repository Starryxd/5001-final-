from ASCII import ascii
from rock_paper_scissors import rock_paper_scissors
from guess_num import guess_number

def play_games():
    if ascii():
        print("Congratulations on passing the ASCII game!\n")
    else:
        print("Game over in ASCII game. Try again later.")
        return

    # Next, play Rock-Paper-Scissors
    if rock_paper_scissors():
        print("Well done on winning Rock-Paper-Scissors!\n")
    else:
        print("Game over in Rock-Paper-Scissors. Try again later.")
        return

    # Finally, the Guess the Number game
    if guess_number():
        print("Great job on guessing the number!")
    else:
        print("Game over in Guess the Number. Try again later.")

play_games()
