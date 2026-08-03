# Author: Amit Gupta
# Date: 15-07-2026
# Description: Skips j=3 in inner loop

for i in range(1, 4):
    for j in range(1, 6):
        if j == 3:
            continue
        print(f"i={i}, j={j}")
