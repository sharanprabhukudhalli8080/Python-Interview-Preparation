"""
Interview Question:
What is file handling in Python?

Answer:
File handling allows a program to read data from a file
or write data to a file.

Python provides the open() function to work with files.
"""

# Example 1: Writing to a file

file = open("sample.txt", "w")
file.write("Hello, this is Python file handling example.")
file.close()

print("Data written to file")


"""
Interview Question:
What are the different file modes in Python?

r  → Read file
w  → Write file (creates new file or overwrites)
a  → Append to file
x  → Create file
"""

# Example 2: Reading from a file

file = open("sample.txt", "r")
content = file.read()

print("File Content:")
print(content)

file.close()


"""
Interview Tip:
Using 'with open()' is better because it automatically
closes the file.
"""

# Example 3: Using with statement

with open("sample.txt", "r") as file:
    data = file.read()
    print("Reading using with:", data)
