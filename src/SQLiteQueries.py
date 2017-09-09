__author__ = 'Alex'
import sqlite3
class Queries():
    def __init__(self):
        # sets the sqlite file
        self.sqlite_file = 'F:\School\MCTC\Classes\Final Semester\Capstone\Week3 - SQLite\my_db.sqlite'
        # self.sqlite_file = 'C:\School\MCTC\Final Semester\Capstone\Week3 - SQLite\PythonSQLitePractice\my_db.sqlite'

        # variable for connecting to the database
        self.conn = sqlite3.connect(self.sqlite_file)
        self.c = self.conn.cursor()
        self.select_results = self

    # method that calls for a connection to the sqlite file
    def print_connection(self):
        print('Connected to Database')

    def select_all_one_condition(self):
        self.c.execute("SELECT * FROM Employees WHERE EmployeeID=?",(1,))
        self.select_results = self.c.fetchall()
        print('1):', self.select_results)

    def select_column_one_condition(self):
        self.c.execute("SELECT EmployeeName FROM Employees WHERE EmployeeID=?",(1,))
        self.select_results = self.c.fetchall()
        print('2):', self.select_results)

    def close_connection(self):
        # closes Connection
        self.conn.commit()
        self.conn.close()
        print('Database Closed')
