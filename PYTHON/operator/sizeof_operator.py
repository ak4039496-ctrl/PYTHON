"""
Author      : Amit Gupta
Description : Demonstrates sizeof equivalent in Python using sys.getsizeof()
Created on  : July 9, 2026
"""
import sys   # Import sys module for getsizeof()

# Variables of different data types
a = 10        # Integer variable
c = 'A'       # Character (string of length 1)
f = 3.14      # Float variable
d = 3.14159   # Double precision float (Python float is double precision)

print("\n--- sizeof Equivalent in Python ---")

# sys.getsizeof() gives memory size in bytes
print(f"Size of int type: {sys.getsizeof(0)} bytes")
print(f"Size of char type: {sys.getsizeof('A')} bytes")
print(f"Size of float type: {sys.getsizeof(0.0)} bytes")
print(f"Size of variable a: {sys.getsizeof(a)} bytes")
print(f"Size of variable c: {sys.getsizeof(c)} bytes")
print(f"Size of variable f: {sys.getsizeof(f)} bytes")
print(f"Size of variable d: {sys.getsizeof(d)} bytes")
