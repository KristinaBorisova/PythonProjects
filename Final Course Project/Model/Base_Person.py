# helps me to keep track of weak references and instances
import weakref
# import Regular expressions module
import re

# Parent Class
class Person:
    # instance method
    def print_info_CSV_Format(self):
        return "{},{},{}".format(self.name, self.age, self.gender)

    _instance = set()

    # Initializer/constructor
    # self - a parameter that invokes the object itself
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        return print(
            "---Personal Details--- \n" "Name:", self.name, "\n" "Age:", self.age, "\n" "Gender:", self.gender, "\n"
        )

    @classmethod
    def get_instances(cls):
        dead = set()
        for ref in cls._instance:
            obj = ref()
            if obj is not None:
                yield obj
            else:
                dead.add(ref)
        cls._instance -= dead
