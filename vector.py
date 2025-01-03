class Vector:
    def __init__(self, values):
        assert Vector.is_iterable(values), 'values must be iterable!'
        self.values = tuple(values)

    def __eq__(self, other):
        if isinstance(other, Vector):
            if len(self) != len(other):
                return False
            for x1, x2 in zip(self.values, other.values):
                if x1 != x2:
                    return False
            return True
        elif Vector.is_iterable(other) and tuple(other) == self.values:
            return True
        return False

    def __add__(self, other):
        if isinstance(other, Vector):
            if len(self) == len(other):
                return self.__class__(list(a+b for a, b in zip(self.values, other.values)))
            else:
                raise ValueError(f"you can't add a Vector of length {len(other)} to your Vector with length {len(self)}")
        elif isinstance(other, (int, float)):
            return self.__class__(list(a+other for a in self.values))
        raise ValueError(f"you can't add a vector to {type(other)}")

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self) == len(other):
                return self.__class__(a*b for a, b in zip(self.values, other.values))
            else:
                raise ValueError(f"you can't multiply a Vector of length {len(other)} to your Vector with length {len(self)}")
        elif isinstance(other, (int, float)):
            return self.__class__(a*other for a in self.values)
        raise ValueError(f"you cannot multiply a vector with {type(other)}")

    def __abs__(self):
        length = len(self)
        return sum(map(lambda x: x**length, self.values)) ** (1/length)

    def __len__(self):
        return len(self.values)

    def __repr__(self):
        return f"{type(self).__name__}{self.values}"  # self.values itself is a tuple and has parenthesis

    @staticmethod
    def is_iterable(x, dictionary=True):
        for dtype in (list, tuple, set, frozenset, dict if dictionary else None):
            if dtype is not None and isinstance(x, dtype):
                return True
        return False
