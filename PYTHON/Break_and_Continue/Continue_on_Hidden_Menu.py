# Author: Amit Gupta
# Date: 16-07-2026
# Description: Skips hidden menu option

menu = ["Start", "Hidden", "Settings", "Help"]
for item in menu:
    if item == "Hidden":
        continue
    print("Menu option:", item)
