
'''100 days of python challenge. 
Day 4 : Print a List of numbers'''


# Creating a list of numbers
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Printing the list
print("List of numbers:", numbers_list)
# Printing the list of numbers vertically using join and newline character
vertical_numbers = "\n".join(map(str, numbers_list))
print("The vertical Numbers are:",vertical_numbers)