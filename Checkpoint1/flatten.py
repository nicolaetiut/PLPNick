def flatten(list_a, max_depth):
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

print "Original list is: "
print mylst

print "Flatten level is: "
print level

print "Flattend list is: "
print list(flatten(mylst, level))
