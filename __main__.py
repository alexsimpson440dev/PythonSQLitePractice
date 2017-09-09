__author__ = 'Alex'
from src.SQLlite import SQL
def main():
    database = SQL
    database.__init__(database)
    database.get_connection(database)
    database.add_new_table(database)
    database.add_new_column(database)
    database.insert_date(database)
    database.update_data(database)
    database.add_unique_index(database)
    database.drop_unique(database)
    database.close_connection(database)

if __name__ == '__main__':
    main()