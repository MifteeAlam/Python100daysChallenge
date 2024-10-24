"""100 days python challenge day 5. 

"""

# Create an empty list
my_list = []

# Append elements to the list
my_list.append(10)   # Adds 10 to the end of the list
my_list.append(20)   # Adds 20 to the end of the list
my_list.append(30)   # Adds 30 to the end of the list

print("After appending:", my_list)  # Output: [10, 20, 30]

# Insert an element at a specific position
my_list.insert(1, 15)  # Inserts 15 at index 1, shifting the rest of the elements to the right
print("After inserting 15 at index 1:", my_list)  # Output: [10, 15, 20, 30]


# Remove an element by its value
my_list.remove(20)  # Removes the first occurrence of 20 from the list
print("After removing 20:", my_list)  # Output: [10, 15, 30]

# Pop an element by its index
popped_element = my_list.pop(2)  # Removes and returns the element at index 2
print("Popped element:", popped_element)  # Output: 30
print("After popping element at index 2:", my_list)  # Output: [10, 15]

# Clear all elements from the list
my_list.clear()  # Empties the list
print("After clearing the list:", my_list)  # Output: []
