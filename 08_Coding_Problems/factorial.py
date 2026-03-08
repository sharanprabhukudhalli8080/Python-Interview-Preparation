"""
Interview Question:
Find factorial of a number.

Factorial of n:
n! = n × (n-1) × (n-2) ...
"""

num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial:", fact)
