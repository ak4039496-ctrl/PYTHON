# Author:-Amit Kumar
# Date:- 2026-07-10

# -------------------------------
# Arithmetic Operators
# -------------------------------
a = 10
b = 3

print("\n--- Arithmetic Operators ---")
print(f"Addition:- {a} + {b} => {a + b}")
print(f"Subtraction:- {a} - {b} => {a - b}")
print(f"Multiplication:- {a} * {b} => {a * b}")
print(f"Division:- {a} / {b} => {a // b}") # Using // to mimic C's integer truncation behavior
print(f"Modulus:- {a} % {b} => {a % b}")

# -------------------------------
# Relational Operators
# -------------------------------
x = 5
y = 10

print("\n--- Relational Operators ---")
# Python comparison returns True/False. We use int() to convert it into 1/0 to match C's print statements.
print(f"x > y :- {int(x > y)}")
print(f"x < y :- {int(x < y)}")
print(f"x == y :- {int(x == y)}")
print(f"x != y :- {int(x != y)}")
print(f"x >= y :- {int(x >= y)}")
print(f"x <= y : {int(x <= y)}")

# -------------------------------
# Logical Operators
# -------------------------------
p = 1
q = 0

print("\n--- Logical Operators ---")
# Python uses readable keyword replacements ('and', 'or', 'not') for logic
print(f"p && q :- {int(p and q)}")
print(f"p || q :- {int(p or q)}")
print(f"!p :- {int(not p)}")
print(f"!q :- {int(not q)}")

# -------------------------------
# Assignment Operators
# -------------------------------
num = 10

print("\n--- Assignment Operators ---")
print(f"Initial num => {num}")
num += 5
print(f"After num += 5 :- {num}")
num -= 3
print(f"After num -= 3 :- {num}")
num *= 2
print(f"After num *= 2 :- {num}")
num //= 4 # Using //= to match integer truncation
print(f"After num /= 4 :- {num}")
num %= 3
print(f"After num %= 3 :- {num}")

# -------------------------------
# Increment & Decrement Operators
# -------------------------------
val = 5

print("\n--- Increment & Decrement Operators ---")
# Note: Python does not have standard ++ or -- operators. We simulate their logic manually.

# Pre-increment (++val): increase first, then display
val += 1
print(f"Pre-increment (++val) :- {val}")

# Post-increment (val++): display first, then increase
print(f"Post-increment (val++) :- {val}")
val += 1

print(f"Value after post-increment :- {val}")

# Pre-decrement (--val): decrease first, then display
val -= 1
print(f"Pre-decrement (--val) :- {val}")

# Post-decrement (val--): display first, then decrease
print(f"Post-decrement (val--) :- {val}")
val -= 1

print(f"Value after post-decrement :- {val}")

# -------------------------------
# Bitwise Operators
# -------------------------------
m = 6
n = 3

print("\n--- Bitwise Operators ---")
print(f"m & n :- {m & n}")   # Bitwise AND
print(f"m | n :- {m | n}")   # Bitwise OR
print(f"m ^ n :- {m ^ n}")   # Bitwise XOR
print(f"~m :- {~m}")         # Bitwise NOT
print(f"m << 1 :- {m << 1}") # Left shift
print(f"m >> 1 :- {m >> 1}") # Right shift