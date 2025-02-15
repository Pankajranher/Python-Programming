from flask import Flask, render_template, request, redirect, url_for
from database import database_connection

app = Flask(__name__)

# refered from the word notes
@app.route('/')
def home():
    return render_template('Front_page.html')

# Show all students
@app.route('/students')
def students():
    connection = database_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("select * from students")
    student_list = cursor.fetchall()
    connection.close()
    return render_template('student_list.html', students=student_list)

# Add new student
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        roll_number = request.form['roll_number']
        dob = request.form['dob']
        gender = request.form['gender']

        connection = database_connection()
        cursor = connection.cursor()
        cursor.execute(""" insert into students (name, surname, roll_number, dob, gender) values (%s, %s, %s, %s, %s) """, (name, surname, roll_number, dob, gender))
        connection.commit()
        connection.close()
        return redirect(url_for('students'))
    return render_template('add_student.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
