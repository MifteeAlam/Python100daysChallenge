
'''Day 13	#100 Days Python Challenge
Functions - Definition	
Define a function that returns the square of a number.'''


# Function definition
def square(num):
    """
    This function takes a number as input and returns its square.
    
    Parameters:
    num (int or float): The number to be squared.
    
    Returns:
    int or float: The square of the input number.
    """
    squared_value = num ** 2  # Compute the square
    return squared_value  # Return the computed square

# Taking user input
try:
    user_input = float(input("Enter a number to find its square: "))  # Convert input to float
    result = square(user_input)  # Call the function
    print(f"The square of {user_input} is {result}")  # Display the result

except ValueError:
    print("Invalid input! Please enter a valid number.")  # Handle non-numeric input
