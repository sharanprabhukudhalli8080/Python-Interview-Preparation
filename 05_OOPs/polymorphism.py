"""
Interview Question:
What is polymorphism?

Answer:
Polymorphism means one method can have different behaviors.
"""

class Bird:

    def fly(self):
        print("Bird flies")


class Airplane:

    def fly(self):
        print("Airplane flies")


# Same method name

b = Bird()
a = Airplane()

b.fly()
a.fly()
