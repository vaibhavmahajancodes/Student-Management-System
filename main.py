import json
from pathlib import Path

DATA_FILE = Path("students.json")

def load_students():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_students(students):
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)

def add_student(students):
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    students.append({
        "roll": roll,
        "name": name,
        "marks": marks,
    })
    save_students(students)
    print("Student added successfully!")

def view_students(students):
    if not students:
        print("No records found.")
        return

    print("\n--- Student Records ---")
    for s in students:
        print(f"Roll: {s['roll']} | Name: {s['name']} | Marks: {s['marks']}")

def search_student(students):
    roll = input("Enter Roll No to search: ")
    for s in students:
        if s["roll"] == roll:
            print(s)
            return
    print("Student not found.")

def delete_student(students):
    roll = input("Enter Roll No to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            save_students(students)
            print("Student deleted successfully!")
            return
    print("Student not found.")

def main():
    students = load_students()

    while True:
        print("\\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()
