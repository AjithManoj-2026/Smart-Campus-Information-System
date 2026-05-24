# ==========================================
# ATTENDANCE MANAGEMENT MODULE
# Smart Campus Information System
# ==========================================

import json
import os
from datetime import datetime

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
# Initialize Attendance Structure
# ------------------------------------------
def initialize_attendance(student):

    if "attendance_record" not in student:

        student["attendance_record"] = {}


# ------------------------------------------
# Mark Attendance
# ------------------------------------------
def mark_attendance():

    students = load_students()

    if len(students) == 0:

        print("No students found.")
        return

    student_id = input("\nEnter Student ID : ")

    student = find_student(student_id, students)

    if student is None:

        print("Student not found.")
        return

    # Ensure attendance structure exists
    initialize_attendance(student)

    # Check enrolled courses
    if len(student["courses"]) == 0:

        print("Student has not enrolled in courses.")
        return

    print("\n========== ENROLLED COURSES ==========\n")

    for course in student["courses"]:

        print(course)

    course_code = input("\nEnter Course Code : ")

    if course_code not in student["courses"]:

        print("Student not enrolled in this course.")
        return

    # Create course attendance if absent
    if course_code not in student["attendance_record"]:

        student["attendance_record"][course_code] = {

            "present": 0,
            "total_classes": 0,
            "percentage": 0,
            "last_updated": ""
        }

    status = input("Attendance Status (P/A): ")

    # Increase total classes
    student["attendance_record"][course_code]["total_classes"] += 1

    # Mark present
    if status.upper() == "P":

        student["attendance_record"][course_code]["present"] += 1

        print("\nRFID Attendance Marked Successfully")

    else:

        print("\nStudent Marked Absent")

    # Attendance Calculation
    present = student["attendance_record"][course_code]["present"]

    total = student["attendance_record"][course_code]["total_classes"]

    percentage = (present / total) * 100

    student["attendance_record"][course_code]["percentage"] = round(
        percentage,
        2
    )

    student["attendance_record"][course_code][
        "last_updated"
    ] = str(datetime.now())

    # Overall attendance update
    overall_attendance = []

    for data in student["attendance_record"].values():

        overall_attendance.append(data["percentage"])

    student["attendance"] = round(
        sum(overall_attendance) / len(overall_attendance),
        2
    )

    print("\n===================================")
    print(" ATTENDANCE UPDATED")
    print("===================================")

    print(f"Student Name : {student['name']}")
    print(f"Course       : {course_code}")
    print(f"Attendance % : {percentage}")

    # Smart Attendance Analysis
    if percentage >= 90:

        print("Attendance Status : Excellent")

    elif percentage >= 75:

        print("Attendance Status : Good")

    else:

        print("Attendance Status : Shortage Warning")

    # Academic Risk Detection
    cgpa = student.get("cgpa", 0)

    if percentage < 75 and cgpa < 5:

        print("AI Alert : High Academic Risk")

    save_students(students)


# ------------------------------------------
# View Attendance Report
# ------------------------------------------
def view_attendance_report():

    students = load_students()

    student_id = input("\nEnter Student ID : ")

    student = find_student(student_id, students)

    if student is None:

        print("Student not found.")
        return

    if "attendance_record" not in student:

        print("No attendance records available.")
        return

    print("\n===================================")
    print(" STUDENT ATTENDANCE REPORT")
    print("===================================")

    print(f"Student ID : {student['student_id']}")
    print(f"Name       : {student['name']}")
    print(f"Department : {student['department']}")
    print(f"Overall Attendance : {student['attendance']}%")

    print("\n---------- COURSE ATTENDANCE ----------")

    for course, details in student["attendance_record"].items():

        print(f"\nCourse          : {course}")
        print(f"Present         : {details['present']}")
        print(f"Total Classes   : {details['total_classes']}")
        print(f"Attendance %    : {details['percentage']}")
        print(f"Last Updated    : {details['last_updated']}")

    print("\n===================================")


# ------------------------------------------
# Generate Defaulter List
# ------------------------------------------
def generate_defaulter_list():

    students = load_students()

    print("\n===================================")
    print(" ATTENDANCE DEFAULTER LIST")
    print("===================================")

    found = False

    for student in students:

        attendance = student.get("attendance", 100)

        if attendance < 75:

            found = True

            print(f"\nStudent ID : {student['student_id']}")
            print(f"Name       : {student['name']}")
            print(f"Department : {student['department']}")
            print(f"Attendance : {attendance}%")

    if not found:

        print("\nNo attendance defaulters found.")

    print("\n===================================")


# ------------------------------------------
# Main Menu
# ------------------------------------------
while True:

    print("\n========== ATTENDANCE MANAGEMENT ==========")
    print("1. Mark Attendance")
    print("2. View Attendance Report")
    print("3. Generate Defaulter List")
    print("4. Exit")

    choice = input("\nEnter your choice : ")

    if choice == "1":

        mark_attendance()

    elif choice == "2":

        view_attendance_report()

    elif choice == "3":

        generate_defaulter_list()

    elif choice == "4":

        print("Exiting Attendance Module...")
        break

    else:

        print("Invalid choice.")