"""
Interview Question:
What are loops in Python?

Answer:
Loops are used to repeat a block of code multiple times.

Types of loops in Python:
1. for loop
2. while loop
"""

# Example 1: for loop

for i in range(5):
    print("For loop:", i)


"""
Interview Question:
What is a while loop?

Answer:
A while loop runs as long as the condition remains True.
"""

# Example 2: while loop

i = 1

while i <= 5:
    print("While loop:", i)
    i += 1


# Interview Example: Multiplication Table

num = 5

for i in range(1,11):
    print(num, "x", i, "=", num*i)
