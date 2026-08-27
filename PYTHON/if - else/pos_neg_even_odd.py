# Author: Amit Gupta
# Date: 18-07-2026

# Variable to store the number
num = int(input("Enter a number:- "))

# Check if number is positive
if num > 0:
    # Nested check for even or odd
    if num % 2 == 0:
        print(f"{num} is Positive Even")
    else:
        print(f"{num} is Positive Odd")
# Check if number is negative
elif num < 0:
    # Nested check for even or odd
    if num % 2 == 0:
        print(f"{num} is Negative Even")
    else:
        print(f"{num} is Negative Odd")
# Else condition for zero
else:
    print("Number is Zero")