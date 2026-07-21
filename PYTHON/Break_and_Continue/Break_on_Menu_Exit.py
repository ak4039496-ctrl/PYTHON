# Author: Amit Gupta
# Date: 16-07-2026
# Description: Stops when user selects exit

menu = ["Start", "Settings", "Exit", "Help"]
for item in menu:
    if item == "Exit":
        print("Exiting menu...")
        break
    print("Menu option:", item)
