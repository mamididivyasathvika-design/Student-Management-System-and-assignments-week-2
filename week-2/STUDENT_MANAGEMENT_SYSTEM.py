import csv
import os

FILE_NAME = "students.csv"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Roll Number", "Name", "Marks"])

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, marks])
    print("Student added successfully!")

def view_students():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"{row[0]} | {row[1]} | {row[2]}")

def search_student():
    roll = input("Enter Roll Number to search: ")
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if row[0] == roll:
                print(f"Found: Name: {row[1]}, Marks: {row[2]}")
                return
    print("Student not found.")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    rows = []
    found = False
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] == roll:
                found = True
                continue
            writer.writerow(row)
            
    if found:
        print("Student deleted successfully!")
    else:
        print("Student not found.")

def main():
    initialize_file()
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student\n2. View All\n3. Search\n4. Delete\n5. Exit")
        choice = input("Select an option: ")
        if choice == '1': 
            add_student()
        elif choice == '2': 
            view_students()
        elif choice == '3': 
            search_student()
        elif choice == '4': 
            delete_student()
        elif choice == '5': 
            break
        else: 
            print("Invalid choice!")

if __name__ == "__main__":
    main()