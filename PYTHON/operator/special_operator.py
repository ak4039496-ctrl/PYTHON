# Author:-Amit Kumar
# Date:- 2026-07-10

# Input number
num = int(input("Enter a number:- "))

# Using Python's conditional expression syntax (Beginner Ternary)
message = "Number is Positive" if num > 0 else ("Number is Negative" if num < 0 else "Number is Zero")

print(message)