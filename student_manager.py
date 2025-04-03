print("Quan ly sinh vien")
# This is a simple student management system    
# that allows you to add, view, and delete students.
# It uses a dictionary to store student information.
# Each student has a name, age, and ID.
# The system allows you to add a student, view all students, and delete a student by ID.




# Function to add a student
def add_student(students):
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    student_id = input("Enter student ID: ")
    students[student_id] = {"name": name, "age": age}
    print(f"Student {name} added successfully!")