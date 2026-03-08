"""
Interview Question:
Check whether a string is a palindrome.

A palindrome reads the same forward and backward.
Example: madam, level
"""

text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
