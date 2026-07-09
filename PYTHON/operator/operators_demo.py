"""
Author      : Amit Gupta
Description : Demonstrates all major operators in Python
Created on  : July 9, 2026
"""

# -------------------------------
# Arithmetic Operators
# -------------------------------
a, b = 10, 3
print("\n--- Arithmetic Operators ---")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# -------------------------------
# Relational (Comparison) Operators
# -------------------------------
x, y = 5, 10
print("\n--- Relational Operators ---")
print(f"x > y : {x > y}")
print(f"x < y : {x < y}")
print(f"x == y : {x == y}")
print(f"x != y : {x != y}")
print(f"x >= y : {x >= y}")
print(f"x <= y : {x <= y}")

# -------------------------------
# Logical Operators
# -------------------------------
p, q = True, False
print("\n--- Logical Operators ---")
print(f"p and q : {p and q}")
print(f"p or q : {p or q}")
print(f"not p : {not p}")
print(f"not q : {not q}")

# -------------------------------
# Assignment Operators
# -------------------------------
num = 10
print("\n--- Assignment Operators ---")
print(f"Initial num = {num}")
num += 5
print(f"After num += 5 : {num}")
num -= 3
print(f"After num -= 3 : {num}")
num *= 2
print(f"After num *= 2 : {num}")
num /= 4
print(f"After num /= 4 : {num}")
num %= 3
print(f"After num %= 3 : {num}")

# -------------------------------
# Increment & Decrement Simulation
# -------------------------------
val = 5
print("\n--- Increment & Decrement Simulation ---")
val += 1   # Increment
print(f"Pre-increment simulation (++val): {val}")
print(f"Post-increment simulation (val++): {val}")  # Python doesn’t have ++
val -= 1   # Decrement
print(f"Pre-decrement simulation (--val): {val}")
print(f"Post-decrement simulation (val--): {val}")  # Python doesn’t have --

# -------------------------------
# Bitwise Operators
# -------------------------------
m, n = 6, 3   # Binary: m=110, n=011
print("\n--- Bitwise Operators ---")
print(f"m & n : {m & n}")   # AND
print(f"m | n : {m | n}")   # OR
print(f"m ^ n : {m ^ n}")   # XOR
print(f"~m : {~m}")         # NOT
print(f"m << 1 : {m << 1}") # Left shift
print(f"m >> 1 : {m >> 1}") # Right shift

# -------------------------------
# Conditional (Ternary) Operator
# -------------------------------
print("\n--- Conditional (Ternary) Operator ---")
a, b = 15, 20
max_val = a if a > b else b
print(f"Maximum of {a} and {b} = {max_val}")
