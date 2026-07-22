# Author: Amit Gupta
# Date: 15-07-2026
# Program: Break on Password Match
# Description: Stops when correct password entered

while True:
    pwd = input("Enter password:- ")
    if pwd == "Amit@123":
        print("Access granted")
        break
    else:
        print("Try again")
