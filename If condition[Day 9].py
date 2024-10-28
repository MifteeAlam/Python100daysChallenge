''' 100 days Python Challenge
Day 9	Control Structures - If Statements	Write a program using if-elif-else for basic conditions.'''


# Get user input and convert it to an integer
number = int(input("Enter a number: "))

# Use if-elif-else structure to check conditions
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
