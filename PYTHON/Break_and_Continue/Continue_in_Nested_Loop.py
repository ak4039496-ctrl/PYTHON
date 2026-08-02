# Author: Amit Gupta
# Date: 16-07-2026
# Description: Stops inner loop when j equals 3

for i in range(1, 4):
    for j in range(1, 6):
        if j == 3:
            break
        print(f"i={i}, j={j}")
