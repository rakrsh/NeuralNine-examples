#generators: https://www.youtube.com/watch?v=lox29cXvwnk&list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc&index=3

import sys

def mygenerator(n):
    for x in range(n):
        yield x ** 3


values = mygenerator(1000000)
print(sys.getsizeof(values))

print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))

