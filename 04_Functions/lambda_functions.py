"""
Interview Question:
What is a lambda function?

Answer:
A lambda function is a small anonymous function defined using the lambda keyword.
It can take multiple arguments but only one expression.

Syntax:
lambda arguments : expression
"""

# Example 1

square = lambda x: x * x

print("Square:", square(5))


# Example 2

add = lambda a, b: a + b

print("Addition:", add(10, 20))


"""
Interview Tip:
Lambda functions are often used with functions like:
map(), filter(), and sorted().
"""
