# Author: Amit Gupta
# Date: 18-07-2026

# Variable to store year
year = int(input("Enter a year:- "))

# Check if year is divisible by 400
if year % 400 == 0:
    print(f"{year} is a Leap Year")  # Leap year
# Check if year is divisible by 100 (but not by 400)
elif year % 100 == 0:
    print(f"{year} is NOT a Leap Year")  # Not leap year
# Check if year is divisible by 4 (but not by 100)
elif year % 4 == 0:
    print(f"{year} is a Leap Year")  # Leap year
# If none of the above conditions are true
else:
    print(f"{year} is NOT a Leap Year")  # Not leap year