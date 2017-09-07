__author__ = 'Alex'
from src.SQLlite import SQL
def main():
    database = SQL
    database.__init__(database)
    database.get_connection(database)
    database.add_new_table(database)
    database.close_connection(database)

if __name__ == '__main__':
    main()