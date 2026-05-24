# ==========================================
# AI RECOMMENDATION SYSTEM
# Smart Campus Information System
# ==========================================

import json
import os

# ------------------------------------------
# Load Student Database
# ------------------------------------------
def load_students():

    if not os.path.exists("data/students.json"):

        print("Student database not found.")
        return []

    with open("data/students.json", "r") as file:

        return json.load(file)


# ------------------------------------------
# Save Student Database
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
# Academic Performance Prediction
# ------------------------------------------
def predict_performance(student):

    cgpa = student["cgpa"]

    attendance = student["attendance"]

    if cgpa >= 8.5 and attendance >= 85:

        return "EXCELLENT"

    elif cgpa >= 6.5 and attendance >= 75:

        return "GOOD"

    elif cgpa >= 5:

        return "AVERAGE"

    else:

        return "HIGH RISK"


# ------------------------------------------
# Research Domain Recommendation
# ------------------------------------------
def recommend_research_domain(student):

    skills = [
        skill.lower().strip()
        for skill in student.get("skills", [])
    ]

    # Biotechnology + AI Logic

    if (
        "python" in skills
        and
        "biology" in skills
    ):

        return "Bioinformatics"

    elif (
        "machine learning" in skills
        and
        "statistics" in skills
    ):

        return "Computational Biology"

    elif (
        "genetics" in skills
        and
        "data analysis" in skills
    ):

        return "Genomic Data Science"

    elif (
        "microbiology" in skills
        and
        "chemistry" in skills
    ):

        return "Industrial Biotechnology"

    elif (
        "ai" in skills
        and
        "healthcare" in skills
    ):

        return "Healthcare AI Systems"

    else:

        return "General Biotechnology"


# ------------------------------------------
# Scholarship Eligibility Prediction
# ------------------------------------------
def scholarship_prediction(student):

    cgpa = student["cgpa"]

    attendance = student["attendance"]

    if cgpa >= 9 and attendance >= 90:

        return "Eligible for 50% Scholarship"

    elif cgpa >= 8 and attendance >= 85:

        return "Eligible for 25% Scholarship"

    else:

        return "Not Eligible"


# ------------------------------------------
# Placement Readiness Analysis
# ------------------------------------------
def placement_readiness(student):

    skills = [
        skill.lower().strip()
        for skill in student.get("skills", [])
    ]

    cgpa = student["cgpa"]

    if (
        cgpa >= 8
        and
        "python" in skills
        and
        "communication" in skills
    ):

        return "PLACEMENT READY"

    elif cgpa >= 6:

        return "NEEDS SKILL IMPROVEMENT"

    else:

        return "HIGH TRAINING REQUIRED"


# ------------------------------------------
# AI Complete Analysis
# ------------------------------------------
def ai_complete_analysis():

    students = load_students()

    student_id = input("\nEnter Student ID : ")

    student = find_student(student_id, students)

    if student is None:

        print("Student not found.")
        return

    print("\n===================================")
    print(" AI STUDENT ANALYSIS REPORT")
    print("===================================")

    print(f"Student ID : {student['student_id']}")
    print(f"Name       : {student['name']}")
    print(f"Department : {student['department']}")

    # AI Predictions
    performance = predict_performance(student)

    domain = recommend_research_domain(student)

    scholarship = scholarship_prediction(student)

    placement = placement_readiness(student)

    print("\n---------- AI ANALYSIS ----------")

    print(f"Performance Status     : {performance}")

    print(f"Recommended Domain     : {domain}")

    print(f"Scholarship Prediction : {scholarship}")

    print(f"Placement Readiness    : {placement}")

    # Risk Alert
    if performance == "HIGH RISK":

        print("\n[ALERT] Academic Risk Detected")

    print("===================================")

    # Save AI Results
    student["ai_analysis"] = {

        "performance": performance,

        "recommended_domain": domain,

        "scholarship": scholarship,

        "placement_status": placement
    }

    save_students(students)


# ------------------------------------------
# Department AI Insights
# ------------------------------------------
def department_ai_insights():

    students = load_students()

    print("\n========== AI DEPARTMENT INSIGHTS ==========\n")

    excellent = 0
    risk = 0

    for student in students:

        result = predict_performance(student)

        if result == "EXCELLENT":

            excellent += 1

        elif result == "HIGH RISK":

            risk += 1

    print(f"Excellent Students : {excellent}")

    print(f"High Risk Students : {risk}")

    print(f"Total Students     : {len(students)}")


# ------------------------------------------
# AI Skill Recommendation
# ------------------------------------------
def skill_recommendation():

    students = load_students()

    student_id = input("\nEnter Student ID : ")

    student = find_student(student_id, students)

    if student is None:

        print("Student not found.")
        return

    skills = [
        skill.lower().strip()
        for skill in student.get("skills", [])
    ]

    print("\n========== AI SKILL RECOMMENDATION ==========\n")

    if "python" not in skills:

        print("Recommended Skill : Python")

    elif "data analysis" not in skills:

        print("Recommended Skill : Data Analysis")

    elif "machine learning" not in skills:

        print("Recommended Skill : Machine Learning")

    elif "communication" not in skills:

        print("Recommended Skill : Communication")

    else:

        print("Skill Profile Excellent")


# ------------------------------------------
# Generate AI Report
# ------------------------------------------
def generate_ai_report():

    students = load_students()

    os.makedirs("reports", exist_ok=True)

    filename = "reports/ai_analysis_report.txt"

    with open(filename, "w") as report:

        report.write("=====================================\n")
        report.write(" AI ANALYSIS REPORT\n")
        report.write("=====================================\n\n")

        for student in students:

            performance = predict_performance(student)

            domain = recommend_research_domain(student)

            report.write(
                f"Student ID : {student['student_id']}\n"
            )

            report.write(
                f"Name       : {student['name']}\n"
            )

            report.write(
                f"Performance: {performance}\n"
            )

            report.write(
                f"Domain     : {domain}\n"
            )

            report.write(
                "\n-----------------------------\n"
            )

    print(f"\nAI Report Generated : {filename}")


# ------------------------------------------
# Main Menu
# ------------------------------------------
while True:

    print("\n========== AI RECOMMENDATION SYSTEM ==========")

    print("1. AI Complete Student Analysis")
    print("2. Department AI Insights")
    print("3. AI Skill Recommendation")
    print("4. Generate AI Report")
    print("5. Exit")

    choice = input("\nEnter your choice : ")

    if choice == "1":

        ai_complete_analysis()

    elif choice == "2":

        department_ai_insights()

    elif choice == "3":

        skill_recommendation()

    elif choice == "4":

        generate_ai_report()

    elif choice == "5":

        print("\nExiting AI Recommendation System...")
        break

    else:

        print("Invalid choice.")