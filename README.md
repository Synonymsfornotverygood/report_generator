# REPORT GENERATOR

## Requirements

Python3 is required to be installed on the computer. Also, the python3 Venv package is required to be installed.

If Python3 is not available program can be ran by downloading executable files found in zipped in the dist_zip directory.

Further project requirements for external Python libraries can be found in the requirements.txt file. This file is located in the root folder of the project directory.

The rest of the process of the project's setup is outlined in the installation section below.

## Installation

### Installation from PyPI

Use the following in the command line:

 pip install qub-amphibian-report-generator

**Curently not working please ignore**

### Installation from Git Repository

To install the project: first download the project code from the repository.  Extract or pull the code into the directory of your choice. Open a terminal in this directory.

Next set up the virtual environment. This allows us to install the project's libraries without affecting the broader Python environment on the computer. (In example code Python's venv is used.)

        python3 -m venv {venv-name}

This will create a virtual environment to install the project's required libraries. We then activate it through the following command:

        source {venv-name}/bin/activate

We then install the required files:

        pip install requirements.txt

Then install package:

        python -m build

        pip install -e .

When this process has been completed it is now possible to use the program.

### Installation from executable files

Download the file. Unzip file. Open directory and double-click app file.

## Use

Once the package has been installed and setup the Report Generator program can be used from venv with the command:

        report-generator

This will start the GUI application for the report generator

If the user wants to use the CLI:

        report-generator --cli [options]

CLI options can be found with the command:

        report-generator -h
        report-generator -help

Or can be found in the projects documentation.

If the user wants to set up a new project:

        create-report-generator

## Documentation

Project documentation can be found [here](https://ccushnahan.github.io/report_generator/)


## Versions

Archived versions of the Report Generator Program can be found in links to repositories below
- [Report Generator V1](https://gitlab2.eeecs.qub.ac.uk/13067079/report_generator_v1)
- [Report Generator V2](https://gitlab2.eeecs.qub.ac.uk/13067079/report-generator-v2)


## Changelog

