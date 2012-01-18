def merge(a, b):
    """Second exercise method

       Merge 2 objects with any depth (including contained dictionaries,
       lists, sets, strings, integers,floats). Type mismatches should 
       yield a tuple with the two elements.
    """
    result = {}
    for property, value in a.iteritems():
            if type(value) is type(b[property]):
                if type(value) is list or type(value) is str:
                    result[property] = value + b[property]
                if type(value) is set:
                    result[property] = value | b[property]
                if type(value) is int or type(value) is float:
                    result[property] = value + b[property]
                if type(value) is dict:
                    result[property] = (merge(value, b[property]))
            else:
                result[property] = (value, b[property])
    return result



a = {'x': [1,2,3], 'y': 1, 'z': set([1,2,3]), 'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]}

b = {'x': [4,5,6], 'y': 4, 'z': set([4,2,3]), 'w': 'asdf', 't': {'a': [3, 2]}, 'm': "wer"}


print "First object is: ", a
print "Second object is: ", b

print "Merged object is: ", merge(a, b)
