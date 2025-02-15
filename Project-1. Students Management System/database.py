
import mysql.connector

def database_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mysql@096411",
        database="student_records"
    )


# this is the database connectivity file as the root database from my machine
