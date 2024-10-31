
'''                  100 days python Challenge
Day 10	Control Structures - Loops	Use a for loop to iterate through a list.'''

# List of dictionaries representing students and their grades
students = [
    {"name": "Alice", "grades": [85, 90, 88, 92]},
    {"name": "Bob", "grades": [78, 82, 84, 80]},
    {"name": "Charlie", "grades": [90, 92, 85, 87]},
    {"name": "Diana", "grades": [72, 75, 78, 74]},
]

# Initialize an empty list to store summary reports
summary_reports = []

# Use a for loop to iterate through each student in the list
for student in students:
    # Extract the student's name and grades
    name = student["name"]
    grades = student["grades"]
    print(name)
    print(grades)
    
    # Calculate the average grade
    total = 0
    for grade in grades:
        total += grade
    average_grade = total / len(grades)
    print(average_grade)
    
    # Determine pass/fail status based on the average grade
    status = "Pass" if average_grade >= 75 else "Fail"
    
    # Create a summary report for each student
    report = f"Student: {name}\nAverage Grade: {average_grade:.2f}\nStatus: {status}\n"
    summary_reports.append(report)
    
# Print each summary report
for report in summary_reports:
    print(report)
    print("-" * 20)
