# Author:-Amit Kumar
# Date:- 2026-07-10
import math     # Import math library for pow() function

# Input base number
base = int(input("Enter base number:- "))

# Input exponent
exp = int(input("Enter exponent:- "))

# Calculate power using math.pow() function
result = math.pow(base, exp)

# Display result with 2 decimal places
print(f"{base} ^ {exp} = {result:.2f}")