#Program Description: The purpose of this program is to reverse the number entered by the user


# Take the number from the user as a string (so we can access each digit easily)
n = input("Enter a number: ")

rev = ""            # This will store the reversed number
i = len(n) - 1      # Start from the last index of the string

# Loop backward through the string
while i >= 0:
    rev = rev + n[i]   # Add the current character to the reversed string
    i -= 1             # Move to the previous character

# Display the reversed result
print(f"The number reversed is : {rev}")
