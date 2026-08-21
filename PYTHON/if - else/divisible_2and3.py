# Author: Amit Gupta
# Date: 18-07-2026

# Ask user to enter a number
num = int(input("Enter a number:- "))

# Print the entered number
print(f"You entered:- {num}")

# Check divisibility using if-elif-else
if num % 2 == 0 and num % 3 == 0:
    print(f"{num} is divisible by BOTH 2 and 3")
elif num % 2 == 0:
    print(f"{num} is divisible by 2 only")
elif num % 3 == 0:
    print(f"{num} is divisible by 3 only")
else:
    print(f"{num} is NOT divisible by 2 or 3")