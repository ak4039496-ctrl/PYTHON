# Author: Amit Gupta
# Date: 15-07-2026
# Description: Prints only matching numbers

nums = [10, 20, 30, 40, 50]
target = 30
for n in nums:
    if n != target:
        continue
    print("Match:", n)
