# Author: Amit Gupta
# Date: 16-07-2026
# Description: Skips words shorter than 5 letters

words = ["cat", "python", "java", "elephant"]
for w in words:
    if len(w) < 5:
        continue
    print(w)
