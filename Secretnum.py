# Guess the Secret Number Game

#Program Description: The user must guess the secret number. The loop continues until they guess correctly, giving hints along the way.

# The number the user has to guess
secret = 7

# Set the first guess to 0 (or any value not equal to secret)
guess = 0

# Keep looping until the guess is equal to the secret number
while guess != secret:
    guess = int(input("Guess the secret number between 1 and 10: "))  # Ask for a guess
    
    # Check if the guess is too low, too high, or correct
    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print("🎉 You got it right!")
