# Author:-Amit Kumar
# Date:- 2026-07-10

# Input two numbers
a = int(input("Enter first number:- "))
b = int(input("Enter second number:- "))

# Display values before swapping
print(f"Before swapping:- a => {a}, b => {b}")

# Swap logic using third variable
temp = a   # Store value of a in temp
a = b      # Assign value of b to a
b = temp   # Assign value of temp (original a) to b

# Display values after swapping
print(f"After swapping:- a => {a}, b => {b}")