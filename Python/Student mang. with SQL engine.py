import sqlite3
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Created Student Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll_no INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    gender TEXT NOT NULL
)
""")
conn.commit()

# Function to Add Student
def add_student(roll_no, name, surname, gender):
    cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (roll_no, name, surname, gender))
    conn.commit()
    print("Student added successfully!\n")

# Function to View All Students
def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    print("\n--- List of Students---")
    for student in students:
        print(f"Roll No: {student[0]}, Name: {student[1]}, Surname: {student[2]}, Gender: {student[3]}")
    print("-------------------\n")

# Function to Update Student
def update_student(roll_no, name, surname, gender):
    cursor.execute("UPDATE students SET name=?, surname=?, gender=? WHERE roll_no=?", (name, surname, gender, roll_no))
    conn.commit()
    print("Student updated successfully!\n")

# Function to Delete Student
def delete_student(roll_no):
    cursor.execute("DELETE FROM students WHERE roll_no=?", (roll_no,))
    conn.commit()
    print("Student deleted successfully!\n")

# Main Menu
def main():
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            roll_no = int(input("Enter Roll No: "))
            name = input("Enter Name: ")
            surname = input("Enter Surname: ")
            gender = input("Enter Gender (M/F): ")
            add_student(roll_no, name, surname, gender)
        elif choice == "2":
            view_students()
        elif choice == "3":
            roll_no = int(input("Enter Roll No to Update: "))
            name = input("Enter New Name: ")
            surname = input("Enter New Surname: ")
            gender = input("Enter New Gender (M/F): ")
            update_student(roll_no, name, surname, gender)
        elif choice == "4":
            roll_no = int(input("Enter Roll No to Delete: "))
            delete_student(roll_no)
        elif choice == "5":
            print("Exiting Program...")
            break
        else:
            print("Invalid Choice! Try again.\n")

if __name__ == "__main__":
    main()
    conn.close()
