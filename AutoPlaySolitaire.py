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

        # discard_sets = self.get_discard_possibilities()
        discard_sets = self.get_discard_possibilities_dyn()

        # We make a copy of the deck
        tmp = self.hand[:]

        # try every possible discard
        for discard_set in discard_sets:
            self.play_turn(discard_set, check=False)

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

    def get_discard_possibilities_dyn(self):
        # We begin with the memoisation
        memoization = [[False for i in range (self.number_point + 1)] for i in range(len(self.hand) + 1)]

        # Initialization
        for i in range(len(self.hand)):
            memoization[i][0] = True

        for i in range(1, len(self.hand) + 1):
            for j in range(1, self.number_point + 1):
                if j < self.hand[i - 1].get_value:
                    memoization[i][j] = memoization[i][j - 1]
                else:
                    memoization[i][j] = memoization[i][j - 1] or memoization[i][j - self.hand[i - 1].get_value]

        def solution_rec(i, j, hand):
            if i == 0:
                return [[]]

            results = []
            if memoization[i - 1][j]:
                # We can
                results += solution_rec(i - 1, j, hand)
            if j >= hand[i - 1].get_value and memoization[i - 1][j - hand[i - 1].get_value]:
                # On peut resoudre le pb en prenant cette valeur
                tmp_res = solution_rec(i - 1, j - hand[i - 1].get_value, hand)
                for res in tmp_res:
                    res += [hand[i - 1]]
                results += tmp_res

            return results

        return solution_rec(len(self.hand), self.number_point, self.hand)
