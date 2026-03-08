"""
Interview Question:
How do you take input from the user in Python?

Answer:
Python provides the input() function to take input from the user.
The input is returned as a string by default.

To convert it to numbers we use:
int()  → integer
float() → decimal numbers
"""

# Taking input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Displaying output
print("Hello", name)
print("You are", age, "years old")

"""
Interview Question:
How does Python display output?

Answer:
Python uses the print() function to display output to the console.
"""
