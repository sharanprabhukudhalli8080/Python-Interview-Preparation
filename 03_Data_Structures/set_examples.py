"""
Interview Question:
What is a set in Python?

Answer:
A set is an unordered collection of unique elements.
Duplicate values are automatically removed.
"""

# Creating a set

numbers = {1,2,3,3,4,4,5}

print("Set:", numbers)

# Adding element
numbers.add(6)

print(numbers)

# Looping through set
for i in numbers:
    print(i)
