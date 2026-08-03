# Author: Amit Gupta
# Date: 16-07-2026
# Description: Skips invalid email entries

emails = ["amit@example.com", "invalid@", "john@gmail.com", "test"]
for e in emails:
    if "@" not in e or "." not in e:
        continue
    print("Valid email:", e)
