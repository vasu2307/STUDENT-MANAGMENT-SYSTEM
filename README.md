# STUDENT-MANAGMENT-SYSTEM
Student Management System: Description Overview  This is a menu-driven, console-based Python program that manages student records. It uses Object-Oriented Programming (a Student class) to store each student's details and marks, and lets the user add, view, search, and delete students from a list stored in memory.

## The Student Class

Each student object holds: name, age, course, and marks in Maths, Python, and English.

Method	What it does
__init__()	Constructor that stores the student's details
total()	Returns the sum of the three subject marks
average()	Returns total divided by 3
highest()	Returns the highest mark among the three subjects
lowest()	Returns the lowest mark among the three subjects
result()	Returns "Pass" if the average is 40 or more, otherwise "Fail"
display()	Prints the student's full report (average rounded to 2 decimals)
Global Variable
students = [] is an empty list that stores all Student objects while the program runs.
Functions
add_student(): Takes the student's details as input and converts age and marks to integers. If the user enters non-numeric values, a try-except block catches the ValueError and shows an error message. A new Student object is created and appended to the list.
display_students(): Shows "No students available" if the list is empty. Otherwise it loops through the list and calls display() on each student.
search_student(): Searches by name using a case-insensitive comparison (.lower()). It displays the student if found, or "Student not found."
delete_student(): Finds a student by name (case-insensitive) and removes them from the list.
Main Program Loop

A while True loop shows a menu repeatedly:

Add Student
Display Students
Search Student
Delete Student
Exit

The user's choice calls the matching function. Choosing 5 prints "Thank you!" and ends the loop with break. Any other input shows "Invalid choice!".

Key Concepts Used
Classes and objects
Methods and self
Lists
Functions
Loops and conditionals
Exception handling (try-except)
String methods (lower())
Built-ins like max(), min(), round()
Limitations
Data is not saved. All records are lost when the program closes.
Marks aren't validated (negative numbers or values over 100 are accepted).
Delete and search only handle the first student matching a name if duplicates exist.
Possible Improvements
Save data to a file (JSON/CSV) or a database
Validate marks between 0 and 100
Add an "update student" option
Add grade categories (A, B, C, etc.)

## screanshorts:
<img width="647" height="945" alt="Screenshot 2026-10-06 193814" src="https://github.com/user-attachments/assets/4d7e6cdb-5760-4e23-82f3-0b20e368fa23" />
<img width="511" height="886" alt="Screenshot 2026-10-06 193847" src="https://github.com/user-attachments/assets/73cad3c7-9556-45e3-a2c1-3b01894793b6" />
<img width="511" height="886" alt="Screenshot 2026-10-06 193847" src="https://github.com/user-attachments/assets/3be40b3f-2ed7-4b70-bba9-a53ab826e352" />

## code:
class Student:

    def __init__(self, name, age, course, maths, python, english):
        self.name = name
        self.age = age
        self.course = course
        self.maths = maths
        self.python = python
        self.english = english

    def total(self):
        return self.maths + self.python + self.english

    def average(self):
        return self.total() / 3

    def highest(self):
        return max(self.maths, self.python, self.english)

    def lowest(self):
        return min(self.maths, self.python, self.english)

    def result(self):
        if self.average() >= 40:
            return "Pass"
        else:
            return "Fail"

    def display(self):
        print("\n-------------------------")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Total:", self.total())
        print("Average:", round(self.average(), 2))
        print("Highest Mark:", self.highest())
        print("Lowest Mark:", self.lowest())
        print("Result:", self.result())
        print("-------------------------")


students = []


def add_student():

    name = input("Enter student name: ")

    try:
        age = int(input("Enter age: "))
        maths = int(input("Enter Maths marks: "))
        python_marks = int(input("Enter Python marks: "))
        english = int(input("Enter English marks: "))

    except ValueError:
        print("Please enter valid numbers!")
        return

    course = input("Enter course: ")

    student = Student(
        name,
        age,
        course,
        maths,
        python_marks,
        english
    )

    students.append(student)

    print("Student added successfully!")


def display_students():

    if len(students) == 0:
        print("No students available.")
        return

    for student in students:
        student.display()


def search_student():

    name = input("Enter student name: ")

    for student in students:

        if student.name.lower() == name.lower():
            student.display()
            return

    print("Student not found.")


def delete_student():

    name = input("Enter student name: ")

    for student in students:

        if student.name.lower() == name.lower():

            students.remove(student)

            print("Student deleted successfully!")
            return

    print("Student not found.")


while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")

    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")

## final conclusion:
The project successfully implements a basic Student Management System in Python using OOP concepts. It efficiently manages student records and results, and it can be enhanced in the future with file storage, stronger validation, and additional features.
        
