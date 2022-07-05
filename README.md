# REPORT GENERATOR

## Requirements

Python3 is required to be installed on the computer. Also, the python3 Venv package is required to be installed. 

Further project requirements for external Python libraries can be found in the requirements.txt file. This file is located in the root folder of the project directory.

The rest of the process of the project's setup is outlined in the installation section below.

## Installation

To install the project: first download the project code from the repository.  Extract or pull the code into the directory of your choice. Open a terminal in this directory. 

Next set up the virtual environment. This allows us to install the project's libraries without affecting the broader Python environment on the computer. (In example code Python's venv is used.)

        python3 -m venv {venv-name}

This will create a virtual environment to install the project's required libraries. We then activate it through the following command:

        source {venv-name}/bin/activate

We then install the required files:

        pip install requirements.txt

When this process has been completed it is now possible to use the program.


## Use

The program can then be used through either of the following methods:

        python3 application/main.py {report_name} {report_author} {report_university} {report_school}

Or by editing the default values in application/create_report.py and typing the following command into the terminal:

        python3 application/create_report.py


## Example

Example report can be found in the Test_Report.pdf in examples directory 


## Versions

Archived versions of the Report Generator Program can be found in links to repositories below
- [Report Generator V1](https://gitlab2.eeecs.qub.ac.uk/13067079/report_generator_v1)
- [Report Generator V2](https://gitlab2.eeecs.qub.ac.uk/13067079/report-generator-v2)