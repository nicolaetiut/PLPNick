def flatten(list_a, max_depth):
    """First exercise method

       Implement a function that will flatten two lists up to a maximum given depth.
    """
    for x in list_a:
         if isinstance(x,list):
             if (max_depth > 0):
                 for x in flatten(x, max_depth - 1):
                     yield x
             else:
                 yield x
         else:
             yield x



mylst = [[1], 2, [[3, 4], 5], [[[]]], [[[6]]], 7, 8, [], [[[[9, [10, 11]]]]]]
level = 2

print "Original list is: ", mylst
print "Flatten level is: ", level
print "Flattend list is: ", list(flatten(mylst, level))
