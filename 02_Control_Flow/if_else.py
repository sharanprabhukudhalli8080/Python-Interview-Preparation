"""
Interview Question:
What is an if-else statement in Python?

Answer:
The if-else statement is used to make decisions in a program.
It executes a block of code only when a condition is True.

Syntax:
if condition:
    statement
else:
    statement
"""

# Example 1: Positive or Negative number

num = 10

if num > 0:
    print("Positive number")
else:
    print("Negative number")


"""
Interview Question:
What is an if-elif-else ladder?

Answer:
It is used when we have multiple conditions.
"""

# Example 2: Grade system

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
