# Author: Amit Gupta
# Date: 18-07-2026

# Ask user to enter electricity units consumed
units = int(input("Enter electricity units consumed:- "))

# Print entered units
print(f"Units Consumed =>  {units}")

# Slab rate calculation
if units <= 50:
    bill = units * 0.50
elif units <= 150:
    bill = (50 * 0.50) + ((units - 50) * 0.75)
elif units <= 250:
    bill = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)
else:
    bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 250) * 1.50)

# Add 20% surcharge
bill += (bill * 0.20)

# Print final bill formatted to 2 decimal places
print(f"Total Electricity Bill => Rs. {bill:.2f}")
