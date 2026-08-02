# Author: Amit Gupta
# Date: 16-07-2026
# Description: Skips negative values

nums = [10, -5, 20, -3, 30]
for n in nums:
    if n < 0:
        continue
    print(n)
