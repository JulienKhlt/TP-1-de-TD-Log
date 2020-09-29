from MutableString import MutableString


class Domino:
    """Insert Docstring
        Dominos must be uneven and squared."""
    DEFAULT_SIZE = 3
    DISPLAY_SYMBOL = '*'
    # Store the blank pattern for a given size of Domino
    DISPLAY_LIST = {}
    # Store the pattern for a given size and value
    DISPLAY_PATTERN = {}
    DISPLAY_CANVAS_LIST = {}
    DISPLAY_STRING = {}

    def generate_pattern(self, value, size):
        """
        Generate the pattern of the domino for a given value.
        Returns a list of location (i, j) where something should be
        drawn to display the domino.
        """

        assert size % 2 == 1

        if size <= 1 or value <= 0:
            return []

        if size in Domino.DISPLAY_PATTERN.keys() and value in Domino.DISPLAY_PATTERN[size]:
            return Domino.DISPLAY_PATTERN[size][value]

        if value % 2 == 1:
            return [(0, 0)] + self.generate_pattern(value - 1, size)

        pattern = []

        pattern_normalized = self.generate_normalized_pattern(value)
        pattern += self.expand_pattern(pattern_normalized, size)
        full_pattern = pattern + self.generate_pattern(value - 8, size - 2)
        if size not in Domino.DISPLAY_PATTERN.keys():
            Domino.DISPLAY_PATTERN[size] = {}
        Domino.DISPLAY_PATTERN[size][value] = full_pattern

        return full_pattern

    def generate_mutable_string_blank_half(self):
        """
        Generate a mutable string that can be used to create a
        string representation of half a Domino. It is blank, call generate_display_half(value)
        to generate a list for a given value. 
        """
        if self._size in Domino.DISPLAY_LIST.keys():
            return Domino.DISPLAY_LIST[self._size]

        display_string = MutableString()
        for i in range(self._size):
            for j in range(self._size):
                display_string[i, j] = " "

        Domino.DISPLAY_LIST[self._size] = display_string
        return display_string

    def generate_display_list_half(self, value):
        """
        Generate a list representation of half a Domino.
        """
        display_list = self.generate_display_list_blank_half()
        pattern = self.generate_pattern(value, self._size)

        for (i, j) in pattern:
            list_position_i, list_position_j = self.transform_pattern_coord_to_list_coord(i, j)
            display_list[list_position_i][list_position_j] = Domino.DISPLAY_SYMBOL

        return display_list

    def generate_string_for_value(self, value):
        """
        Generate a string representation of half a Domino (whithout canvas).
        """
        display_list = self.generate_display_list_blank_half()
        pattern = self.generate_pattern(value, self._size)

        for (i, j) in pattern:
            list_position_i, list_position_j = self.transform_pattern_coord_to_list_coord(i, j)
            display_list[list_position_i][list_position_j] = Domino.DISPLAY_SYMBOL

        return display_list

    def transform_pattern_coord_to_list_coord(self, position_i, position_j):
        """Transform the coordinate for patterns into list coordinate for string representation"""
        position_i += self._size // 2
        position_j += self._size // 2

        return position_i, position_j

    def transform_display_list_to_string(self, display_list):
        """Tranform the display list (a.k.a the mutable string) into a real string (I should have done MutableString
        class...)"""
        display_string = []
        for i in range(len(display_list)):
            display_string.append(''.join(display_list[i]))

        return '\n'.join(display_string)

    def __str__(self):
        display_rvalue = self.generate_display_list_half(self._rvalue)
        display_lvalue = self.generate_display_list_half(self._lvalue)
        canvas = self.generate_canvas()



    def generate_canvas(self):
        """
        Generate the canvas to display the domino.
        Returns a MutableString
        """

        if self._size in Domino.DISPLAY_CANVAS_LIST.keys():
            return Domino.DISPLAY_CANVAS_LIST[self._size]

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

        Domino.DISPLAY_CANVAS_LIST[self._size] = canvas
        return canvas


    def __init__(self, l_value, r_value, size=DEFAULT_SIZE):
        # Once set those values shouldn't be modified.
        self._lvalue = l_value
        self._rvalue = r_value
        self._size = size

    # TODO : remplacer par fonction __str__

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
