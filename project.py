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
        