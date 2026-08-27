# Author: Amit Gupta
# Date: 18-07-2026

def main():
    # Ask user to enter operator
    op = input("Enter operator (+, -, *, /):- ").strip()

    # Ask user to enter two numbers
    num1 = float(input("Enter first number:- "))
    num2 = float(input("Enter second number:- "))

    # If operator is '+'
    if op == '+':
        print(f"Result:- {num1 + num2:.3f}")  # Addition (formatted to 3 decimal places)
    # If operator is '-'
    elif op == '-':
        print(f"Result:- {num1 - num2:.2f}")  # Subtraction (formatted to 2 decimal places)
    # If operator is '*'
    elif op == '*':
        print(f"Result:- {num1 * num2:.2f}")  # Multiplication
    # If operator is '/'
    elif op == '/':
        # Check if denominator is not zero
        if num2 != 0:
            print(f"Result:- {num1 / num2:.2f}")  # Division
        else:
            print("Error! Division by zero.")
    else:
        print("Error! Invalid operator.")

if __name__ == "__main__":
    main()