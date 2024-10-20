# List example
my_list = [1, 2, 3]
my_list.append(411)  # Modifying the list

print("List:", my_list)  # Output: [1, 2, 3, 4]

# Tuple example
my_tuple = (1, 2, 3)
#my_tuple.append(4)  # This would raise an error, tuples are immutable
print("Tuple:", my_tuple)  # Output: (1, 2, 3)


numbers=[5,2,9,1,8,6,109,121,999,187,25]
numbers.sort()
print("Sorted using sort():",numbers)

sorted_numbers=sorted(numbers)
print("Sorted using sorted():",sorted_numbers)

"""Key Points:
sort() vs sorted(): Choose sort() if you want to modify the original list. Use sorted() if you want a new sorted list without changing the original.
Sorting in Ascending Order: By default, both methods sort the data in ascending order. If you want to sort in descending order, you can pass an additional argument reverse=True.
 """
sorted_numbers = sorted(numbers, reverse=True)  # Sorts in descending order
print(sorted_numbers)  # Output: [9, 6, 5, 5, 2, 1]

# Step 1: Create an empty list
numbers = []

# Step 2: Add 5 numbers to the list
for i in range(5):
    # Ask the user for a number
    num = float(input("Enter number {}: ".format(i + 1)))  # Adjust to int() if you want integers
    numbers.append(num)  # Add the number to the list

# Step 3: Print the list
print("The numbers in the list are:", numbers)
