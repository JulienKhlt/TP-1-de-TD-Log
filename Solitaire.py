# TP of Julien Khlaut and Pierre Glandon

from Domino import Domino
from random import randint

from DominoExceptions import BadDominoException, BadSumException
from SolitaireState import SolitaireState

class Solitaire:
    """class Solitaire which handles the solitaire. It is based on the class Domino"""

    DEFAULT_NUMBER_DOMINO = 28
    DEFAULT_NUMBER_POINT = 12
    DEFAULT_HAND_SIZE = 7

    def __init__(self, number_domino=DEFAULT_NUMBER_DOMINO,
                 number_point=DEFAULT_NUMBER_POINT,
                 hand_size=DEFAULT_HAND_SIZE):
        """Create the game which possesses the number of dominos in the game
        and the number maximum of cards in the hand, but also which dominoes
        are in the deck or in the hand. And finally a bolean which caracterise the victory"""

        self.number_domino = number_domino
        self.number_point = number_point
        self.hand_size = hand_size
        self.victory = False
        self.deck, self.hand = self.create_deck()
        self.current_state = SolitaireState(self.deck, self.hand, 6)

    def create_deck(self):
        """A function to create the deck and the
        hand without having twice the same domino"""

        id_already_use, deck, hand = [], [], []

        for _ in range(self.number_domino - self.hand_size):

            # We generate a domino and keep its id in id_alread_use
            # then we make sure to ony keep new id

            id = (randint(0, 6), randint(0, 6))
            while id in id_already_use:
                id = (randint(0, 6), randint(0, 6))
            deck.append(Domino(id[0], id[1]))
            id_already_use.append(id)

        for _ in range(self.hand_size):
            id = (randint(0, 6), randint(0, 6))
            while id in id_already_use:
                id = (randint(0, 6), randint(0, 6))
            hand.append(Domino(id[0], id[1]))
            id_already_use.append(id)

        return deck, hand

    def print(self):
        """Printing the dominoes in the hand"""

        for domino in self.hand:
            print(domino)

    def is_game_win(self):
        """Check if the game is won i.e. the deck and the hand are empty"""
        return not self.deck and not self.hand

    def is_game_lost(self):
        """Check if the game is lost"""
        values = [self.hand[i]._lvalue + self.hand[i]._rvalue for i in range(len(self.hand))]
        return not sum_in_list(values, 7, self.number_point)

    def discard(self, discard_set, check=True):
        """Discard cards from hand if discard set is valid (i.e. sum of value is number_point)"""
        if check:
            value = 0
            for domino in discard_set:
                value += domino.get_value

            if value != self.number_point:
                raise BadSumException(self.number_point)

        for domino in discard_set:
            self.hand.remove(domino)

    def draw(self):
        while len(self.hand) < self.hand_size and self.deck:
            self.hand.append(self.deck.pop())

    def play_turn(self, discard_set):
        self.discard(discard_set)
        self.draw()
        self.victory = self.is_game_win()
        self.current_state.update_state(self.deck, self.hand)

    def check_dominos(self, dominos_index_list):
        for domino_index in dominos_index_list:
            self.check_domino(domino_index)

    def check_domino(self, domino_index):
        """Check whether the domino corresponding to DOMINO_INDEX is in the player hand"""
        if domino_index >= len(self.hand) or domino_index < 0:
            raise BadDominoException(domino_index)


def sum_in_list(list, n, sum):
    """Return True if there exists a subset of LIST
    where the sum of its value is equal to SUM. The algorithm is recursive and
    n is the number of numbers in the list we can use
    TODO Make a dynamic programming version of it"""

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




