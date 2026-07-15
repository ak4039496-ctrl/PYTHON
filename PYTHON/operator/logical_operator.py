# Author:-Amit Kumar
# Date:- 2026-07-10

# Input two numbers separately for simplicity
a = int(input("Enter first number:- "))
b = int(input("Enter second number:- "))

# Logical AND (true only if both conditions are true)
if a > 0 and b > 0:
    print("Both numbers are positive")

# Logical OR (true if at least one condition is true)
if a > 0 or b > 0:
    print("At least one number is positive")

# Logical NOT (inverts the condition)
if not (a > 0):
    print("a is not positive")