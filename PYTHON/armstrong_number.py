# Author: Amit Gupta
# Date: 18-07-2026

# Ask user to enter a 3-digit number
num = int(input("Enter a 3-digit number:- "))

# Extract digits using integer division (//) and modulo (%)
d1 = num // 100          # First digit
d2 = (num // 10) % 10    # Second digit
d3 = num % 10            # Third digit

# Calculate sum of cubes of digits (using ** for exponents)
total_sum = (d1 ** 3) + (d2 ** 3) + (d3 ** 3)

# Check if number is Armstrong
if total_sum == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is NOT an Armstrong number")