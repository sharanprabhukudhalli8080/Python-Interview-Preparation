"""
Interview Question:
What is a list in Python?

Answer:
A list is a collection of items stored in order.
Lists are mutable, meaning we can modify their elements.
"""

# Creating a list
numbers = [10, 20, 30, 40]

print("Original list:", numbers)

# Adding element
numbers.append(50)

print("After append:", numbers)

# Access element
print("First element:", numbers[0])

# Loop through list
for i in numbers:
    print(i)

"""
Interview Question:
Difference between list and tuple?

List → mutable
Tuple → immutable
"""
