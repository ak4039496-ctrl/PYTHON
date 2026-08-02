# Author: Amit Gupta
# Date: 15-07-2026
# Program: Continue on Non-Prime
# Description: Prints only prime numbers

nums = [4, 6, 8, 9, 11, 15]
for n in nums:
    if any(n % i == 0 for i in range(2, n)):
        continue
    print("Prime:", n)
