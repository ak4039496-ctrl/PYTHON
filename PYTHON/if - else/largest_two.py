# Author: Amit Gupta
# Date: 18-07-2026

# Input two numbers
a = int(input("Enter first number:- "))
b = int(input("Enter second number:- "))

# If condition to check which is larger
if a > b:
    print(f"{a} is larger")
# Else if condition to check if b is larger
elif b > a:
    print(f"{b} is larger")
# Else condition when both are equal
else:
    print("Both numbers are equal")