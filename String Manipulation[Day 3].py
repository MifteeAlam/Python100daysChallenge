""" 
100 Days Python Challenge !  Day 3
String Manipulation Example
"""

# Concatenation
str1 = "Hello"
str2 = "World"
concatenated = str1 + " " + str2
print("Concatenated String:", concatenated)  # Output: Hello World

# Slicing
my_string = "PythonProgramming"
sliced_part = my_string[:6] # Slicing the word 'Python'
print("Sliced String:", sliced_part)  # Output: Python

# Reversing a string
reversed_string = my_string[::-1]
print("Reversed String:", reversed_string)  # Output: gnimmargorPnohtyP

# Changing case
upper_case = concatenated.upper()
lower_case = concatenated.lower()
print("Uppercase:", upper_case)  # Output: HELLO WORLD
print("Lowercase:", lower_case)  # Output: hello world

# Replacing a substring
replaced_string = my_string.replace("Python", "Java")
print("Replaced String:", replaced_string)  # Output: JavaProgramming

# Splitting and joining
split_words = concatenated.split()  # Splits the string into a list of words
joined_string = "-".join(split_words)
print("Joined String:", joined_string)  # Output: Hello-World
