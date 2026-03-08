"""
Interview Question:
What is abstraction?

Answer:
Abstraction hides internal implementation details
and shows only the necessary features.
"""

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        print("Area:", self.side * self.side)


s = Square(4)
s.area()
