"""
Interview Question:
What is recursion in Python?

Answer:
Recursion is a process where a function calls itself
to solve a smaller instance of the same problem.
"""

# Example: Factorial using recursion

def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n - 1)


print("Factorial:", factorial(5))


"""
Interview Question:
What is the base case in recursion?

Answer:
The base case is the condition that stops the recursive calls.
Without it, recursion will run infinitely.
"""
