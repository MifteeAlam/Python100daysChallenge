''' 100 days Coding Challenge
Day 17	Lists - List Comprehensions	
Use list comprehensions to create a list of squares from 1 to 10.'''



# Using list comprehension to create a list of squares from 1 to 10
squares = [x**2 for x in range(1, 11)]
print(squares)  # Output: [1, 4, 9, 6, 25, 36, 49, 64, 81, 100]


''' Extras

# Get user input for range
N = int(input("Enter the range (N): "))

# 1️⃣ Generate a list of squares from 1 to N
squares = [x**2 for x in range(1, N+1)]

# 2️⃣ Filter out even squares (keep only odd squares)
odd_squares = [sq for sq in squares if sq % 2 != 0]

# 3️⃣ Calculate the sum of odd squares
sum_odd_squares = sum(odd_squares)

# 4️⃣ Create a dictionary mapping numbers to their squares
square_dict = {x: x**2 for x in range(1, N+1)}

# Print results
print(f"\nList of Squares: {squares}")
print(f"Odd Squares Only: {odd_squares}")
print(f"Sum of Odd Squares: {sum_odd_squares}")
print(f"Number-Square Dictionary: {square_dict}")
'''