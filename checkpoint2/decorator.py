import datetime
import time

now = datetime.datetime.now()


def time_slow(threshold = None):
    def my_decorator(aFunction):
        def wrapped(*args, **kwargs):
            millis1 = int(round(time.time() * 1000))
            res = aFunction(*args, **kwargs)
            millis2 = int(round(time.time() * 1000))
            total_time = millis2 - millis1
            if (total_time > threshold):
                print "The function call to '" + aFunction.__name__ + "' lasted " + str(total_time) + " milliseconds."
                print "Logging slow function called at " + now.strftime("%Y-%m-%d %H:%M") + "."
            return res
        return wrapped
    return my_decorator

@time_slow(threshold = 10)
def aFunction():
    for x in range(1, 1000000):
        y = x * x
    print "done"

aFunction()
