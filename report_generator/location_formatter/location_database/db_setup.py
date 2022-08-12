"""Database setup.

Setup file to create a locations SQLITE database and load location information
into the database to allow for queries.

"""

import os
import sqlite3
from sqlite3 import Error

import pandas


def create_connection():
    """Create connection.

    Create a SQLite3 connection object and return it.

    Returns:
        conn: SQLite3 connection object

    """
    conn = None

    try:
        conn = sqlite3.connect("location_database/location.db")
    except Error as e:
        print(e)

    return conn


def create_tables(conn: object) -> None:
    """Create SQL table strings.

    Create SQL table strings for the locations database.

    Use SQLite3 connection object to create tables in locations
    database with table strings.

    Tables:
        country_codes: table representing country data
        geocode: table representing geocode data

    Args:
        conn: SQLite3 connection object

    """
    country_table = """CREATE TABLE IF NOT EXISTS country_codes (
        country_code_id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        continent_name VARCHAR(50) NOT NULL,
        continent_code VARCHAR(4) NOT NULL,
        country_name VARCHAR(50) NOT NULL,
        two_letter_country_code VARCHAR(2),
        three_letter_country_code VARCHAR(3),
        country_number integer NOT NULL
    )
    """

    geocode_table = """CREATE TABLE IF NOT EXISTS geocode (
            geoname_id INT NOT NULL PRIMARY KEY,
            place_name VARCHAR(50),
            ascii_name TEXT,
            alternate_names TEXT,
            latitude REAL,
            longitude REAL,
            feature_class TEXT,
            feature_code TEXT,
            country_code TEXT,
            cc2 TEXT,
            admin1_code TEXT,
            admin2_code TEXT,
            admin3_code TEXT,
            admin4_code TEXT,
            population_info integer,
            elevation integer,
            dem integer,
            timezone TEXT,
            modification TEXT
        )
    """

    try:
        cursor = conn.cursor()
        cursor.execute(country_table)
        cursor.execute(geocode_table)
        print("Tables Created")
    except Error as e:
        print(e)


def insert_country_data(conn: object) -> None:
    """Insert counry data.

    Inserts counry data into the country_codes table

    Args:
        conn: SQLite3 connection object

    """
    # Open Country data in pandas
    curr_dir = os.getcwd()
    file_path = os.path.join(curr_dir, "csv_files", "country-and-continent-codes.csv")
    data_frame = pandas.read_csv(file_path)

    data_frame.to_sql("country_codes", conn, if_exists="replace", index=False)


def insert_country_data_row(conn: object, row_values: list) -> None:
    """Insert country data row.

    Inserts row of country data into country table in locations database.

    Args:
        conn: SQLite3 connection object
        row_values: List of values from the Pandas dataframe row.

    """
    sql = """ INSERT INTO country_codes
    (
        continent_name,
        continent_code,
        country_name,
        two_letter_country_code,
        three_letter_country_code,
        country_number
    )
    VALUES(?,?,?,?,?,?)"""

    try:
        cursor = conn.cursor()
        cursor.execute(sql, row_values)
        conn.commit()
    except Error as e:
        print(row_values)
        print(e)


def insert_geocode_data(conn: object) -> None:
    """Insert geocode data.

    Inserts geocode data into locations database.

    Opens the csv files that contain the geocode data directory
    and iterates through to insert the geocode data by section.


    Args:
        conn: SQLite3 connection object

    """
    curr_dir = os.getcwd()
    dir_path = os.path.join(curr_dir, "csv_files", "split_csv")

    files = os.listdir(dir_path)
    file_percentage_single = 100 / len(files)

    for i in range(len(files)):
        file = files[i]
        file_path = os.path.join(dir_path, file)
        insert_geocode_data_section(conn, file_path)
        print(f"Geocode section complete: {file}")
        print(f"Percentage complete: {(i + 1)* file_percentage_single}%")

    print(files)


def insert_geocode_data_section(conn: object, file_path: str) -> None:
    """Insert geocode data section.

    Opens ands processes geocode data section csv file and
    then inserts it into the geocode_data table in the locations
    database.

    Args:
        conn: SQLite3 connection object
        file_path: string of filepath to section csv

    """
    data_frame = pandas.read_csv(file_path, sep="\t")
    # data_frame.reset_index(drop=True)

    data_frame.to_sql("geocode", conn, if_exists="append", index=False)


if __name__ == "__main__":
    conn = create_connection()
    print("Database Created")
    create_tables(conn)
    print("Tables Created")
    insert_country_data(conn)
    print("Country Data Populated")
    print("Populating Geocode data: This may take a long time.")
    insert_geocode_data(conn)
    print("Geocode Data Populated")
    print("Set up process complete")
    conn.close()
