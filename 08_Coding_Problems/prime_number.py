"""
Interview Question:
Check whether a number is prime.

Prime number → number divisible only by 1 and itself.
"""

num = int(input("Enter a number: "))

for i in range(2, num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime Number")
