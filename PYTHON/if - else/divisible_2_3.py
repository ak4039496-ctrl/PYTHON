# Author: Amit Gupta
# Date: 18-07-2026

# Ask user to enter a number
num = int(input("Enter a number:- "))

# Check if divisible by 2 but not by 3
if num % 2 == 0 and num % 3 != 0:
    print(f"{num} is divisible by 2 only")
# Check if divisible by 3 but not by 2
elif num % 3 == 0 and num % 2 != 0:
    print(f"{num} is divisible by 3 only")
# Else condition for divisible by both or neither
else:
    print(f"{num} is not divisible by both 2 and 3")