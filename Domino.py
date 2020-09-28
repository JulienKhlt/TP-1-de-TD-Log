class Domino:
    """Insert Docstring
        Dominos must be uneven and squared."""
    
    DISPLAY_SYMBOL = '*'
    DISPLAY_FORMATTER = {
        0: {},
        1: {(2, 3): DISPLAY_SYMBOL},
        2: {(1, 1): DISPLAY_SYMBOL, (3, 5): DISPLAY_SYMBOL},
        3: {(1, 1): DISPLAY_SYMBOL, (2, 3): DISPLAY_SYMBOL, (3, 5): DISPLAY_SYMBOL},
        4: {(1, 1): DISPLAY_SYMBOL, (1, 5): DISPLAY_SYMBOL, (3, 1): DISPLAY_SYMBOL, (3, 5): DISPLAY_SYMBOL},
        5: {(1, 1): DISPLAY_SYMBOL, (1, 5): DISPLAY_SYMBOL, (2, 3): DISPLAY_SYMBOL, (3, 1): DISPLAY_SYMBOL, (3, 5): DISPLAY_SYMBOL},
        6: {(1, 1): DISPLAY_SYMBOL, (1, 3): DISPLAY_SYMBOL, (1, 5): DISPLAY_SYMBOL, (3, 1): DISPLAY_SYMBOL, (3, 3): DISPLAY_SYMBOL, (3, 5): DISPLAY_SYMBOL}
    }
    
    DEFAULT_HEIGHT = 3
    DEFAULT_WIDTH = 3
    DEFAULT_SIZE = 3

    def generate_pattern(self, value, size):
        """
        Generate the pattern of the domino for a given value.
        Returns a list of location (i, j) where something should be
        drawn to display the domino.
        """

        assert size % 2 == 1

        if size <= 1:
            return []

        if value % 2 == 1:
            return [(0, 0)] + self.generate_pattern(value - 1, size)

        pattern = []

        pattern_normalized = self.generate_normalized_pattern(value)
        pattern += self.expand_pattern(pattern_normalized, size)
        return pattern + self.generate_pattern(value - 8, size - 2)


    def linear_to_circular_one_round(self, linear_value, round_border_size):
        round_size = round_border_size * round_border_size
        # otherwise it means that it does more than one round
        assert linear_value < round_size

        quarter_round_count = linear_value // (round_border_size - 1)
        line_rest = linear_value % (round_border_size - 1)

        if quarter_round_count == 0:
            return line_rest, 0
        if quarter_round_count == 1:
            return round_border_size - 1, line_rest
        if quarter_round_count == 2:
            return round_border_size - 1 - line_rest, round_border_size - 1
        return 0, round_border_size - 1 - line_rest

    def linear_to_circular(self, linear_value):
        full_round_size = self.size * self.size
        round_count = linear_value // full_round_size
        round_rest = linear_value % full_round_size

        local_i, local_j = self.linear_to_circular_one_round(round_rest, self.size - 2 * round_count)
        return local_i + round_count, local_j + round_count
    #
    # def generate_pattern(self, case_value):
    #     """
    #     Generate the pattern of the domino for a given value.
    #     Returns a list of location (i, j) where something should be
    #     drawn to display the domino.
    #     """
    #
    #     assert 0 <= case_value and case_value <= self.size ** 2
    #
    #     if (self.size % 2 == 1):
    #         if case_value % 2 == 1:
    #             return [((self.size - 1) // 2, (self.size - 1) // 2)] + self.generate_pattern(case_value - 1)
    #         pattern = []
    #         if case_value > 0:
    #             multiplier = (self.size * self.size - 1) // case_value
    #         for i in range(case_value):
    #             pattern.append(self.linear_to_circular(i * multiplier))
    #
    #         return pattern

    def generate_display_list(self):
        display_string = []
        for i in range(self.size):
            for j in range(self.size):
                display_string += [" "]
            display_string += ["\n"]

        return display_string

    def generate_display_string(self, value):
        display_list = self.generate_display_list()
        pattern = self.generate_pattern(value, self.size)

        for (i, j) in pattern:
            string_position = self.grid_position_to_string_position(i, j)
            display_list[string_position] = "*"

        return ''.join(display_list)

    def grid_position_to_string_position(self, position_i, position_j):
        position_i += self.size - 2
        position_j += self.size - 2



        return position_i + position_j * (self.size + 1)

    def __init__(self, l_value, r_value):
        self.l_value = l_value
        self.r_value = r_value
        self.size = Domino.DEFAULT_SIZE
    
    # TODO : remplacer par fonction __str__


    def generate_normalized_pattern(self, value):
        pattern = []

        if value >= 2:
            pattern += [(-1, -1), (1, 1)]
        if value >= 4:
            pattern += [(1, -1), (-1, 1)]
        if value >= 6:
            pattern += [(0, -1), (0, 1)]
        if value >= 8:
            pattern += [(-1, 0), (1, 0)]

        return pattern

    def expand_pattern(self, pattern_normalized, size):
        pattern = []

        for (i, j) in pattern_normalized:
            pattern.append(((size - 2) * i, (size - 2) * j))

        return pattern
