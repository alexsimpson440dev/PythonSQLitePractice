__author__ = 'Alex'
import sqlite3
class Queries():
    def __init__(self):
        # sets the sqlite file
        self.sqlite_file = 'my_db.sqlite'
        # self.sqlite_file = 'C:\School\MCTC\Final Semester\Capstone\Week3 - SQLite\PythonSQLitePractice\my_db.sqlite'

        # variable for connecting to the database
        self.conn = sqlite3.connect(self.sqlite_file)
        self.c = self.conn.cursor()
        self.select_results = self

        # variable for getting table info
        self.info = self

    # method that calls for a connection to the sqlite file
    def print_connection(self):
        print('Connected to Database')

    #selects all columns from a table based off of a condition
    def select_all_one_condition(self):
        self.c.execute("SELECT * FROM Employees WHERE EmployeeID=?",(1,))
        self.select_results = self.c.fetchall()
        print('1):', self.select_results)

    #selects a column based off of one condition
    def select_column_one_condition(self):
        self.c.execute("SELECT EmployeeName FROM Employees WHERE EmployeeID=?", (1,))
        self.select_results = self.c.fetchall()
        print('2):', self.select_results)

    # gets table info
    def get_table_columns(self):
        self.c.execute('PRAGMA TABLE_INFO(Employees)')

        # prints table info
        self.info = [tup[1] for tup in self.c.fetchall()]
        print("Table Columns: ", self.info)

    def get_table_info(self, print_out=True):
        self.c.execute('PRAGMA TABLE_INFO(Employees)')

        # prints table info
        self.info = [tup[1] for tup in self.c.fetchall()]

        col_dict = dict()
        for col in self.info:
            col_dict[col[1]] = 0
        for col in col_dict:
            self.c.execute('SELECT ({0}) from Employees where {0} is not null'.format(col))
            number_rows = len(self.c.fetchall())
            col_dict[col] = number_rows
        if print_out:
            print("\nNumber of entries per column:")
            for i in col_dict.items():
                print('{}: {}'.format(i[0], i[1]))
        return col_dict

    def close_connection(self):
        # closes Connection
        self.conn.commit()
        self.conn.close()
        print('Database Closed')
