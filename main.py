# TP of Julien Khlaut and Pierre Glandon
from AutoPlaySolitaire import AutoPlaySolitaire
from InteractiveSolitaire import InteractiveSolitaire
from Solitaire import Solitaire

if __name__ == '__main__':
    # Creation of the game
    game = AutoPlaySolitaire()

    # Execution of the game
    N = 5000
    win_count = 0
    for _ in range(N):
        if game.auto_play():
            win_count += 1
        game = AutoPlaySolitaire()

    print(win_count / N * 100)
