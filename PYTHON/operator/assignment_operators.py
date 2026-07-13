# Author:-Amit Kumar
# Date:- 2026-07-10

# Declare integer variable 'num' and assign value 11
num = 11

# Simple assignment (=) assigns value to variable
print(f"Initial value of num :- {num}")

# Add and assign (+=) -> num = num + 5
num += 5
print(f"After num += 5, num => {num}")

# Subtract and assign (-=) -> num = num - 3
num -= 3
print(f"After num -= 3, num => {num}")

# Multiply and assign (*=) -> num = num * 2
num *= 2
print(f"After num *= 2, num => {num}")

# Divide and assign (//=) -> num = num // 4
# Note: We use '//=' for integer division to perfectly mimic C's integer truncation.
num //= 4
print(f"After num /= 4, num => {num}")

# Modulus and assign (%=) -> num = num % 3
num %= 3
print(f"After num %= 3, num => {num}")