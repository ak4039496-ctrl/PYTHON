# Author:-Amit Kumar
# Date:- 2026-07-10

# Input two numbers
a = int(input("Enter first number:- "))
b = int(input("Enter second number:- "))

# Display values before swapping
print(f"Before swapping:- a => {a}, b => {b}")

# Swap logic without third variable (using + and - operators)
a = a + b   # Step 1: Add both numbers and store in 'a'
b = a - b   # Step 2: Subtract new 'a' with 'b' to get original 'a'
a = a - b   # Step 3: Subtract new 'a' with new 'b' to get original 'b'

# Display values after swapping
print(f"After swapping: a => {a}, b => {b}")