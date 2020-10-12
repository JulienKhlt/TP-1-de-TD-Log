from DominoExceptions import EndGameException
from Solitaire import Solitaire


class AutoPlaySolitaire(Solitaire):

    TESTED_SOLUTION = {}
    MATCH_COUNT = 0

    def auto_play(self):
        """TODO Returns a solution, if any. None otherwise"""

        try:
            self.auto_play_helper()
        except EndGameException:
            return True
        return False

    def auto_play_helper(self):
        """Raise an EndGameException if a solution exists."""

        discard_sets = self.get_discard_possibilities()

        # We make a copy of the deck
        tmp = self.hand[:]

        # try every possible discard
        for discard_set in discard_sets:
            self.play_turn(discard_set)

            if self.victory:
                raise EndGameException

            if self.current_state.state_size not in AutoPlaySolitaire.TESTED_SOLUTION:
                AutoPlaySolitaire.TESTED_SOLUTION[self.current_state.state_size] = {}

            current_state_size = self.current_state.state_size
            current_state_hash = self.current_state.__hash__()

            if current_state_hash not in AutoPlaySolitaire.TESTED_SOLUTION[current_state_size]:
                try:
                    self.auto_play_helper()
                except EndGameException:
                    AutoPlaySolitaire.TESTED_SOLUTION[current_state_size][current_state_hash] = True
                    raise EndGameException
                AutoPlaySolitaire.TESTED_SOLUTION[current_state_size][current_state_hash] = False
            else:
                AutoPlaySolitaire.MATCH_COUNT += 1
                if AutoPlaySolitaire.TESTED_SOLUTION[current_state_size][current_state_hash]:
                    raise EndGameException
            self.hand = tmp[:]

    def get_discard_possibilities(self):
        """Returns a list containing the sets that can be discarded."""
        result = []
        self.get_discard_possibilities_rec(self.hand, [], self.number_point, result)

        return result

    def get_discard_possibilities_rec(self, deck_rest, deck_used, total_value, results_set):
        """Make the recursive computation of the function above."""

        # Initialisation
        if total_value == 0:
            results_set += [deck_used]
            return
        if not deck_rest or total_value < 0:
            return

        # Then there are two possibilities whether
        # we use the last number in the list or not
        # the recursion stop when the sum is null
        # or when there is no more number.
        self.get_discard_possibilities_rec(deck_rest[:-1], deck_used + [deck_rest[-1]],
                                           total_value - deck_rest[-1].get_value, results_set)
        self.get_discard_possibilities_rec(deck_rest[:-1], deck_used, total_value, results_set)
