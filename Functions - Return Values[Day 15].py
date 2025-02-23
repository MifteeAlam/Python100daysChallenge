'''Day 15  #100 Days Python Challenge
Functions - Return Values
Write a function that returns multiple values (e.g., min and max).1 2'''

def analyze_numbers(numbers):
    """Return various statistics from a list of numbers."""
    if not numbers:  # Check for an empty list
        return None, None, None, 0, 0
    
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    
    even_count = sum(1 for n in numbers if n % 2 == 0)  # Count even numbers
    odd_count = len(numbers) - even_count  # Total numbers minus even numbers
    
    return minimum, maximum, average, even_count, odd_count

# User input
user_input = input("Enter a list of numbers separated by spaces: ")
numbers_list = list(map(int, user_input.split()))  # Convert input to a list of integers

# Analyze the numbers
minimum, maximum, average, even_count, odd_count = analyze_numbers(numbers_list)

# Output the results
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Average: {average:.2f}")  # Formatting the average to two decimal places
print(f"Count of Even Numbers: {even_count}")
print(f"Count of Odd Numbers: {odd_count}")
