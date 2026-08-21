# Author: Amit Gupta
# Date: 18-07-2026

# Variable to store year
year = int(input("Enter a year:- "))

# Print the entered year
print(f"You entered:- {year}")

# Leap year logic using if-else
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is NOT a Leap Year")