from Domino import Domino
from random import randint
from Game import Game

if __name__ == '__main__':
    game = Game(28)

    while not game.victory:

        game.affichage()

        game.round()

        if game.islost():
            print("Vous avez perdu... Dommage !")
            exit(1)

    print("Vous avez gagné ! Bravo !")