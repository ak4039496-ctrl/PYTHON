# Author:-Amit Kumar
# Date:- 2026-07-10

# Input a number
num = int(input("Enter a number:- "))

# Python's ternary style format: (value_if_true if condition else value_if_false)
# Check even or odd
print(f"{num} is Even" if (num % 2 == 0) else f"{num} is Odd")

# Check positive or negative
print(f"{num} is Positive" if (num >= 0) else f"{num} is Negative")