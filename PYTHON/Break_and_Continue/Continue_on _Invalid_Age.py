# Author: Amit Gupta
# Date: 16-07-2026
# Description: Skips invalid ages

ages = [25, -5, 30, -1, 40]
for age in ages:
    if age < 0:
        continue
    print("Valid age:", age)
