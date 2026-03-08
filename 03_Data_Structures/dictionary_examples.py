"""
Interview Question:
What is a dictionary in Python?

Answer:
A dictionary stores data in key-value pairs.
It is unordered and mutable.
"""

# Creating dictionary

student = {
    "name": "Sharan",
    "age": 21,
    "course": "CSE"
}

print(student)

# Access value
print("Name:", student["name"])

# Add new key
student["marks"] = 90

print(student)

# Loop through dictionary

for key, value in student.items():
    print(key, ":", value)
