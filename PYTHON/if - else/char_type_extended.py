# Author: Amit Gupta
# Date: 18-07-2026

# Ask user to enter a character
ch = input("Enter a character:- ")[:1]

# Print the entered character
print(f"You entered:- {ch}")

# Check if character is uppercase alphabet
if 'A' <= ch <= 'Z':
    print(f"{ch} is Uppercase Alphabet")
# Check if character is lowercase alphabet
elif 'a' <= ch <= 'z':
    print(f"{ch} is Lowercase Alphabet")
# Check if character is digit
elif '0' <= ch <= '9':
    print(f"{ch} is a Digit")
# Else condition for special characters
else:
    print(f"{ch} is a Special Character")