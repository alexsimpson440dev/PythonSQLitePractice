__author__ = 'Alex'
from src.SQLlite import SQL
from src.SQLiteQueries import Queries
def main():
    database = SQL
    queries = Queries

    response = input('Do you want to set up database?')

    if response.lower() == 'yes':
        database.__init__(database)
        database.get_connection(database)
        database.add_new_table(database)
        database.add_new_column(database)
        database.insert_date(database)
        database.update_data(database)
        database.add_unique_index(database)
        database.drop_unique(database)
        database.close_connection(database)

    else:
        # select statements
        queries.__init__(queries)
        queries.print_connection(queries)
        queries.select_all_one_condition(queries)
        queries.close_connection(queries)

if __name__ == '__main__':
    main()