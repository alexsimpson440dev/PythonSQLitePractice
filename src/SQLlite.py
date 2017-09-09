__author__ = 'Alex'
import sqlite3
class SQL():
    def __init__(self):
        self.sqlite_file = 'F:\School\MCTC\Classes\Final Semester\Capstone\Week3 - SQLite\my_db.sqlite'
        # self.sqlite_file = 'C:\School\MCTC\Final Semester\Capstone\Week3 - SQLite\PythonSQLitePractice\my_db.sqlite'
        try:
            self.conn = sqlite3.connect(self.sqlite_file)
            self.c = self.conn.cursor()
        except sqlite3.OperationalError:
            print('Connection Error! Cannot Connect to Database!')
        # Table(s)
        self.employees_table = "Employees"
        # Employees table fields
        self.employeeID_field = "EmployeeID"; self.INTEGER = 'INTEGER'
        self.employeename_field = "EmployeeName"; self.TEXT = "TEXT"
        self.employeehire_field = "Hire Date" #uses type2
        self.employeejob = "Job Description" #uses type2
        self.uniqueindex = "Unique Index"

    # connects to database
    def get_connection(self):
        print('Connection Opened')

    # adds new table
    def add_new_table(self):
        try:
            self.c.execute('CREATE TABLE {tn} ({nc} {nf})'.format(tn=self.employees_table, nc=self.employeeID_field, nf=self.INTEGER))
            print('Table ', self.employees_table, 'created.')
        except AttributeError:
            print('No Attribute for "c"!')
        except sqlite3.OperationalError:
            print('Table already exists')

    # adds new column to table
    def add_new_column(self):
        try:
            self.c.execute('ALTER TABLE {tn} ADD COLUMN {nc} {nf}'.format(tn=self.employees_table, nc=self.employeename_field, nf=self.TEXT))
            print('Added New Column: ' + self.employeename_field + ' to Table: ' + self.employees_table)
        except sqlite3.OperationalError:
            print('Column already exists!')
    # inserts data into table
    def insert_date(self):
        try:
            self.c.execute("INSERT INTO {tn} ({c1}, {c2}) VALUES (1, 'Alexander Simpson')"\
                        .format(tn=self.employees_table, c1=self.employeeID_field, c2=self.employeename_field))
            print("Inserted new data to Table: "+self.employees_table+"!")
        except sqlite3.IntegrityError:
            print('Error! EmployeeID already exists in Primary Key Column!', self.employeeID_field)

    # updates data in table
    def update_data(self):
        self.c.execute("UPDATE {tn} SET {cn1} = 'Alex Simpson' WHERE {cn2} = 1"\
                       .format(tn=self.employees_table, cn1=self.employeename_field, cn2=self.employeeID_field))
        print("Table "+self.employees_table+" updated!")

    # Creating an unique index
    def add_unique_index(self):
        self.c.execute('CREATE INDEX {ix} on {tn}({cn})'\
                .format(ix=self.uniqueindex, tn=self.employees_table, cn=self.employeename_field))
        print('unique index added')

    def drop_unique(self):
        # Dropping the unique index
        # E.g., to avoid future conflicts with update/insert functions
        self.c.execute('DROP INDEX {ix}'.format(ix=self.uniqueindex))
        print('unique index dropped!')

    def close_connection(self):
        try:
            self.conn.commit()
            self.conn.close()
            print('Connection Closed')
        except AttributeError:
            print('No Attribute for "conn"!')