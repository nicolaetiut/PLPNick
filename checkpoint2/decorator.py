"""Write a function decorator that tracks how long the
execution of the wrapped function took. The decorator
will log slow function calls including details about
the execution time and function name. The decorator
should take an optional threshold argument.
"""
import datetime
import time

now = datetime.datetime.now()


def get_current_millis():
    return int(round(time.time() * 1000))


def get_operation_results_in_order(operations):
    """ Return results of operations called in order.

    >>> def get_current_millis():
    ...     return int(round(time.time() * 1000))
    >>> def aFunction():
    ...     for x in range(1, 1000000):
    ...         y = x * x
    >>> op1 = {'call': get_current_millis, 'args': None, 'kwargs': None}
    >>> op2 = {'call': aFunction, 'args': None, 'kwargs': None}
    >>> operations = [op1, op2, op1]
    >>> results = get_operation_results_in_order(operations)
    >>> len(results)
    3

    >>> operations = [None, None, op2]
    >>> results = get_operation_results_in_order(operations)
    >>> len(results)
    0
    """
    results = []
    for op in operations:
        if op and callable(op['call']):
            if op['args'] and op['kwargs']:
                results.append(
            op['call'](*op['args'], **op['kwargs'])
            )
            else:
                results.append(op['call']())
        else:
            return []
    return results


def check_millis(time_before, time_after, threshold):
    """ Checks if interval between time_before and time_after > than threshold.

    >>> check_millis(1, 2, 3)
    False

    >>> check_millis(1, 6, 3)
    True

    >>> check_millis(4, 1, 3)
    False

    >>> check_millis(4, 1, -5)
    False
    """
    if (time_after > time_before and time_after - time_before > threshold):
        return True
    return False


def time_slow(logger, threshold=None):
    def my_decorator(aFunction):
        def wrapped(*args, **kwargs):
            op1 = {'call': get_current_millis, 'args': None, 'kwargs': None}
            op2 = {'call': aFunction, 'args': args, 'kwargs': kwargs}
            operations = [op1, op2, op1]
            res = get_operation_results_in_order(operations)
            if len(res) == 3 and check_millis(res[0], res[2], threshold):
                logger.log("The function call to '" +
                aFunction.__name__ +
                "' lasted " + str(res[2] - res[0]) + " milliseconds.")
                logger.log("Logging slow function called at " +
                now.strftime("%Y-%m-%d %H:%M") + ".")
        return wrapped
    return my_decorator


class MyLogger:

    def log(self, message):
        print message

logger = MyLogger()


@time_slow(logger, threshold=10)
def aFunction():
    for x in range(1, 1000000):
        y = x * x
    print "done"

aFunction()
