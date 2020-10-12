from Solitaire import Solitaire


class AutoPlaySolitaire(Solitaire):
    def auto_play(self):
        """Returns a solution, if any. None otherwise"""
        pass

    def auto_play_helper(self):
        if self.is_game_win():
            return True

        discard_sets = self.get_discard_possibilities()
        if not discard_sets:
            return False

        # We make a copy of the deck
        tmp = self.hand[:]

        found_solution = False

        # try every possible discard
        for discard_set in discard_sets:
            self.discard(discard_set)
            self.draw()

            found_solution = found_solution or self.auto_play_helper()
            if found_solution:
                return True

            self.hand = tmp[:]

        return False

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
