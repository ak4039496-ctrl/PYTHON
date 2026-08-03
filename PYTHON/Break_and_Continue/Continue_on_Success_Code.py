# Author: Amit Gupta
# Date: 15-07-2026
# Description: Prints only error codes

codes = [200, 201, 404, 500]
for c in codes:
    if c < 400:
        continue
    print("Error code:", c)
