#Enter Name Program
#Program Description: This program requires the user to type their name

#variable to store user name
name = input("Enter your name: ")

#while loop will run as long as the variable name has nothing stored in it
while name == "" or not name.isalpha():
    print("Invalid name")
    #Asking the user to enter their name in case they didn't type anything
    name = input("Enter your name: ")

#Exit out of the loop once the user has typed their
print(f"Hello {name}")
