# Author: Amit Gupta
# Date: 18-07-2026

# Variable to store the number
num = int(input("Enter a number:- "))

# Print the entered number
print(f"You entered:- {num}")

# Check if number is positive, negative, or zero
if num > 0:
    # Nested check for single-digit or multi-digit 
    if 1 <= num <= 9:
        print(f"{num} is Positive Single-digit")
    else:
        print(f"{num} is Positive Multi-digit")
elif num < 0:
    # Nested check for single-digit or multi-digit
    if -9 <= num <= -1:
        print(f"{num} is Negative Single-digit")
    else:
        print(f"{num} is Negative Multi-digit")
else:
    print("Number is Zero")