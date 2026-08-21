# Author: Amit Gupta
# Date: 18-07-2026

# Ask user to enter a number
num = int(input("Enter a number:- "))

# Check if number is divisible by both 5 and 11
if num % 5 == 0 and num % 11 == 0:
    print(f"{num} is divisible by both 5 and 11")
# Else condition if not divisible by both
else:
    print(f"{num} is NOT divisible by both 5 and 11")