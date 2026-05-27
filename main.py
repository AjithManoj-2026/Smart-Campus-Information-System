# ==========================================
# MAIN MODULE
# Smart Campus Information System
# ==========================================

import os
import subprocess

# ------------------------------------------
# Main Banner
# ------------------------------------------
def display_banner():

    print("\n==========================================")
    print(" SMART CAMPUS INFORMATION SYSTEM ")
    print("==========================================")

    print("AI-Enhanced Academic ERP Platform")

    print("==========================================\n")


# ------------------------------------------
# Main Menu
# ------------------------------------------
def main_menu():

    while True:

        display_banner()

        print("1. Student Registration Module")
        print("2. Course Enrollment Module")
        print("3. Grade Evaluation Module")
        print("4. Fee Management Module")
        print("5. Attendance Management Module")
        print("6. Search & Sorting Module")
        print("7. Directory Scanning Module")
        print("8. Analytics Dashboard Module")
        print("9. AI Recommendation System")
        print("10. Exit")

        choice = input("\nEnter your choice : ")

        # ----------------------------------
        # Execute Selected Module
        # ----------------------------------

        if choice == "1":
            subprocess.run(['py', r'Student Registration\Student_Registration.py'])
        elif choice == "2":
            subprocess.run(['py', r'Course Enrollment\Course_Enrollment.py'])
        elif choice == "3":
            subprocess.run(['py', r'Grade Evaluation\Grade_Evaluation.py'])
        elif choice == "4":
            subprocess.run(['py', r'Fee Calculation\Fee_Calculation.py'])
        elif choice == "5":
            subprocess.run(['py', r'Attendance Management\Attend_management.py'])
        elif choice == "6":
            subprocess.run(['py', r'Searching and Sorting\searchsort.py'])
        elif choice == "7":
            subprocess.run(['py', r'Directory Scanning\Directory_Scanning.py'])
        elif choice == "8":
            subprocess.run(['py', r'Analytics Dashboard\Analytical.py'])
        elif choice == "9":
            subprocess.run(['py', r'AI Recommendation System\AI_Recommend.py'])
        elif choice == "10":
            print("\nExiting Smart Campus System...")
            print("Thank You.")
            break
        else:
            print("\nInvalid choice. Please try again.")


# ------------------------------------------
# Start Program
# ------------------------------------------
main_menu()