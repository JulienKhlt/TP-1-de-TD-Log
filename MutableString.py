class MutableString:
    """
    A mutable definition of a string.
    Will be expanded at need.
    Sparse matrix representation could have been better?
    """

    def __init__(self, string=""):
        self._string_list = []
        self._has_changed = False
        self._string = string

        self._string_list = string.split('\n')
        for i in range(len(self._string_list)):
            self._string_list[i] = list(self._string_list[i])

    def __str__(self):
        if self._has_changed:
            self.generate_string()

        return self._string

    def __getitem__(self, key):
        if type(key) is tuple:
            row, col = key
            return self._string_list[row][col]
        else:
            return self._string_list[key]

    def __setitem__(self, key, value):
        self._has_changed = True
        if type(key) is tuple:
            row, col = key
            # if it is out of bound, the list is expanded with spaces
            for _ in range(len(self._string_list), row + 1):
                self._string_list.append([])

            for _ in range(len(self._string_list[row]), col + 1):
                self._string_list[row].append(" ")

            self._string_list[row][col] = value

        else:
            if type(value) is list:
                self._string_list[key] = value
            else:
                self._string_list[key] = list(value)

    def generate_string(self):
        """Generate the string representation of the object, doesn't return anything."""
        if not self._has_changed:
            return

        string = []
        for i in range(len(self._string_list)):
            string.append(''.join(self._string_list[i]))

        self._string = '\n'.join(string)
        self._has_changed = False
