#Data class example : https://www.youtube.com/watch?v=ojrbuVKblew

class Investor:

    def __init__(self, name: str, age: int, cash: float):
        self.name = name
        self.age = age
        self.cash = cash

    def __repr__(self):
        return f"Name: {self.name}"

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.cash < other.cash

i1 = Investor("john", 21, 45000)
i2 = Investor("Anna", 31, 95000)
i3 = Investor("Bob", 29, 75000)

i4 = Investor("john", 21, 45000)

print(i1>i4)