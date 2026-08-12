# Author: Amit Gupta
# Date: 08-07-2026

# Ask user to enter a year
year = int(input("Enter a year:- "))

# Check if year is divisible by 100
if year % 100 == 0:
    print(f"{year} is a Century Year")  # Example: 1900, 2000
else:
    print(f"{year} is NOT a Century Year")  # Example: 1999, 2021