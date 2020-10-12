class BadDominoException(Exception):
    def __init__(self, n):
        super().__init__()
        self._value = n

    @property
    def value(self):
        return self._value

    def __str__(self):
        return f"The Domino '{self._value + 1}' is not in your hand."


class BadSumException(Exception):
    def __init__(self, sum):
        super().__init__()
        self._sum = sum

    @property
    def sum(self):
        return self._sum

    def __str__(self):
        return f"The sum of you Dominos is not equal to '{self.sum}'"