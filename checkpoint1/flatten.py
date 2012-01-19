def flatten(l, depth):
    """ Flatten two lists up to a maximum given depth.

    >>> flatten([], 0)
    []

    >>> flatten([1, 2, 3], 0)
    [1, 2, 3]

    >>> flatten([[1], [2], [3]], 0)
    [[1], [2], [3]]

    >>> flatten([[1], [2], [3]], 1)
    [1, 2, 3]

    >>> flatten([[1], [2], [3]], 100)
    [1, 2, 3]

    >>> flatten([[[1]], [[2]], [3], 4], 1)
    [[1], [2], 3, 4]

    >>> flatten([[[1]], [[2]], [3], 4], 2)
    [1, 2, 3, 4]

    >>> flatten(((1, 2), (3, 4)), 1)
    [1, 2, 3, 4]

    >>> flatten('abc', 0)
    'abc'

    >>> flatten([['abc'], 1, [['abc']]], 2)
    ['a', 'b', 'c', 1, 'abc']

    >>> flatten([], -2)
    Traceback (most recent call last):
        ...
    AssertionError
    """

    assert depth >= 0
    if depth == 0:
        return l

    result = []
    for list_element in l:
        try:
            result.extend(
                flatten(iter(list_element), depth - 1)
            )
        except TypeError:
            result.append(list_element)
    return result

