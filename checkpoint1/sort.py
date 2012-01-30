"""Sort list of dictionaries from file based on the dictionary keys.
The rule for comparing dictionaries between them is:
- if the value of the dictionary with the lowest alphabetic key
is lower than the value of the other dictionary with the lowest
alphabetic key, then the first dictionary is smaller than the
second.
- if the two values specified in the previous rule are equal
reapply the algorithm ignoring the current key.
"""
import sys


def quicksort(l):
    """Quicksort implementation using list comprehensions

    >>> quicksort([1, 2, 3])
    [1, 2, 3]

    >>> quicksort('bac')
    ['a', 'b', 'c']

    >>> quicksort([{'bb': 1, 'aa': 2}, {'ba': 1, 'ab': 2}, {'aa': 1, 'ac': 2}])
    [{'aa': 1, 'ac': 2}, {'aa': 2, 'bb': 1}, {'ab': 2, 'ba': 1}]

    >>> quicksort([])
    []
    """
    if l == []:
        return []
    else:
        pivot = l[0]
        sub_list = [list_element for list_element in l[1:]
            if list_element < pivot]
        lesser = quicksort(sub_list)
        sub_list = [list_element for list_element in l[1:]
            if list_element >= pivot]
        greater = quicksort(sub_list)
        return lesser + [pivot] + greater


def sortListFromFile(fileName, outputFileName):
    """Sort list of dictionaries from file. The input is a file containing
    the list of dictionaries. Each dictionary key value is specified on
    the same line in the form <key> <whitespace> <value>. Each list item
    is split by an empty row. The output is a file containing a list of
    integers specifying the dictionary list in sorted order. Each integer
    identifies a dictionary in the order they were received in the input
    file.

    >>> sortListFromFile('nonexistentfile','output.txt')
    Traceback (most recent call last):
        ...
    IOError: [Errno 2] No such file or directory: 'nonexistentfile'
    """
    l = []
    with open(fileName, 'r') as f:
        elem = {}
        for line in f:
            if line.strip():
                line = line.split()
                elem[line[0]] = line[1]
            else:
                l.append(elem)
                elem = {}
        l.append(elem)
    f.closed
    with open(outputFileName, 'w+') as f:
        for list_elem in quicksort(l):
            f.write(str(l.index(list_elem)) + '\n')
    f.closed

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        sortListFromFile(sys.argv[1], 'output.txt')
    else:
        print "Please provide an input file as argument."
