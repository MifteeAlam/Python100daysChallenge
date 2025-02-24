
''' 100 Days Coding Challenge
Day 16	Functions - Lambda Functions	
Create a lambda function to double a number.'''



# Get two numbers from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Lambda functions for basic arithmetic
addition = lambda x, y: x + y
subtraction = lambda x, y: x - y
multiplication = lambda x, y: x * y
division = lambda x, y: x / y if y != 0 else "Cannot divide by zero"

# Display results
print(f"Addition: {addition(a, b)}")
print(f"Subtraction: {subtraction(a, b)}")
print(f"Multiplication: {multiplication(a, b)}")
print(f"Division: {division(a, b)}")


