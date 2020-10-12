# TP of Julien Khlaut and Pierre Glandon
from AutoPlaySolitaire import AutoPlaySolitaire
from InteractiveSolitaire import InteractiveSolitaire

if __name__ == '__main__':
    # Creation of the game
    game = AutoPlaySolitaire()

    # Execution of the game
    print(game.auto_play_helper())