from Solitaire import Solitaire


class InteractiveSolitaire(Solitaire):
    def turn(self):
        """This is a function that handles a turn in the solitaire's game"""

        # We choose which dominoes are going to be removed
        # and we sort them from the bigger to the smaller
        num_domino = sorted(input("Choose the number of the dominos to remove "), reverse=True)

        # Then we check if the sum of dominoes selected is indeed the number_point (12 normally)
        sum = 0
        for i in range(len(num_domino)):
            sum += self.hand[int(num_domino[i]) - 1]._lvalue + self.hand[int(num_domino[i]) - 1]._rvalue

        if sum == self.number_point:
            for i in range(len(num_domino)):
                del (self.hand[int(num_domino[i]) - 1])
                self.is_game_win()
        else:
            print(f"The sum of the dominos selected is not equal to {self.number_point}. Try again")

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