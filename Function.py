#Program Description: Here a function called add(a, b) is created where 
# any given two numbers are added together. 

#Creating the function called add which has two parameters a & b. 
def add(a, b):
    return a + b


#Recieving two no.s from the user and converting it to 
# float for smooth addition. 

num1 = float(input("Enter the first number: "))

num2 = float(input("Enter the second number: "))


#Calling the add function and printing the result. 

print(f"The numbers {num1} and {num2} added together = {add(num1, num2)}" )

#Creating the remaining functions

#Subtraction Function
#Create a function which performs subtraction called sub(a-b)

def sub(a,b):
    return a - b 

#Multiplication
#Create a function which performs multiplication called mul(a * b)
def mul(a,b):
    return a*b

#Printing the multiplication and subtraction 

print(f"The numbers {num1} and {num2} subtracted together  = {sub(num1, num2)}")
print(f"The numbers {num1} and {num2} multiplied together = {mul(num1,num2)}")
