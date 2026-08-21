# Author: Amit Gupta
# Date: 18-07-2026

# Variable to store student marks
marks = int(input("Enter your marks (0-100):- "))

# Check if marks are greater than or equal to 90
if marks >= 90 and marks<=100:
    print("Grade:- A")  # Print Grade A
# Check if marks are between 75 and 89
elif marks >= 75 and marks<=90:
    print("Grade- B")  # Print Grade B
# Check if marks are between 50 and 74
elif marks >= 50 and marks<=75:
    print("Grade:- C")  # Print Grade C
# Check if marks are between 33 and 49
elif marks >= 33 and marks<=50:
    print("Grade:- D")  # Print Grade D
# If marks are below 33
else:
    print("Grade=> F (Fail)")  # Print Fail
    