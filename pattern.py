# Program Description:
# This program prints a pattern of numbers. 
# For a given number n, it prints each number from 1 to n,
# repeated as many times as its value.

# Ask the user to enter a number and convert it to an integer
n = int(input("Enter a number: "))

# Start a counter i at 1
i = 1

# Loop from 1 to n (inclusive)
while i <= n:
    # Print the number i repeated i times
    # str(i) converts the number to a string so it can be repeated
    print(str(i) * i)
    
    # Move to the next number
    i += 1
