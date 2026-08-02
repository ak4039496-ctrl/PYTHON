# Author: Amit Gupta
# Date: 16-07-2026
# Description: Skips empty lines

lines = ["Hello", "", "World", "", "Python"]
for line in lines:
    if line == "":
        continue
    print(line)
