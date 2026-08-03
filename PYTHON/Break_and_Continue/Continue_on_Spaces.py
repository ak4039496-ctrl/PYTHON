# Author: Amit Gupta
# Date: 16-07-2026
# Description: Skips spaces in text

text = "python programming"
for ch in text:
    if ch == " ":
        continue
    print(ch, end="")
