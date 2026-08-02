# Author: Amit Gupta
# Date: 16-07-2026
# Description: Stops when error code found

codes = [200, 201, 404, 500]
for c in codes:
    if c >= 400:
        print("Error code:", c)
        break
    print("Success code:", c)
