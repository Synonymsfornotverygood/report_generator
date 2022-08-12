# Excel Extraction

Application to open and extract data from version of amphibian dataset in excel

CLI interface takes file path argument and extracts data. Then cleans dataset then passes
the data to api.

This tool accepts comma separated value files (.csv) as well as Excel files (.xlsx, xls).

This script requires that 'pandas' be installed within the Python environment that this is running on.


## Requirements

- Python
- sqlite3
- Pandas
- Openpyxl

## Installation

Set up a virtual environment

    python3 -m venv {virtual env name}

    python3 -m venv extract-venv


Activate virtual environment

    source extract-venv/bin/activate


Use the following command to install the required python packages

    pip install requirements.txt


## Use

Activate virtual environment

    source extract-venv/bin/activate

Call the program from the command line

    python3 src/excel_to_sql.py {excel_file_name}

If you want to test from the example excel file in example dir

    python3 src/excel_to_sql.py
