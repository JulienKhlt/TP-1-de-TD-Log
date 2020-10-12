from Solitaire import Solitaire


class AutoPlaySolitaire(Solitaire):
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
