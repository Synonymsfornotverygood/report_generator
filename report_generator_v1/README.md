# Report Generator V1

This is the original version of the report generator program
- Archived for reference
- May only be compatible with linux systems due to hardcoded paths that have not been refactored out
  - Minor effort to change therefore for windows/mac
- Requirements.txt may install packages no longer required for the report generator

## Installation and Set up

Create a directory for the report generator and move the report_generator_v1 to there.

Rename the folder "report_generator"

Navigate to that directory

Create a virtual environment for the program

        python3 -m venv venv_dir_name

Activate the virtual environment

        source venv_dir_name/bin/activate

Install the requiements.txt file

        pip install requirements.txt

## Use

Place the data-set source file into report generator folder

Edit the main.py file to change source file name if needed and other report variables such as Report Name and Author

Run the command

        python3 applications/main.py

This will create a folder based on the report name and create a html file based on the source and a pdf file. 