# ==========================================
# FEE MANAGEMENT MODULE
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
# Calculate Tuition Fee
# ------------------------------------------
def calculate_tuition_fee(student):

    base_fee = 50000

    # Course based fee increase
    course_count = len(student["courses"])

    course_fee = course_count * 2500

    return base_fee + course_fee


# ------------------------------------------
# Scholarship Calculation
# ------------------------------------------
def calculate_scholarship(student):

    cgpa = student.get("cgpa", 0)

    if cgpa >= 9:

        return 0.50     # 50%

    elif cgpa >= 8:

        return 0.25     # 25%

    elif cgpa >= 7:

        return 0.10     # 10%

    else:

        return 0


# ------------------------------------------
# Attendance Fine
# ------------------------------------------
def attendance_fine(student):

    attendance = student.get("attendance", 100)

    if attendance < 75:

        return 2000

    return 0


# ------------------------------------------
# Generate Fee Receipt
# ------------------------------------------
def generate_receipt(student, fee_data):

    os.makedirs("reports", exist_ok=True)

    filename = f"reports/{student['student_id']}_fee_receipt.txt"

    with open(filename, "w") as file:

        file.write("=====================================\n")
        file.write(" SMART CAMPUS FEE RECEIPT\n")
        file.write("=====================================\n\n")

        file.write(f"Student ID : {student['student_id']}\n")
        file.write(f"Name       : {student['name']}\n")
        file.write(f"Department : {student['department']}\n\n")

        file.write(f"Tuition Fee     : Rs {fee_data['tuition_fee']}\n")
        file.write(f"Scholarship     : Rs {fee_data['scholarship_amount']}\n")
        file.write(f"Attendance Fine : Rs {fee_data['fine']}\n")
        file.write(f"Total Payable   : Rs {fee_data['final_fee']}\n\n")

        file.write(
            f"Generated On : {datetime.now()}\n"
        )

        file.write("\n=====================================")

    print(f"\nReceipt Generated : {filename}")


# ------------------------------------------
# Process Fee Payment
# ------------------------------------------
def process_fee_payment():

    students = load_students()

    if len(students) == 0:

        print("No students found.")
        return

    student_id = input("\nEnter Student ID : ")

    student = find_student(student_id, students)

    if student is None:

        print("Student not found.")
        return

    print("\n===================================")
    print(" FEE CALCULATION SYSTEM")
    print("===================================")

    print(f"Student Name : {student['name']}")
    print(f"Department   : {student['department']}")
    print(f"CGPA         : {student['cgpa']}")

    # Tuition Fee
    tuition_fee = calculate_tuition_fee(student)

    # Scholarship
    scholarship_percent = calculate_scholarship(student)

    scholarship_amount = tuition_fee * scholarship_percent

    # Fine
    fine = attendance_fine(student)

    # Final Fee
    final_fee = tuition_fee - scholarship_amount + fine

    print("\n---------- FEE BREAKDOWN ----------")

    print(f"Base Tuition Fee : Rs {tuition_fee}")
    print(f"Scholarship      : Rs {scholarship_amount}")
    print(f"Attendance Fine  : Rs {fine}")
    print(f"Final Payable    : Rs {final_fee}")

    # Smart Fee Status
    if scholarship_percent >= 0.50:

        print("Scholarship Status : Merit Scholarship")

    elif scholarship_percent > 0:

        print("Scholarship Status : Academic Scholarship")

    else:

        print("Scholarship Status : Not Eligible")

    # Payment Confirmation
    confirm = input("\nProceed with payment? (yes/no): ")

    if confirm.lower() == "yes":

        # Create fee dictionary if absent
        if "fee_details" not in student:

            student["fee_details"] = {}

        student["fee_details"] = {

            "tuition_fee": tuition_fee,
            "scholarship_amount": scholarship_amount,
            "fine": fine,
            "final_fee": final_fee,
            "payment_status": "PAID",
            "payment_date": str(datetime.now())
        }

        student["fees_paid"] = True

        save_students(students)

        generate_receipt(
            student,
            student["fee_details"]
        )

        print("\n===================================")
        print(" PAYMENT SUCCESSFUL")
        print("===================================")

    else:

        print("\nPayment Cancelled.")


# ------------------------------------------
# View Fee Details
# ------------------------------------------
def view_fee_details():

    students = load_students()

    student_id = input("\nEnter Student ID : ")

    student = find_student(student_id, students)

    if student is None:

        print("Student not found.")
        return

    if "fee_details" not in student:

        print("No fee records available.")
        return

    fee = student["fee_details"]

    print("\n===================================")
    print(" STUDENT FEE DETAILS")
    print("===================================")

    print(f"Student ID     : {student['student_id']}")
    print(f"Student Name   : {student['name']}")
    print(f"Department     : {student['department']}")

    print("\n---------- PAYMENT INFO ----------")

    print(f"Tuition Fee    : Rs {fee['tuition_fee']}")
    print(f"Scholarship    : Rs {fee['scholarship_amount']}")
    print(f"Fine           : Rs {fee['fine']}")
    print(f"Final Amount   : Rs {fee['final_fee']}")
    print(f"Payment Status : {fee['payment_status']}")
    print(f"Payment Date   : {fee['payment_date']}")

    print("===================================")


# ------------------------------------------
# Main Menu
# ------------------------------------------
while True:

    print("\n========== FEE MANAGEMENT ==========")
    print("1. Process Fee Payment")
    print("2. View Fee Details")
    print("3. Exit")

    choice = input("\nEnter your choice : ")

    if choice == "1":

        process_fee_payment()

    elif choice == "2":

        view_fee_details()

    elif choice == "3":

        print("Exiting Fee Module...")
        break

    else:

        print("Invalid choice.")