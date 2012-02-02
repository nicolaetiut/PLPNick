"""Given a dictionary, swap keys <-> values. The program should
use some custom logic to check if the swap is possible, but without
using try..except constructs or the __hash__() function.
"""
import collections


def swap_dict(dictionary):
    """ Switch key value pairs if possible for the given dictionary.

    >>> swap_dict({'a': 123, 'b': 456})
    {456: ['b'], 123: ['a']}

    >>> swap_dict({'a': 1, 'b': 1, 'c': 2})
    {1: ['a', 'b'], 2: ['c']}

    >>> swap_dict({'a': (1, 2, [3])})
    'Swap is not possible'
    """
    new_dict = {}
    for key, value in dictionary.items():
        if not isKeyable(value):
            return "Swap is not possible"
        if value in new_dict.keys():
            new_dict[value].append(key)
        else:
            new_dict[value] = [key]
    return new_dict


def isKeyable(value):
    return not isinstance(value, (list, tuple))

if __name__ == "__main__":
    my_dict = {'a': 1, 'b': 1, 'c': 2}
    print my_dict
    print swap_dict(my_dict)
