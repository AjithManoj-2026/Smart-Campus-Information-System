# ==========================================
# DIRECTORY SCANNING MODULE
# Smart Campus Information System
# ==========================================

import os
import json
from datetime import datetime

# ------------------------------------------
# Required Project Structure
# ------------------------------------------
required_folders = [

    "data",
    "reports",
    "backups"
]

required_files = [

    "data/students.json"
]

# ------------------------------------------
# Create Missing Folder
# ------------------------------------------
def create_missing_folder(folder):

    try:

        os.makedirs(folder, exist_ok=True)

        print(f"[RECOVERED] Folder created : {folder}")

    except Exception as error:

        print(f"[ERROR] Unable to create folder : {error}")


# ------------------------------------------
# Create Empty JSON File
# ------------------------------------------
def create_empty_json(file_path):

    try:

        with open(file_path, "w") as file:

            json.dump([], file, indent=4)

        print(f"[RECOVERED] File created : {file_path}")

    except Exception as error:

        print(f"[ERROR] Unable to create file : {error}")


# ------------------------------------------
# Scan Required Folders
# ------------------------------------------
def scan_folders():

    print("\n========== FOLDER SCAN ==========\n")

    for folder in required_folders:

        try:

            if os.path.exists(folder):

                print(f"[FOUND] Folder : {folder}")

            else:

                print(f"[MISSING] Folder : {folder}")

                create_missing_folder(folder)

        except Exception as error:

            print(f"[ERROR] Folder scan failed : {error}")


# ------------------------------------------
# Scan Required Files
# ------------------------------------------
def scan_files():

    print("\n========== FILE SCAN ==========\n")

    for file_path in required_files:

        try:

            if os.path.exists(file_path):

                print(f"[FOUND] File : {file_path}")

                # Check empty file
                if os.path.getsize(file_path) == 0:

                    print(f"[WARNING] Empty file detected : {file_path}")

            else:

                print(f"[MISSING] File : {file_path}")

                create_empty_json(file_path)

        except Exception as error:

            print(f"[ERROR] File scan failed : {error}")


# ------------------------------------------
# Scan Database Integrity
# ------------------------------------------
def check_json_integrity():

    print("\n========== DATABASE INTEGRITY CHECK ==========\n")

    for file_path in required_files:

        try:

            with open(file_path, "r") as file:

                json.load(file)

            print(f"[HEALTHY] JSON Valid : {file_path}")

        except json.JSONDecodeError:

            print(f"[CORRUPTED] Invalid JSON : {file_path}")

        except FileNotFoundError:

            print(f"[ERROR] File not found : {file_path}")

        except Exception as error:

            print(f"[ERROR] Integrity check failed : {error}")


# ------------------------------------------
# Display Directory Contents
# ------------------------------------------
def display_directory_contents():

    print("\n========== PROJECT DIRECTORY CONTENTS ==========\n")

    try:

        for folder in required_folders:

            print(f"\n--- {folder.upper()} ---")

            if os.path.exists(folder):

                files = os.listdir(folder)

                if len(files) == 0:

                    print("No files found.")

                else:

                    for file in files:

                        print(file)

            else:

                print("Folder missing.")

    except Exception as error:

        print(f"[ERROR] Unable to scan directory : {error}")


# ------------------------------------------
# Generate System Scan Report
# ------------------------------------------
def generate_scan_report():

    try:

        os.makedirs("reports", exist_ok=True)

        report_name = "reports/system_scan_report.txt"

        with open(report_name, "w") as report:

            report.write("=====================================\n")
            report.write(" SMART CAMPUS SYSTEM SCAN REPORT\n")
            report.write("=====================================\n\n")

            report.write(
                f"Generated On : {datetime.now()}\n\n"
            )

            report.write("Required Folders:\n")

            for folder in required_folders:

                status = "FOUND"

                if not os.path.exists(folder):

                    status = "MISSING"

                report.write(f"{folder} : {status}\n")

            report.write("\nRequired Files:\n")

            for file_path in required_files:

                status = "FOUND"

                if not os.path.exists(file_path):

                    status = "MISSING"

                report.write(f"{file_path} : {status}\n")

        print(f"\n[REPORT GENERATED] {report_name}")

    except Exception as error:

        print(f"[ERROR] Report generation failed : {error}")


# ------------------------------------------
# Storage Statistics
# ------------------------------------------
def storage_statistics():

    print("\n========== STORAGE STATISTICS ==========\n")

    total_files = 0
    total_size = 0

    try:

        for folder in required_folders:

            if os.path.exists(folder):

                files = os.listdir(folder)

                total_files += len(files)

                for file in files:

                    path = os.path.join(folder, file)

                    if os.path.isfile(path):

                        total_size += os.path.getsize(path)

        print(f"Total Files : {total_files}")
        print(f"Total Size  : {round(total_size / 1024, 2)} KB")

        # Smart health status
        if total_files >= 5:

            print("System Health : EXCELLENT")

        else:

            print("System Health : GOOD")

    except Exception as error:

        print(f"[ERROR] Statistics generation failed : {error}")


# ------------------------------------------
# Main Menu
# ------------------------------------------
while True:

    print("\n========== DIRECTORY SCANNER ==========")

    print("1. Scan Required Folders")
    print("2. Scan Required Files")
    print("3. Check Database Integrity")
    print("4. Display Directory Contents")
    print("5. Generate System Scan Report")
    print("6. View Storage Statistics")
    print("7. Exit")

    choice = input("\nEnter your choice : ")

    if choice == "1":

        scan_folders()

    elif choice == "2":

        scan_files()

    elif choice == "3":

        check_json_integrity()

    elif choice == "4":

        display_directory_contents()

    elif choice == "5":

        generate_scan_report()

    elif choice == "6":

        storage_statistics()

    elif choice == "7":

        print("\nExiting Directory Scanner...")
        break

    else:

        print("Invalid choice.")