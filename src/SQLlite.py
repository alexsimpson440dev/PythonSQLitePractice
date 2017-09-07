__author__ = 'Alex'
import sqlite3
class SQL():
    def __init__(self):
        self.sqlite_file = 'F:\School\MCTC\Classes\Final Semester\Capstone\Week3 - SQLite\my_db.sqlite'
        #Table(s)
        self.employees_table = "Employees"
        #Employees table fields
        self.employeeID_field = "EmployeeID"; self.INTEGER = 'INTEGER'
        self.employeename_field = "EmployeeName"; self.TEXT = "TEXT"
        self.employeehire_field = "Hire Date" #uses type2
        self.employeejob = "Job Description" #uses type2

    def get_connection(self):
        self.conn = sqlite3.connect(self.sqlite_file)
        self.c = self.conn.cursor()

    def add_new_table(self):
        self.c.execute('CREATE TABLE {tn} ({nc} {nf})'.format(tn=self.employees_table, nc = self.employeeID_field, nf=self.INTEGER))

    def close_connection(self):
        self.conn.commit()
        self.conn.close()