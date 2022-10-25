# decorators: https://www.youtube.com/watch?v=iZZtEJjQLjQ&list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc&index=2
# Practical example #1 - Timing

import time

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after-before} seconds to execute!\n")
        return value

    return wrapper

@timed
def myfunction(x):
    result = 1
    for i in range(1, x):
        result *=1
    return result


myfunction(10000)
