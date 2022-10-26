from dataclasses import dataclass, field


@dataclass(order=True)
class Investor:
    sort_index: float = field(init=False, repr=False)
    name: str
    age: int
    cash: float = field(repr=True, default=0.0)

    def __post_init__(self):
        self.sort_index = self.cash

i1 = Investor("john", 21)
i2 = Investor("Anna", 31, 95000)
i3 = Investor("Bob", 29, 75000)

print(i1)
print(i2)
print(i3)

mylist = [i1, i2, i3]
mylist.sort()

print(mylist)