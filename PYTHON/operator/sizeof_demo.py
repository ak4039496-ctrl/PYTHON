# Author:-Amit Kumar
# Date:- 2026-07-10
import sys   # System library to get memory size details

# Declare variables
a = 0         # Integer
ch = 'A'      # String/Character
f = 0.0       # Float (Python floats are double-precision by default)

# Print size of each variable using sys.getsizeof()
print("Size of int =>", sys.getsizeof(a), "bytes")
print("Size of char =>", sys.getsizeof(ch), "bytes")
print("Size of float =>", sys.getsizeof(f), "bytes")