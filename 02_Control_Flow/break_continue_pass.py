"""
Interview Question:
Explain break, continue, and pass in Python.

break → Stops the loop immediately
continue → Skips the current iteration
pass → Does nothing (placeholder statement)
"""

# break example

for i in range(10):

    if i == 5:
        break

    print("Break Example:", i)


# continue example

for i in range(5):

    if i == 2:
        continue

    print("Continue Example:", i)


# pass example

for i in range(5):

    if i == 3:
        pass

    print("Pass Example:", i)
