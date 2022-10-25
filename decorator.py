# decorators: https://www.youtube.com/watch?v=iZZtEJjQLjQ&list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc&index=2


def mydecorator(function):

    def wrapper(*args, **kwargs):
        print("I am decorating your function!")
        return_val = function(*args, **kwargs)
        return return_val

    return wrapper

@mydecorator
def hello_world(person):
    print("Hello world")

hello_world("Mike")

