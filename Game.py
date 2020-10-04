# TP of Julien Khlaut and Pierre Glandon

from Domino import Domino
from random import randint

class Game:
    """class Game which handles the solitaire. It is based on the class Domino"""

    def __init__(self, number_domino = 28, number_point = 12):
        """Create the game which possesses the number of dominos in the game
        and the number maximum of cards in the hand, but also which dominoes
        are in the deck or in the hand. And finally a bolean which caracterise the victory"""

        self.number_domino = number_domino
        self.number_point = number_point
        self.victory = False
        self.deck, self.hand = self.create_deck()

    def create_deck(self):
        """A function to create the deck and the
        hand without having twice the same domino"""

        id_already_use, deck, hand = [], [], []

        for _ in range(self.number_domino - 7):

            # We generate a domino and keep its id in id_alread_use
            # then we make sure to ony keep new id

            id = (randint(0, 6), randint(0, 6))
            while id in id_already_use:
                id = (randint(0, 6), randint(0, 6))
            deck.append(Domino(id[0], id[1]))
            id_already_use.append(id)

        for _ in range(7):
            id = (randint(0, 6), randint(0, 6))
            while id in id_already_use:
                id = (randint(0, 6), randint(0, 6))
            hand.append(Domino(id[0], id[1]))
            id_already_use.append(id)

        return deck, hand

    def affichage(self):
        """Printing the dominoes in the hand"""

        for domino in self.hand:
            print(domino)

    def round(self):
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
                if len(self.deck) != 0:
                    domino = self.deck.pop()
                    self.hand.append(domino)
                else:
                    if len(self.hand) == 0:
                        self.victory = True
        else:
            print(f"The sum of the dominos selected is not equal to {self.number_point}. Try again")

        print(f"It remains {len(self.deck)} dominos in the deck and {len(self.hand)} in you hand")

    def islost(self):
        """Check if the game is lost"""
        values = [self.hand[i]._lvalue + self.hand[i]._rvalue for i in range(len(self.hand))]
        return not sum_in_list(values, 7, self.number_point)

    def play_game(self):
        """Manage the game"""
        while not self.victory:

            if self.islost():
                print("You have lost... Too bad !")
                exit(0)

            self.affichage()

            self.round()

        print("You have won ! Congratulation !")


def sum_in_list(list, n, sum):
    """Return a bolean the caracterise the defeat,
    we check if we can make the sum which the numbers
    that are in the list. The algorithm is recursive and
    n is the number of numbers in the list we can use"""

    # Initialisation
    if (sum == 0):
        return True
    if (n == 0):
        return False

    # Recursion : if the last item is bigger than the sum.
    if (list[n - 1] > sum):
        return sum_in_list(list, n - 1, sum)

    # Then there are two possibilities whether
    # we use the last number in the list or not
    # the recursion stop when the sum is null
    # or when there is no more number.
    return sum_in_list(list, n - 1, sum) or sum_in_list(list, n - 1, sum - list[n - 1])