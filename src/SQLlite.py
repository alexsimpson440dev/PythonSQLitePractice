__author__ = 'Alex'
import sqlite3
class SQL():
    def __init__(self):
        self.sqlite_file = 'F:\School\MCTC\Classes\Final Semester\Capstone\Week3 - SQLite\my_db.sqlite'

    def get_connection(self):
        self.conn = sqlite3.connect(self.sqlite_file)
        self.c = self.conn.cursor()

