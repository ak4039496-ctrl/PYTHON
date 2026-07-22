# Author: Amit Gupta
# Date: 15-07-2026
# Program: Continue on Invalid Input
# Description: Skips invalid entries

for val in ["10", "abc", "20", "xyz"]:
    if not val.isdigit():
        continue
    print("Valid number:", val)
