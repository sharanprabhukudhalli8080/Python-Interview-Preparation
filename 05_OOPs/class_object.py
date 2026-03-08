"""
Interview Question:
What is a class and object in Python?

Answer:
Class → Blueprint for creating objects.
Object → Instance of a class.
"""

# Creating a class

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Creating object

s1 = Student("Sharan", 21)
s1.display()
