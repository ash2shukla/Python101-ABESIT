import doctest


def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)


if __name__ == "__main__":
    doctest.testmod()   # automatically validate the embedded tests
