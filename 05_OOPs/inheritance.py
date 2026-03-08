"""
Interview Question:
What is inheritance?

Answer:
Inheritance allows one class to inherit properties and methods from another class.
"""

# Parent class

class Animal:

    def speak(self):
        print("Animal makes sound")


# Child class

class Dog(Animal):

    def bark(self):
        print("Dog barks")


# Object

d = Dog()
d.speak()
d.bark()
