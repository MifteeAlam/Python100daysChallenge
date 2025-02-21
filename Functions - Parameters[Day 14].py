
'''Day 14	#100 Days Python Challenge
Functions - Parameters	
Create a function with parameters and print the results.'''



# 1️⃣ Basic Function with Parameters
def add_numbers(a, b):
    return a + b

# 2️⃣ Function with Default Parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")

# 3️⃣ Function with Multiple Parameters (Keyword Arguments)
def introduce(name, age, country="USA"):
    print(f"My name is {name}, I am {age} years old, from {country}.")

# 4️⃣ Function with Variable-Length Arguments (*args, **kwargs)
def sum_all(*numbers):
    return sum(numbers)

def print_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

# 5️⃣ Function with List & Dictionary as Parameters
def double_numbers(numbers):
    return [n * 2 for n in numbers]

def student_info(student):
    print(f"Name: {student['name']}, Grade: {student['grade']}")

# 6️⃣ Lambda Function
square = lambda x: x * x
multiply = lambda a, b: a * b

# Calling functions to demonstrate their usage
print(f"Sum: {add_numbers(5, 10)}")  # Basic function

greet()  # Default parameter
greet("Alice")

introduce("John", 30)  # Keyword arguments
introduce(age=25, name="Emily", country="Canada")

print(f"Total Sum: {sum_all(1, 2, 3, 4, 5)}")  # *args







