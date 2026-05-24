# ==========================================
# GRADE EVALUATION MODULE
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
# Save Students
# ------------------------------------------
def save_students(students):

    with open("data/students.json", "w") as file:

        json.dump(students, file, indent=4)


# ------------------------------------------
# Find Student
# ------------------------------------------
def find_student(student_id, students):

    for student in students:

        if student["student_id"] == student_id:
            return student

    return None


# ------------------------------------------
# Calculate Grade
# ------------------------------------------
def calculate_grade(total):

    if total >= 90:
        return "O"

    elif total >= 80:
        return "A+"

    elif total >= 70:
        return "A"

    elif total >= 60:
        return "B+"

    elif total >= 50:
        return "B"

    elif total >= 40:
        return "C"

    else:
        return "F"


# ------------------------------------------
# Calculate Grade Points
# ------------------------------------------
def calculate_grade_points(grade):

    points = {

        "O": 10,
        "A+": 9,
        "A": 8,
        "B+": 7,
        "B": 6,
        "C": 5,
        "F": 0
    }

    return points[grade]


# ------------------------------------------
# Evaluate Student Performance
# ------------------------------------------
def evaluate_student():

    students = load_students()

    if len(students) == 0:

        print("No student records found.")
        return

    student_id = input("\nEnter Student ID : ")

    student = find_student(student_id, students)

    if student is None:

        print("Student not found.")
        return

    # Check if courses enrolled
    if len(student["courses"]) == 0:

        print("Student has not enrolled in any courses.")
        return

    print("\n===================================")
    print(" GRADE EVALUATION SYSTEM")
    print("===================================")

    print(f"Student Name : {student['name']}")
    print(f"Department   : {student['department']}")

    # Create grades dictionary if absent
    if "grades" not in student:

        student["grades"] = {}

    total_grade_points = 0
    total_subjects = 0

    # Evaluate each course
    for course in student["courses"]:

        print(f"\nCourse : {course}")

        internal = float(input("Internal Marks (30): "))
        assignment = float(input("Assignment Marks (20): "))
        final_exam = float(input("Final Exam Marks (50): "))

        total = internal + assignment + final_exam

        grade = calculate_grade(total)

        grade_points = calculate_grade_points(grade)

        # Save course grade details
        student["grades"][course] = {

            "internal": internal,
            "assignment": assignment,
            "final_exam": final_exam,
            "total": total,
            "grade": grade,
            "grade_points": grade_points
        }

        total_grade_points += grade_points
        total_subjects += 1

        print("-----------------------------------")
        print(f"Total Marks : {total}")
        print(f"Grade       : {grade}")
        print(f"Grade Point : {grade_points}")

        # Smart Performance Analysis
        if total >= 90:

            print("Performance : Outstanding")

        elif total >= 75:

            print("Performance : Excellent")

        elif total >= 60:

            print("Performance : Good")

        elif total >= 40:

            print("Performance : Average")

        else:

            print("Performance : Needs Improvement")

    # GPA Calculation
    gpa = total_grade_points / total_subjects

    student["cgpa"] = round(gpa, 2)

    print("\n===================================")
    print(" SEMESTER RESULT SUMMARY")
    print("===================================")

    print(f"Student ID : {student['student_id']}")
    print(f"Student    : {student['name']}")
    print(f"GPA        : {round(gpa, 2)}")

    # AI-like Academic Suggestion
    if gpa >= 9:

        print("Academic Status : Dean's List Candidate")

    elif gpa < 5:

        print("Academic Status : At Academic Risk")

    else:

        print("Academic Status : Good Standing")

    print("===================================")

    # Save updated data
    save_students(students)


# ------------------------------------------
# View Student Result
# ------------------------------------------
def view_result():

    students = load_students()

    student_id = input("\nEnter Student ID : ")

    student = find_student(student_id, students)

    if student is None:

        print("Student not found.")
        return

    if "grades" not in student:

        print("No grades available.")
        return

    print("\n===================================")
    print(" STUDENT RESULT REPORT")
    print("===================================")

    print(f"Student ID : {student['student_id']}")
    print(f"Name       : {student['name']}")
    print(f"Department : {student['department']}")
    print(f"CGPA       : {student['cgpa']}")

    print("\n---------- SUBJECT RESULTS ----------")

    for course, details in student["grades"].items():

        print(f"\nCourse       : {course}")
        print(f"Total Marks  : {details['total']}")
        print(f"Grade        : {details['grade']}")
        print(f"Grade Points : {details['grade_points']}")

    print("\n===================================")


# ------------------------------------------
# Main Menu
# ------------------------------------------
while True:

    print("\n========== GRADE MODULE ==========")
    print("1. Evaluate Student Grades")
    print("2. View Student Result")
    print("3. Exit")

    choice = input("\nEnter your choice : ")

    if choice == "1":

        evaluate_student()

    elif choice == "2":

        view_result()

    elif choice == "3":

        print("Exiting Grade Module...")
        break

    else:

        print("Invalid choice.")