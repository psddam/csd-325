# Name: Peter Ddamulira
# Assignment: Module 8.2 - JSON Student List
# Description:
# This program loads student records from a JSON file, displays the
# original list, adds a new student, displays the updated list,
# and writes the updated information back to the JSON file.

import json


def print_students(student_list):
    """Print each student in the required format."""
    for student in student_list:
        print(
            f"{student['L_Name']}, {student['F_Name']} : "
            f"ID = {student['Student_ID']} , "
            f"Email = {student['Email']}"
        )


# Open and load the JSON file
with open("student.json", "r") as file:
    students = json.load(file)

# Display the original student list
print("\nOriginal Student List")
print("-----------------------------")
print_students(students)

# Create your new student record
new_student = {
    "F_Name": "Peter",
    "L_Name": "Ddamulira",
    "Student_ID": 72568,
    "Email": "pddamulira@example.com"
}

# Only add the student if they are not already in the list
student_exists = False

for student in students:
    if student["Student_ID"] == new_student["Student_ID"]:
        student_exists = True
        break

if not student_exists:
    students.append(new_student)
else:
    print("\nPeter Ddamulira is already in the student list.")

# Display the updated student list
print("\nUpdated Student List")
print("-----------------------------")
print_students(students)

# Save the updated list back to the JSON file
with open("student.json", "w") as file:
    json.dump(students, file, indent=4)

# Notify the user
print("\nThe student.json file was updated successfully.")