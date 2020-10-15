from DominoExceptions import BadSumException, BadDominoException
from Solitaire import Solitaire


class InteractiveSolitaire(Solitaire):
    def turn(self):
        """This is a function that handles a turn in the solitaire's game"""

        # We choose which dominoes are going to be removed
        # and we sort them from the bigger to the smaller
        num_domino = list(input("Choose the number of the dominos to remove "))
        try:
            num_domino = [int(i) - 1 for i in num_domino]
        except ValueError:
            print("Please enter a sequence of int! (ex: 145 to select dominos 1, 4 and 5)")
            return

        dominos_to_discard = [self.hand[i] for i in num_domino]

        try:
            self.check_dominos(num_domino)
            self.play_turn(dominos_to_discard)
        except BadSumException as bad_sum:
            print(bad_sum)
        except BadDominoException as bad_domino:
            print(bad_domino)
        finally:
            print(f"It remains {len(self.deck)} dominos in the deck and {len(self.hand)} in you hand")

    def play(self):
        """Manage the game"""
        while not self.victory:

            if self.is_game_lost():
                print("You have lost... Too bad !")
                exit(0)

            self.print()

            self.turn()

        print("You have won ! Congratulation !")
