# ==========================================
# MAIN MODULE
# Smart Campus Information System
# ==========================================

import os

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

            os.system("python student_registration.py")

        elif choice == "2":

            os.system("python course_enrollment.py")

        elif choice == "3":

            os.system("python grade_evaluation.py")

        elif choice == "4":

            os.system("python fee_management.py")

        elif choice == "5":

            os.system("python attendance_management.py")

        elif choice == "6":

            os.system("python search_sorting.py")

        elif choice == "7":

            os.system("python directory_scanner.py")

        elif choice == "8":

            os.system("python analytics_dashboard.py")

        elif choice == "9":

            os.system("python ai_recommendation.py")

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