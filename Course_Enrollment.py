# =========================================
# COURSE ENROLLMENT MODULE
# Smart Campus Information System
# =========================================

import json
import os

# -----------------------------------------
# Available Courses Database
# -----------------------------------------
courses = {

    "BT201": {
        "name": "Bioinformatics",
        "credits": 4,
        "faculty": "Dr. Meera",
        "prerequisite": None
    },

    "BT202": {
        "name": "Genetics",
        "credits": 3,
        "faculty": "Dr. Arjun",
        "prerequisite": None
    },

    "CS301": {
        "name": "Python Programming",
        "credits": 4,
        "faculty": "Dr. Rahul",
        "prerequisite": None
    },

    "AI401": {
        "name": "Artificial Intelligence",
        "credits": 5,
        "faculty": "Dr. Kavya",
        "prerequisite": "CS301"
    }
}

# -----------------------------------------
# Load Student Data
# -----------------------------------------
def load_students():

    if not os.path.exists("data/students.json"):
        print("Student database not found.")
        return []

    with open("data/students.json", "r") as file:
        return json.load(file)


# -----------------------------------------
# Save Student Data
# -----------------------------------------
def save_students(students):

    with open("data/students.json", "w") as file:
        json.dump(students, file, indent=4)


# -----------------------------------------
# Display Available Courses
# -----------------------------------------
def display_courses():

    print("\n========== AVAILABLE COURSES ==========\n")

    for code, details in courses.items():

        print(f"Course Code   : {code}")
        print(f"Course Name   : {details['name']}")
        print(f"Credits       : {details['credits']}")
        print(f"Faculty       : {details['faculty']}")
        print(f"Prerequisite  : {details['prerequisite']}")
        print("----------------------------------------")


# -----------------------------------------
# Find Student
# -----------------------------------------
def find_student(student_id, students):

    for student in students:

        if student["student_id"] == student_id:
            return student

    return None


# -----------------------------------------
# Calculate Total Credits
# -----------------------------------------
def calculate_total_credits(student):

    total = 0

    for course in student["courses"]:

        total += courses[course]["credits"]

    return total


# -----------------------------------------
# Enroll Course
# -----------------------------------------
def enroll_course():

    students = load_students()

    if len(students) == 0:
        print("No students found.")
        return

    student_id = input("\nEnter Student ID : ")

    student = find_student(student_id, students)

    if student is None:
        print("Student not found.")
        return

    print(f"\nStudent Name : {student['name']}")
    print(f"Department   : {student['department']}")

    display_courses()

    course_code = input("\nEnter Course Code to Enroll : ")

    # Check valid course
    if course_code not in courses:
        print("Invalid Course Code.")
        return

    # Check duplicate enrollment
    if course_code in student["courses"]:
        print("Student already enrolled in this course.")
        return

    # Check prerequisite
    prerequisite = courses[course_code]["prerequisite"]

    if prerequisite is not None:

        if prerequisite not in student["courses"]:

            print(f"Prerequisite not completed: {prerequisite}")
            return

    # Credit limit check
    current_credits = calculate_total_credits(student)

    new_course_credits = courses[course_code]["credits"]

    if current_credits + new_course_credits > 20:

        print("Credit limit exceeded.")
        return

    # Enroll course
    student["courses"].append(course_code)

    # AI-like Recommendation
    recommendations = {

        "Bioinformatics": "AI401",
        "Python Programming": "AI401",
        "Genetics": "BT201"
    }

    recommended_course = recommendations.get(
        courses[course_code]["name"]
    )

    print("\n======================================")
    print(" COURSE ENROLLMENT SUCCESSFUL")
    print("======================================")

    print(f"Student ID     : {student['student_id']}")
    print(f"Student Name   : {student['name']}")
    print(f"Enrolled Course: {course_code}")
    print(f"Course Name    : {courses[course_code]['name']}")
    print(f"Faculty        : {courses[course_code]['faculty']}")
    print(f"Credits Added  : {new_course_credits}")

    total_after = calculate_total_credits(student)

    print(f"Total Credits  : {total_after}")

    # Smart recommendation
    if recommended_course is not None:

        print(
            f"Suggested Next Course : {recommended_course}"
        )

    print("======================================")

    # Save updated data
    save_students(students)


# -----------------------------------------
# View Student Courses
# -----------------------------------------
def view_student_courses():

    students = load_students()

    student_id = input("\nEnter Student ID : ")

    student = find_student(student_id, students)

    if student is None:
        print("Student not found.")
        return

    print("\n========== ENROLLED COURSES ==========\n")

    if len(student["courses"]) == 0:
        print("No courses enrolled.")
        return

    total_credits = 0

    for course_code in student["courses"]:

        details = courses[course_code]

        print(f"{course_code} - {details['name']}")
        print(f"Faculty : {details['faculty']}")
        print(f"Credits : {details['credits']}")
        print("----------------------------------")

        total_credits += details["credits"]

    print(f"\nTotal Credits : {total_credits}")


# -----------------------------------------
# Main Menu
# -----------------------------------------
while True:

    print("\n========== COURSE ENROLLMENT MENU ==========")
    print("1. Display Available Courses")
    print("2. Enroll Course")
    print("3. View Student Courses")
    print("4. Exit")

    choice = input("\nEnter your choice : ")

    if choice == "1":
        display_courses()

    elif choice == "2":
        enroll_course()

    elif choice == "3":
        view_student_courses()

    elif choice == "4":
        print("Exiting Course Enrollment Module...")
        break

    else:
        print("Invalid choice.")