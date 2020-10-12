# TP of Julien Khlaut and Pierre Glandon

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
            display_list[list_position_i, 2 * list_position_j] = Domino.DISPLAY_SYMBOL

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
        canvas.insert(1, 2 * self._size + 1, display_rvalue)

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
            for j in range(1, 2 * self._size):
                canvas[i, j] = '-'
            canvas[i, 2 * self._size] = '|'
            for j in range(2 * self._size + 1, 4 * self._size + 1):
                canvas[i, j] = '-'
            canvas[i, -1] = '+'

        for j in [0, 2 * self._size, 4 * self._size]:
            for i in range(1, self._size + 1):
                canvas[i, j] = '|'

        # Domino.DISPLAY_CANVAS_LIST[self._size] = copy.copy(canvas)
        return canvas

    def __init__(self, l_value, r_value, size=DEFAULT_SIZE):
        # Once set those values shouldn't be modified.
        check_half_domino(l_value)
        check_half_domino(r_value)
        self._lvalue = l_value
        self._rvalue = r_value
        self._size = int(size)

    @property
    def lvalue(self):
        return self._lvalue

    @property
    def rvalue(self):
        return self._rvalue

    @property
    def get_value(self):
        return self._rvalue + self._lvalue

    @staticmethod
    def generate_normalized_pattern(value):
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

    @staticmethod
    def expand_pattern(pattern_normalized, size):
        """Takes a normalized 3x3 patterns and turns it into an equivalent value size x size pattern"""
        pattern = []

        for (i, j) in pattern_normalized:
            pattern.append(((size // 2) * i, (size // 2) * j))

        return pattern

    def __repr__(self):
        return f"Domino({self._lvalue}, {self._rvalue})"

    def __eq__(self, other):
        return self.lvalue == other.lvalue and self.rvalue == other.rvalue

    def __ne__(self, other):
        return self.lvalue != other.lvalue or self.rvalue != other.rvalue

    def __lt__(self, other):
        return self.lvalue < other.lvalue or self.rvalue < other.lvalue


class Correct_Half_Domino(Exception):
    def __init__(self, n):
        super().__init__()
        self._value = n

    @property
    def value(self):
        return self._value

    def __str__(self):
        return f"Half domino's value is not correct : '{self._value}'. It has to be an integer between 0 and 6"


def check_half_domino(value):
    if type(value) != int or value > 6 or value < 0:
        raise Correct_Half_Domino(value)
