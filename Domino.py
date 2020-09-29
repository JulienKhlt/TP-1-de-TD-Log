import copy

from MutableString import MutableString


class Domino:
    """Insert Docstring
        Dominos size must uneven be and squared."""
    DEFAULT_SIZE = 3
    DISPLAY_SYMBOL = '*'

    def generate_pattern(self, value, size):
        """
        Generate the pattern of the domino for a given value.
        Returns a list of location (i, j) where something should be
        drawn to display the domino.
        """

        assert size % 2 == 1

        if size <= 1 or value <= 0:
            return []

        # if size in Domino.DISPLAY_PATTERN.keys() and value in Domino.DISPLAY_PATTERN[size]:
        #     return copy.copy(Domino.DISPLAY_PATTERN[size][value])

        if value % 2 == 1:
            return [(0, 0)] + self.generate_pattern(value - 1, size)

        pattern = []

        # We build a pattern for 3x3 domino
        pattern_normalized = self.generate_normalized_pattern(value)
        # We expand it for the correct size
        pattern += self.expand_pattern(pattern_normalized, size)
        # We generate the interior of the pattern recursively
        full_pattern = pattern + self.generate_pattern(value - 8, size - 2)

        # if size not in Domino.DISPLAY_PATTERN.keys():
        #     Domino.DISPLAY_PATTERN[size] = {}
        # Domino.DISPLAY_PATTERN[size][value] = copy.copy(full_pattern)

        return full_pattern

    def generate_string_for_value(self, value):
        """
        Generate a string representation of half a Domino (whithout canvas).
        """
        display_list = MutableString()
        pattern = self.generate_pattern(value, self._size)

        for (i, j) in pattern:
            list_position_i, list_position_j = self.transform_pattern_coord_to_list_coord(i, j)
            display_list[list_position_i, list_position_j] = Domino.DISPLAY_SYMBOL

        return display_list

    def transform_pattern_coord_to_list_coord(self, position_i, position_j):
        """Transform the coordinate for patterns into list coordinate for string representation"""
        position_i += self._size // 2
        position_j += self._size // 2

        return position_i, position_j

    def __str__(self):
        display_rvalue = self.generate_string_for_value(self._rvalue)
        display_lvalue = self.generate_string_for_value(self._lvalue)
        canvas = self.generate_canvas()

        canvas.insert(1, 1, display_lvalue)
        canvas.insert(1, self._size + 2, display_rvalue)

        return str(canvas)

    def generate_canvas(self):
        """
        Generate the canvas to display the domino.
        Returns a MutableString
        """

        # if self._size in Domino.DISPLAY_CANVAS_LIST.keys():
        #     return copy.copy(Domino.DISPLAY_CANVAS_LIST[self._size])

        canvas = MutableString()
        for i in [0, self._size + 1]:
            # We generate top/bottom border
            canvas[i, 0] = '+'
            for j in range(1, self._size + 1):
                canvas[i, j] = '-'
            canvas[i, self._size + 1] = '|'
            for j in range(self._size + 2, 2 * self._size + 3):
                canvas[i, j] = '-'
            canvas[i, -1] = '+'

        for j in [0, self._size + 1, 2 * self._size + 2]:
            for i in range(1, self._size + 1):
                canvas[i, j] = '|'

        # Domino.DISPLAY_CANVAS_LIST[self._size] = copy.copy(canvas)
        return canvas

    def __init__(self, l_value, r_value, size=DEFAULT_SIZE):
        # Once set those values shouldn't be modified.
        self._lvalue = l_value
        self._rvalue = r_value
        self._size = size

    def generate_normalized_pattern(self, value):
        """Generate a 3x3 pattern for the given value, useful to generate higher value pattern by expanding it."""
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
        """Takes a normalized 3x3 patterns and turns it into an equivalent value size x size pattern"""
        pattern = []

        for (i, j) in pattern_normalized:
            pattern.append(((size // 2) * i, (size // 2) * j))

        return pattern
