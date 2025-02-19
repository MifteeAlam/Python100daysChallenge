'''Day 12	#100 Days Python Challenge
Control Structures - Break and Continue	
Write a loop that uses break and continue statements.'''


# Initialize a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Loop through the numbers
for num in numbers:
    if num % 2 == 0:
        print(f"Even number {num} encountered, skipping it.")
        continue  # Skip even numbers

    if num == 7:
        print("Number 7 encountered, exiting the loop.")
        break  # Exit the loop when number 7 is encountered

    print(f"Processing number: {num}")
