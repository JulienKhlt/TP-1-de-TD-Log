from Solitaire import Solitaire


class InteractiveSolitaire(Solitaire):
    def turn(self):
        """This is a function that handles a turn in the solitaire's game"""

        # We choose which dominoes are going to be removed
        # and we sort them from the bigger to the smaller
        num_domino = list(input("Choose the number of the dominos to remove "))
        dominos_to_discard = [self.hand[int(i) - 1] for i in num_domino]

        try:
            self.discard(dominos_to_discard)
            self.draw()
            self.is_game_win()
        except ValueError:
            print(f"The sum of the dominos selected is not equal to {self.number_point}. Try again")
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
