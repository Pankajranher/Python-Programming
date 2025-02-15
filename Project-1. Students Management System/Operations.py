# student_crud.py
from database import database_connection

def add_student(name, surname, roll_number, dob, gender):
    connection = database_connection()
    cursor = connection.cursor()
    cursor.execute(""" INSERT INTO students (name, surname, roll_number, dob, gender) VALUES (%s, %s, %s, %s, %s) """, (name, surname, roll_number, dob, gender))
    connection.commit()
    connection.close()

def fetch_students():
    connection = database_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    for student in cursor.fetchall():
        print(student)
    connection.close()

# For Example
add_student('Pankaj', 'Ranher', '161', '25-04-2002', 'Male')
fetch_students()
