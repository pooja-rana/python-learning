from abc import ABC,abstractmethod
# abstract class
class Subject(ABC):
    @abstractmethod
    def subject(self):
        pass
class Maths(Subject):
    # override superclass method
    def subject(self):
        print("Subject is Maths")
class Physics(Subject):
    # override superclass method
    def subject(self):
        print("Subject is Physics")
class Chemistry(Subject):
    # override superclass method
    def subject(self):
        print("Subject is Chemistry")
class English(Subject):
    # override superclass method
    def subject(self):
        print("Subject is English")
maths=Maths()
maths.subject()

physics=Physics()
physics.subject()

chemistry=Chemistry()
chemistry.subject()

english=English()
english.subject()


# What are Concrete Methods in Abstract Base Class(ABC)


import abc
from abc import ABC, abstractmethod
class SuperClass(ABC):
    @abstractmethod
    def my_method(self):
        print("The abstract superclass")
class SubClass(SuperClass):
    def my_method(self):
        super().my_method()
        print("The subclass")
obj=SubClass()
obj.my_method()



# Abstract Properties of an Abstract Class:-

import abc
from abc import ABC, abstractmethod


class Color(ABC):
    def __init__(self, color):
        self.color = color

    # an abstract method
    @abc.abstractproperty
    def print_color(self):
        pass


class Red(Color):
    def __init__(self):
        super().__init__("Red")

    @property
    def print_color(self):
        return self.color


class Green(Color):
    def __init__(self):
        super().__init__("Green")

    @property
    def print_color(self):
        return self.color


class Blue(Color):
    def __init__(self):
        super().__init__("Blue")

    @property
    def print_color(self):
        return self.color


obj = Green()
print("The color is " + obj.color)