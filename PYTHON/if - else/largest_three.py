# Author: Amit Gupta
# Date: 18-07-2026

# Input three numbers
a = int(input("Enter first number:- "))
b = int(input("Enter second number:- "))
c = int(input("Enter third number:- "))

# If condition to check largest among three
if a >= b and a >= c:
    print(f"{a} is the largest")
elif b >= a and b >= c:
    print(f"{b} is the largest")
else:
    print(f"{c} is the largest")