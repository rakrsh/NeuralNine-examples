#magic method and dunder example: https://www.youtube.com/watch?v=KSiRzuSx120&list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"

    def __call__(self):
        print("Hello I was called!")


v1 = Vector(10, 20)
v2 = Vector(50, 60)
v3 = v1 + v2

print(v3)
v3()

