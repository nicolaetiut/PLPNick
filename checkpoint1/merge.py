import operator

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

    >>> a = {
    ... 'x': [1, 2, 3], 'y': 1, 'z': set([1, 2, 3]),
    ... 'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]
    ... }
    >>> b = {
    ... 'x': [4, 5, 6], 'y': 4, 'z': set([4, 2, 3]),
    ... 'w': 'asdf', 't': {'a': [3, 2]}, 'm': "wer"
    ... }
    >>> r = merge(a, b)

    >>> r['m']
    ([1], 'wer')

    >>> sorted(r['t'].items())
    [('a', [1, 2, 3, 2])]

    >>> r['w']
    'qweqweasdf'

    >>> r['y']
    5

    >>> r['x']
    [1, 2, 3, 4, 5, 6]

    >>> r['z']
    set([1, 2, 3, 4])

    >>> sorted(merge({'x': 1}, {'y': 2}).items())
    [('x', 1), ('y', 2)]

    """

    process_chain = try_to_apply_operator_in_order(
        operator.add,
        operator.or_,
        merge,
        lambda a, b: (a, b)
    )

    result = dict(a)
    result.update(b)

    a_key_set = set(a.keys())
    b_key_set = set(b.keys())
    common_keys = a_key_set.intersection(b_key_set)

    for key in common_keys:
        result[key] = process_chain(a[key], b[key])

    return result


def try_to_apply_operator_in_order(operation, next_operation=None):

    def wrapper(a, b):
        try:
            return operation(a, b)
        except TypeError:
            if callable(next_operation):
                return next_operation(a, b)
            else:
                raise

    return wrapper


def try_chain(*operations):
    chain = try_to_apply_operator_in_order(operations[-1])
    for op in reversed(operations[:-1]):
        chain = try_to_apply_operator_in_order(op, chain)
    return chain
