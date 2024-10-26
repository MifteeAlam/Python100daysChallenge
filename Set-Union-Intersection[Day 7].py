'''Day 7	#100 Days Python Challenge
Python Basics - Sets	
Create sets and perform union and intersection operations.'''


# Step 1: Define sets
# We create two sets, set_a and set_b, each containing some integers.
# Sets in Python automatically remove duplicate values.
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Display the sets to understand what elements are in each
print("Set A:", set_a)
print("Set B:", set_b)

# Step 2: Perform Union Operation
# The union of two sets includes all unique elements from both sets.
# We can perform a union using either the '|' operator or the union() method.

# Using the '|' operator to find the union of set_a and set_b
union_set_operator = set_a | set_b

# Using the union() method to achieve the same result
union_set_method = set_a.union(set_b)

# Display the results of the union operation
print("Union using '|' operator:", union_set_operator)
print("Union using union() method:", union_set_method)

# Step 3: Perform Intersection Operation
# The intersection of two sets includes only the elements present in both sets.
# We can perform an intersection using either the '&' operator or the intersection() method.

# Using the '&' operator to find the intersection of set_a and set_b
intersection_set_operator = set_a & set_b

# Using the intersection() method to achieve the same result
intersection_set_method = set_a.intersection(set_b)

# Display the results of the intersection operation
print("Intersection using '&' operator:", intersection_set_operator)
print("Intersection using intersection() method:", intersection_set_method)
