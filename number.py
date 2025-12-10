# Program Description:
# This program takes a word as input from the user and prints the word in reverse order.
# It uses a while loop to iterate from the last character to the first.

# Ask the user to enter a word
s = input("Enter a word: ")
rev = ""

# Start index at the last character of the string (len(s) - 1)
i = len(s) - 1

# Loop while index is greater than or equal to 0
while i >= 0:
    rev = rev + s[i] # Add the current character to the reversed string 
    # Move to the previous character
    i -= 1

# Display the reversed result
print(f"The number reversed is : {rev}")
