# ==========================================
# ANALYTICS DASHBOARD MODULE
# Smart Campus Information System
# ==========================================

import json
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------
# Load Student Data
# ------------------------------------------
def load_students():

    if not os.path.exists("data/students.json"):

        print("Student database not found.")
        return []

    with open("data/students.json", "r") as file:

        return json.load(file)


# ------------------------------------------
# Convert JSON Data to DataFrame
# ------------------------------------------
def create_dataframe():

    students = load_students()

    if len(students) == 0:

        return None

    df = pd.DataFrame(students)

    return df


# ------------------------------------------
# Display Overall Statistics
# ------------------------------------------
def overall_statistics():

    df = create_dataframe()

    if df is None:

        return

    print("\n===================================")
    print(" OVERALL ANALYTICS STATISTICS")
    print("===================================")

    print(f"Total Students       : {len(df)}")

    print(
        f"Average CGPA         : "
        f"{round(df['cgpa'].mean(), 2)}"
    )

    print(
        f"Highest CGPA         : "
        f"{df['cgpa'].max()}"
    )

    print(
        f"Average Attendance   : "
        f"{round(df['attendance'].mean(), 2)}%"
    )

    paid_students = df["fees_paid"].sum()

    print(f"Fees Paid Students   : {paid_students}")

    print("===================================")


# ------------------------------------------
# Department-wise CGPA Analysis
# ------------------------------------------
def department_cgpa_analysis():

    df = create_dataframe()

    if df is None:

        return

    dept_analysis = df.groupby(
        "department"
    )["cgpa"].mean()

    print("\n========== DEPARTMENT CGPA ==========\n")

    print(dept_analysis)

    # Graph
    plt.figure(figsize=(8, 5))

    plt.bar(
        dept_analysis.index,
        dept_analysis.values
    )

    plt.xlabel("Department")
    plt.ylabel("Average CGPA")

    plt.title("Department-wise CGPA Analysis")

    plt.grid(True)

    plt.show()


# ------------------------------------------
# Attendance vs CGPA Analysis
# ------------------------------------------
def attendance_vs_cgpa():

    df = create_dataframe()

    if df is None:

        return

    print("\nGenerating Attendance vs CGPA Graph...")

    plt.figure(figsize=(8, 5))

    plt.scatter(
        df["attendance"],
        df["cgpa"]
    )

    plt.xlabel("Attendance Percentage")
    plt.ylabel("CGPA")

    plt.title("Attendance vs CGPA")

    plt.grid(True)

    plt.show()


# ------------------------------------------
# Fee Payment Analysis
# ------------------------------------------
def fee_analysis():

    df = create_dataframe()

    if df is None:

        return

    paid = len(df[df["fees_paid"] == True])

    unpaid = len(df[df["fees_paid"] == False])

    print("\n========== FEE ANALYSIS ==========\n")

    print(f"Paid Students   : {paid}")
    print(f"Unpaid Students : {unpaid}")

    plt.figure(figsize=(6, 6))

    plt.pie(

        [paid, unpaid],

        labels=["Paid", "Unpaid"],

        autopct="%1.1f%%"
    )

    plt.title("Fee Payment Analysis")

    plt.show()


# ------------------------------------------
# Top Performing Students
# ------------------------------------------
def top_performers():

    df = create_dataframe()

    if df is None:

        return

    top_students = df.sort_values(

        by="cgpa",

        ascending=False

    ).head(5)

    print("\n========== TOP PERFORMERS ==========\n")

    print(

        top_students[
            [
                "student_id",
                "name",
                "department",
                "cgpa"
            ]
        ]
    )


# ------------------------------------------
# Attendance Defaulter Analysis
# ------------------------------------------
def attendance_defaulters():

    df = create_dataframe()

    if df is None:

        return

    defaulters = df[df["attendance"] < 75]

    print("\n========== ATTENDANCE DEFAULTERS ==========\n")

    if len(defaulters) == 0:

        print("No defaulters found.")

    else:

        print(

            defaulters[
                [
                    "student_id",
                    "name",
                    "attendance",
                    "cgpa"
                ]
            ]
        )


# ------------------------------------------
# Skill Distribution Analysis
# ------------------------------------------
def skill_distribution():

    students = load_students()

    skill_count = {}

    for student in students:

        skills = student.get("skills", [])

        for skill in skills:

            skill = skill.strip().lower()

            if skill in skill_count:

                skill_count[skill] += 1

            else:

                skill_count[skill] = 1

    print("\n========== SKILL DISTRIBUTION ==========\n")

    for skill, count in skill_count.items():

        print(f"{skill} : {count}")

    # Graph
    plt.figure(figsize=(8, 5))

    plt.bar(
        skill_count.keys(),
        skill_count.values()
    )

    plt.xlabel("Skills")
    plt.ylabel("Students")

    plt.title("Skill Distribution Analysis")

    plt.xticks(rotation=45)

    plt.grid(True)

    plt.show()


# ------------------------------------------
# Academic Risk Analysis
# ------------------------------------------
def academic_risk_analysis():

    df = create_dataframe()

    if df is None:

        return

    risk_students = df[
        (df["cgpa"] < 5)
        &
        (df["attendance"] < 75)
    ]

    print("\n========== ACADEMIC RISK ANALYSIS ==========\n")

    if len(risk_students) == 0:

        print("No high-risk students found.")

    else:

        print(

            risk_students[
                [
                    "student_id",
                    "name",
                    "cgpa",
                    "attendance"
                ]
            ]
        )


# ------------------------------------------
# Generate Analytics Report
# ------------------------------------------
def generate_analytics_report():

    df = create_dataframe()

    if df is None:

        return

    os.makedirs("reports", exist_ok=True)

    filename = "reports/analytics_report.txt"

    with open(filename, "w") as report:

        report.write("=====================================\n")
        report.write(" SMART CAMPUS ANALYTICS REPORT\n")
        report.write("=====================================\n\n")

        report.write(
            f"Total Students : {len(df)}\n"
        )

        report.write(
            f"Average CGPA : "
            f"{round(df['cgpa'].mean(), 2)}\n"
        )

        report.write(
            f"Average Attendance : "
            f"{round(df['attendance'].mean(), 2)}%\n"
        )

        report.write(
            f"Highest CGPA : "
            f"{df['cgpa'].max()}\n"
        )

    print(
        f"\nAnalytics Report Generated : {filename}"
    )


# ------------------------------------------
# Main Menu
# ------------------------------------------
while True:

    print("\n========== ANALYTICS DASHBOARD ==========")

    print("1. Overall Statistics")
    print("2. Department-wise CGPA Analysis")
    print("3. Attendance vs CGPA")
    print("4. Fee Payment Analysis")
    print("5. Top Performers")
    print("6. Attendance Defaulters")
    print("7. Skill Distribution")
    print("8. Academic Risk Analysis")
    print("9. Generate Analytics Report")
    print("10. Exit")

    choice = input("\nEnter your choice : ")

    if choice == "1":

        overall_statistics()

    elif choice == "2":

        department_cgpa_analysis()

    elif choice == "3":

        attendance_vs_cgpa()

    elif choice == "4":

        fee_analysis()

    elif choice == "5":

        top_performers()

    elif choice == "6":

        attendance_defaulters()

    elif choice == "7":

        skill_distribution()

    elif choice == "8":

        academic_risk_analysis()

    elif choice == "9":

        generate_analytics_report()

    elif choice == "10":

        print("Exiting Analytics Dashboard...")
        break

    else:

        print("Invalid choice.")