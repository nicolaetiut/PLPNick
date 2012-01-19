def merge(a, b):
    """Merge 2 objects with any depth (including contained dictionaries,
    lists, sets, strings, integers,floats). Type mismatches should yield
    a tuple with the two elements.

    >>> merge({'x': [1, 2, 3]}, {'x': [4, 5, 6]})
    {'x': [1, 2, 3, 4, 5, 6]}

    >>> merge({'y': 1}, {'y': 4})
    {'y': 5}

    >>> merge({'z': set([1, 2, 3])}, {'z': set([4, 5, 6])})
    {'z': set([1, 2, 3, 4, 5, 6])}

    >>> merge({'w': 'qweqwe'}, {'w': 'asd'})
    {'w': 'qweqweasd'}

    >>> merge({'t': {'a': [1, 2]}}, {'t': {'a': [3, 4]}})
    {'t': {'a': [1, 2, 3, 4]}}

    >>> merge({'m': [1]}, {'m': 2})
    {'m': ([1], 2)}

    >>> merge({}, {})
    {}
    """
    result = {}
    for property, value in a.iteritems():
        try:
            result[property] = merge(value, b[property])
        except AttributeError:
            if type(value) is set:
                result[property] = value | b[property]
            else:
                try:
                    result[property] = value + b[property]
                except TypeError:
                    result[property] = (value, b[property])
    return result


if __name__ == "__main__":

    a = {
       'x': [1, 2, 3], 'y': 1, 'z': set([1, 2, 3]),
       'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]
    }

    b = {
       'x': [4, 5, 6], 'y': 4, 'z': set([4, 2, 3]),
       'w': 'asdf', 't': {'a': [3, 2]}, 'm': "wer"
    }

    print "First object is: ", a
    print "Second object is: ", b
    print "Merged object is: ", merge(a, b)
