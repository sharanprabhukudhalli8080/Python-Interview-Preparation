"""
Interview Question:
What is Exception Handling in Python?

Answer:
Exception handling is used to handle runtime errors
so the program does not crash.
Python uses try, except, else, and finally blocks.
"""

# Example 1: Basic Exception Handling

try:
    a = 10
    b = 0
    result = a / b
    print(result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")


"""
Interview Question:
What are the main blocks used in exception handling?

Answer:
try     → Code that may cause an error
except  → Handles the error
else    → Executes if no error occurs
finally → Executes whether error occurs or not
"""


# Example 2: try-except-else-finally

try:
    num = int(input("Enter a number: "))
    result = 100 / num

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")

else:
    print("Result:", result)

finally:
    print("Program finished")
