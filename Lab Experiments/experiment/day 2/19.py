
# Complete Student, Teacher, Subject, Name and DOB Database

# Student database: name and date of birth
students = {
    "Rahul": "2004-05-12",
    "Priya": "2005-08-20",
    "Arun": "2004-11-15",
    "Pavan": "2005-01-10"
}

# Teacher database
teachers = {
    "Ramesh": "Python",
    "Suresh": "Java",
    "Lakshmi": "DBMS",
    "Kumar": "Python"
}

# Subject database
subjects = ["Python", "Java", "DBMS"]

# Student and subject relationships
student_subjects = {
    "Rahul": "Python",
    "Priya": "Java",
    "Arun": "DBMS",
    "Pavan": "Python"
}


# Display all students with DOB
def display_students():
    print("\n--- Student Name and DOB ---")
    for name, dob in students.items():
        print("Name:", name, "| DOB:", dob)


# Display all teachers and their subjects
def display_teachers():
    print("\n--- Teacher and Subject ---")
    for teacher, subject in teachers.items():
        print("Teacher:", teacher, "| Subject:", subject)


# Display all subjects
def display_subjects():
    print("\n--- Available Subjects ---")
    for subject in subjects:
        print(subject)


# Search student details
def search_student():
    name = input("Enter student name: ").strip().title()
    if name in students:
        print("Name:", name)
        print("DOB:", students[name])
        print("Subject:", student_subjects[name])
    else:
        print("Student not found.")


# Find teacher for a subject
def search_teacher():
    subject = input("Enter subject: ").strip().lower()
    found = False

    for teacher, taught_subject in teachers.items():
        if taught_subject.lower() == subject:
            print("Teacher:", teacher)
            found = True

    if not found:
        print("No teacher found for this subject.")


# Main menu
while True:
    print("\n===== DATABASE MENU =====")
    print("1. Display Students and DOB")
    print("2. Display Teachers and Subjects")
    print("3. Display All Subjects")
    print("4. Search Student Details")
    print("5. Search Teacher by Subject")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        display_students()
    elif choice == "2":
        display_teachers()
    elif choice == "3":
        display_subjects()
    elif choice == "4":
        search_student()
    elif choice == "5":
        search_teacher()
    elif choice == "6":
        print("Program ended.")
        break
    else:
        print("Invalid choice. Please try again.")
