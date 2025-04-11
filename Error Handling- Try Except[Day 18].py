''' 100 days Coding Challenge
Day 18	Error Handling - Try/Except
Handle an exception for dividing by zero.'''

# Step 1: Define the numerator and denominator
numerator = 10
denominator = 0  # This will cause a ZeroDivisionError if we try to divide by it

# Step 2: Use a try/except block to handle the potential error
try:
    # Attempt to perform the division
    result = numerator / denominator
    # If successful, print the result
    print("The result is:", result)

# Step 3: Catch the ZeroDivisionError if it occurs
except ZeroDivisionError:
    # Print a user-friendly error message
    print("Error: You tried to divide by zero, which is not allowed.")

# Optional: Add a generic exception catch block (not necessary here, but useful for debugging)
except Exception as e:
    # Print the actual error message for any other unexpected errors
    print("An unexpected error occurred:", e)

# Step 4: Continue the program
print("Program continues after error handling.")
