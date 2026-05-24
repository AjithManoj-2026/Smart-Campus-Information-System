# ================================
# SMART CAMPUS INFORMATION SYSTEM
# Student Registration Module
# ================================

import json
import os

students = []

# --------------------------------
# Generate Student ID
# --------------------------------
def generate_student_id(department, count):

    dept_codes = {
        "Biotechnology": "BT",
        "Computer Science": "CS",
        "Electronics": "EC",
        "Mechanical": "ME"
    }

    code = dept_codes.get(department, "GEN")

    year = 2026

    return f"{code}{year}{count:03}"


# --------------------------------
# Validate Phone Number
# --------------------------------
def validate_phone(phone):

    return phone.isdigit() and len(phone) == 10


# --------------------------------
# Validate Email
# --------------------------------
def validate_email(email):

    return "@" in email and "." in email


# --------------------------------
# Generate College Email
# --------------------------------
def generate_college_email(name, department):

    dept_short = department[:2].lower()

    username = name.replace(" ", "").lower()

    return f"{username}.{dept_short}@smartcampus.edu"


# --------------------------------
# Check Duplicate Email
# --------------------------------
def check_duplicate(email):

    for student in students:
        if student["personal_email"] == email:
            return True

    return False


# --------------------------------
# Save Data to JSON File
# --------------------------------
def save_to_file():

    os.makedirs("data", exist_ok=True)

    with open("data/students.json", "w") as file:
        json.dump(students, file, indent=4)

    print("\nData saved successfully.")


# --------------------------------
# Register Student
# --------------------------------
def register_student():

    print("\n========== STUDENT REGISTRATION ==========\n")

    name = input("Enter Student Name : ")

    age = int(input("Enter Age : "))

    gender = input("Enter Gender : ")

    department = input(
        "Enter Department (Biotechnology/Computer Science/Electronics/Mechanical): "
    )

    semester = int(input("Enter Semester : "))

    phone = input("Enter Phone Number : ")

    while not validate_phone(phone):
        print("Invalid Phone Number.")
        phone = input("Re-enter Phone Number : ")

    personal_email = input("Enter Personal Email : ")

    while not validate_email(personal_email):
        print("Invalid Email.")
        personal_email = input("Re-enter Email : ")

    # Duplicate check
    if check_duplicate(personal_email):
        print("\nStudent already registered with this email.")
        return

    blood_group = input("Enter Blood Group : ")

    skills = input("Enter Skills (comma separated) : ").split(",")

    research_interest = input(
        "Enter Research Interest (AI/Bioinformatics/Genetics/etc): "
    )

    # Generate Student ID
    student_id = generate_student_id(department, len(students) + 1)

    # Generate College Email
    college_email = generate_college_email(name, department)

    # Default Password
    password = student_id + "@123"

    # Profile Completion Logic
    profile_completion = 100

    if blood_group == "":
        profile_completion -= 10

    if len(skills) == 0:
        profile_completion -= 10

    # Student Record
    student = {
        "student_id": student_id,
        "name": name,
        "age": age,
        "gender": gender,
        "department": department,
        "semester": semester,
        "phone": phone,
        "personal_email": personal_email,
        "college_email": college_email,
        "blood_group": blood_group,
        "skills": skills,
        "research_interest": research_interest,
        "attendance": 100,
        "cgpa": 0.0,
        "fees_paid": False,
        "courses": [],
        "password": password,
        "profile_completion": profile_completion
    }

    students.append(student)

    print("\n======================================")
    print(" STUDENT REGISTERED SUCCESSFULLY")
    print("======================================")

    print(f"Student ID       : {student_id}")
    print(f"Name             : {name}")
    print(f"Department       : {department}")
    print(f"College Email    : {college_email}")
    print(f"Default Password : {password}")
    print(f"Profile Status   : {profile_completion}% Complete")

    # Smart Recommendation
    if research_interest.lower() == "bioinformatics":
        print("Suggested Club   : Computational Biology Club")

    elif research_interest.lower() == "ai":
        print("Suggested Club   : AI Innovation Club")

    print("======================================")

    save_to_file()


# --------------------------------
# Display All Students
# --------------------------------
def display_students():

    if len(students) == 0:
        print("\nNo students registered.")
        return

    print("\n========== STUDENT DATABASE ==========\n")

    for student in students:

        print(f"ID         : {student['student_id']}")
        print(f"Name       : {student['name']}")
        print(f"Department : {student['department']}")
        print(f"CGPA       : {student['cgpa']}")
        print("-----------------------------------")


# --------------------------------
# Main Menu
# --------------------------------
while True:

    print("\n========== SMART CAMPUS MENU ==========")
    print("1. Register Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
        register_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        print("\nExiting Smart Campus System...")
        break

    else:
        print("Invalid choice.")