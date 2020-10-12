class SolitaireState:
    """A hash key generated form the current state of a solitaire game.
    The state is defined by the deck and hand."""

    def __init__(self, deck, hand, max_value):
        self.deck = sorted(deck)
        self.hand = sorted(hand)

        # The hashing function depends of the size of the deck
        self.state_size = len(self.deck) + len(self.hand)
        # Important bc the hashing function is gonna count in that base
        self.max_value = max_value

    def __eq__(self, other_state):
        if len(self.deck) != len(other_state.deck) or len(self.hand) != len(other_state.hand):
            return False

        for domino in self.deck:
            if domino not in other_state.deck:
                return False

        for domino in self.hand:
            if domino not in other_state.hand:
                return False

        return True

    def update_state(self, deck, hand):
        self.deck = sorted(deck)
        self.hand = sorted(hand)
        self.state_size = len(self.hand) + len(self.deck)

    @staticmethod
    def hash_2(x, y):
        return x + (x + y) * (x + y + 1) / 2

    @staticmethod
    def hash_3(x, y, z):
        return SolitaireState.hash_2(SolitaireState.hash_2(x, y), z)

    @staticmethod
    def hash(int_list):
        """Bijection between N^len(int_list) and N
            Should work because we split the state in size
            before hashing them and the size of the hand is fixed."""
        if len(int_list) == 1:
            return SolitaireState.hash_2(int_list[0].rvalue, int_list[0].lvalue)

        return SolitaireState.hash_3(int_list[0].rvalue, int_list[0].lvalue, SolitaireState.hash(int_list[1:]))

    def __hash__(self):
        """Returns a unique identifier between 0 and max_value ** #(deck + hand)"""
        hash_value = 0
        full_list = self.deck + self.hand

        for index, domino in enumerate(full_list):
            hash_value += (self.max_value ** index) * domino.rvalue + (self.max_value ** (index + 1)) * domino.lvalue

        return hash_value