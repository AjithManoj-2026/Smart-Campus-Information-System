# ==========================================
# SEARCHING & SORTING MODULE
# Smart Campus Information System
# ==========================================

import json
import os

# ------------------------------------------
# Load Students
# ------------------------------------------
def load_students():

    if not os.path.exists("data/students.json"):

        print("Student database not found.")
        return []

    with open("data/students.json", "r") as file:

        return json.load(file)


# ------------------------------------------
# Display Student
# ------------------------------------------
def display_student(student):

    print("\n===================================")

    print(f"Student ID   : {student['student_id']}")
    print(f"Name         : {student['name']}")
    print(f"Department   : {student['department']}")
    print(f"Semester     : {student['semester']}")
    print(f"CGPA         : {student['cgpa']}")
    print(f"Attendance   : {student['attendance']}%")
    print(f"Fees Paid    : {student['fees_paid']}")

    print("===================================")


# ------------------------------------------
# Search by Student ID
# ------------------------------------------
def search_by_id():

    students = load_students()

    student_id = input("\nEnter Student ID : ")

    found = False

    for student in students:

        if student["student_id"] == student_id:

            display_student(student)

            found = True
            break

    if not found:

        print("Student not found.")


# ------------------------------------------
# Search by Name
# ------------------------------------------
def search_by_name():

    students = load_students()

    name = input("\nEnter Student Name : ").lower()

    found = False

    for student in students:

        if name in student["name"].lower():

            display_student(student)

            found = True

    if not found:

        print("No matching students found.")


# ------------------------------------------
# Search by Department
# ------------------------------------------
def search_by_department():

    students = load_students()

    department = input("\nEnter Department : ").lower()

    found = False

    for student in students:

        if department == student["department"].lower():

            display_student(student)

            found = True

    if not found:

        print("No students found in this department.")


# ------------------------------------------
# Filter High CGPA Students
# ------------------------------------------
def filter_high_cgpa():

    students = load_students()

    minimum_cgpa = float(
        input("\nEnter Minimum CGPA : ")
    )

    found = False

    print("\n========== HIGH CGPA STUDENTS ==========")

    for student in students:

        if student["cgpa"] >= minimum_cgpa:

            display_student(student)

            found = True

    if not found:

        print("No matching students found.")


# ------------------------------------------
# Attendance Defaulter Search
# ------------------------------------------
def attendance_defaulters():

    students = load_students()

    found = False

    print("\n========== ATTENDANCE DEFAULTERS ==========")

    for student in students:

        if student["attendance"] < 75:

            display_student(student)

            found = True

    if not found:

        print("No attendance defaulters found.")


# ------------------------------------------
# Sort by CGPA
# ------------------------------------------
def sort_by_cgpa():

    students = load_students()

    sorted_students = sorted(

        students,

        key=lambda student: student["cgpa"],

        reverse=True
    )

    print("\n========== STUDENTS SORTED BY CGPA ==========")

    rank = 1

    for student in sorted_students:

        print(f"\nRank : {rank}")

        display_student(student)

        rank += 1


# ------------------------------------------
# Sort by Attendance
# ------------------------------------------
def sort_by_attendance():

    students = load_students()

    sorted_students = sorted(

        students,

        key=lambda student: student["attendance"],

        reverse=True
    )

    print("\n========== STUDENTS SORTED BY ATTENDANCE ==========")

    rank = 1

    for student in sorted_students:

        print(f"\nRank : {rank}")

        display_student(student)

        rank += 1


# ------------------------------------------
# Search Students with Skills
# ------------------------------------------
def search_by_skill():

    students = load_students()

    skill = input("\nEnter Skill : ").lower()

    found = False

    print("\n========== STUDENTS WITH MATCHING SKILLS ==========")

    for student in students:

        skills = [

            s.strip().lower()

            for s in student["skills"]
        ]

        if skill in skills:

            display_student(student)

            found = True

    if not found:

        print("No students found with this skill.")


# ------------------------------------------
# AI-like Academic Risk Detection
# ------------------------------------------
def academic_risk_students():

    students = load_students()

    found = False

    print("\n========== ACADEMIC RISK STUDENTS ==========")

    for student in students:

        if student["cgpa"] < 5 and student["attendance"] < 75:

            display_student(student)

            print("Risk Status : HIGH RISK")

            found = True

    if not found:

        print("No high-risk students detected.")


# ------------------------------------------
# Main Menu
# ------------------------------------------
while True:

    print("\n========== SEARCH & SORT MODULE ==========")

    print("1. Search by Student ID")
    print("2. Search by Name")
    print("3. Search by Department")
    print("4. Filter High CGPA Students")
    print("5. Attendance Defaulters")
    print("6. Sort by CGPA")
    print("7. Sort by Attendance")
    print("8. Search by Skill")
    print("9. Academic Risk Students")
    print("10. Exit")

    choice = input("\nEnter your choice : ")

    if choice == "1":

        search_by_id()

    elif choice == "2":

        search_by_name()

    elif choice == "3":

        search_by_department()

    elif choice == "4":

        filter_high_cgpa()

    elif choice == "5":

        attendance_defaulters()

    elif choice == "6":

        sort_by_cgpa()

    elif choice == "7":

        sort_by_attendance()

    elif choice == "8":

        search_by_skill()

    elif choice == "9":

        academic_risk_students()

    elif choice == "10":

        print("Exiting Search & Sort Module...")
        break

    else:

        print("Invalid choice.")