#encapsulation : https://www.youtube.com/watch?v=dzmYoSzL8ok&list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc&index=5

class Person:

    def __init__(self, name, age, gender):

        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        self.__name = value

    @staticmethod
    def mymethod():
        print("Static method here")

p1 = Person("Mike", 20, "m")
print(p1.Name)

p1.Name = "Bob"
print(p1.Name)

Person.mymethod()
p1.mymethod()