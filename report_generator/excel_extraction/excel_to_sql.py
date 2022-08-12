"""Application to open and extract data from version of amphibian dataset in excel.

CLI interface takes file path argument and extracts data. Then cleans dataset then
passes the data to api.

This tool accepts comma separated value files (.csv) as well as Excel files
(.xlsx, xls).

This script requires that 'pandas' be installed within the Python environment
that this is running on.
"""


import datetime
import sqlite3
import sys
from sqlite3 import Error

import pandas
import tables
from clean_data import clean_data
from data_structure import structure_data


def export_to_database(
    path_to_excel: str,
    db_output_name: str = None,
) -> None:
    """Export data from dataset to database.

    Takes a path to excel file, opens it, processes it, creates a sqlite db,
    creates tables, populates database

    Args:
        path_to_excel(str): file path string
        db_output_name(str): db file name
    """
    pandas.options.mode.chained_assignment = None
    if db_output_name is None:
        dtstr = datetime.datetime.now().strftime("%m-%d-%Y_%H:%M:%S")
        db_output_name = f"databases/dataset_{dtstr}.db"
    # Open excel
    data_frame = None
    try:
        # Create and clean data
        data_frame = create_data_frame(path_to_excel)
        clean_data_frame = clean_data(data_frame)

        # with open("min.txt", "w") as file:
        #     file.write("\n".join(clean_data_frame["ElevationMin"].unique().tolist()))

        # Create the database/database connection
        conn = create_connection(db_output_name)

        # Creates tables/Makes sure tables are created
        create_tables(conn)

        # Structures data from dataframe to match tables layout
        structured_data = structure_data(clean_data_frame)
        # Populate tables
        populate_tables(structured_data, conn)

    except FileNotFoundError as e:
        print(e)


def create_connection(db_output_name: str) -> object:
    """Create database connection object.

    If database does not exist it will create the database.

    Args:
        db_output_name(str): Name of db to connect to or create

    Returns:
        conn(object): SQLite3 connection object
    """
    conn = None

    try:
        conn = sqlite3.connect(db_output_name)
    except Error as e:
        print(e)

    return conn


def create_tables(conn: object) -> None:
    """Create tables in database.

    Gets sql string to pass to cursor to create tables for database

    Args:
        conn(object): sqlite3 connection object
    """
    tables_list = tables.get_tables_sql()

    try:
        cursor = conn.cursor()
        for table in tables_list:
            # print(table)
            cursor.execute(table)
            # print("Tables Created")
        cursor.close()
    except Error as e:
        print(e)


def populate_tables(structured_data: object, conn: object) -> None:
    """Populate database with data from structured_data.

    Takes structured data and sqlite3 connector object loops through
    structured_data obj and passes values to the populate_table method

    Args:
        structured_data(obj): object made up of Panda's DataFrame objects
        conn(obj): sqlite3 connector object
    """
    for table_name, table_data in structured_data.items():
        print(f"Populating {table_name}")
        populate_table(table_name, table_data, conn)


def populate_table(table_name: str, table_data: object, conn: object) -> None:
    """Populate database tables with data.

    Takes args and calls Pandas.DataFrame.to_sql Method

    Args:
        table_name(str) - name of table for data to be passed to
        table_data(object) - Panda's DataFrame object containing data to go in table
        conn(object) - sqlite3 connection object
    """
    if table_name == "species":
        table_data["elevation_min"] = pandas.to_numeric(table_data["elevation_min"])
        print(table_data["elevation_min"])

    table_data.to_sql(table_name, conn, index=False, if_exists="append")


def create_data_frame(path_to_dataset: str):
    """Create datafrane from dataset.

    Loads excel file and returns Pandas DataFrame obj

    Args:
        path_to_data_set(str): file path string

    Returns:
        data_frame(object): Pandas DataFrame object
    """
    data_frame = None
    try:
        data_frame = pandas.read_excel(path_to_dataset)

    except FileNotFoundError as e:
        print("Failed to open excel file")
        print(e)

    return data_frame


def main(path_to_file: str) -> None:
    """Run main method.

    Main function for excel to sql

    Args:
        path_to_file(str): File path string.
    """
    export_to_database(path_to_file)


if __name__ == "__main__":

    args = sys.argv

    path_to_file = ""

    if len(args) < 2:
        path_to_file = "example/output_3.xlsx"
    else:
        path_to_file = args[1]

    main(path_to_file)
