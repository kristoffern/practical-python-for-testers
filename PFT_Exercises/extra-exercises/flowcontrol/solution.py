
def count_above(iterable, limit):
    """Return the number of elements in iterable who's values are > limit
    You can assume that all elements are integers 
    Hint: for, if
    """
    count = 0
    for i in iterable:
        if i > limit:
            count += 1
    return count


def add_all(iterable):
    """Return the sum of all elements in iterable
    You should ignore any values that cannot be treated as a number
    Hint: for, try
    """
    value = 0
    for i in iterable:
        try:
            value += i
        except TypeError:
            pass
    return value


def count_below(iterable, limit=5):
    """Count the number of elements in iterable that
    are less than limit (default limit is 5)"""
    count = 0
    for i in iterable:
        if i < limit:
            count += 1
    return count
