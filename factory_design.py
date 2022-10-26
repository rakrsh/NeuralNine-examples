#factory design pattern: https://www.youtube.com/watch?v=-a1PFtooGo4&list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc&index=7

from abc import ABCMeta, abstractmethod, abstractstaticmethod

class IPerson(metaclass = ABCMeta):

    @abstractstaticmethod
    def person_method():
        ''' Interface method'''

class Student(IPerson):

    def __init__(self):
        self.name = "Basic student name"

    def person_method(self):
        print("I am a student")

class Teacher(IPerson):

    def __init__(self):
        self.name = "Basic teacher name"

    def person_method(self):
        print("I am a teacher")

class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type.lower() == "student":
            return Student()
        elif person_type.lower() == "teacher":
            return Teacher()
        else:
            print("Invalid type")
            return -1


if __name__ == "__main__":
    choice = input("What type of person do you want to create \n")
    person = PersonFactory.build_person(choice)
    person.person_method()