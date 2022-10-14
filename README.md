# REPORT GENERATOR

## Requirements

Python3 installation is required. The Python3 Venv package is recommended.

If Python3 is not available - the project can be run by downloading the executables folder that matches the OS that your computer uses. The project can be started by opening the report-generator file.

## Installation

### Installation from PyPI

To install from PyPI and using pip it is recommended to initially set up a virtual environment or use a package manager like poetry.

#### Create Venv

        python3 -m venv {venv-name}

<img src="docs/images/create_venv.gif" alt="Project Installation 1: Create Venv" title="project_installation_1" width="75%">

#### Activate Venv

Then activate the venv.

        source {venv-name}/bin/activate

<img src="docs/images/activate_venv.gif" alt="Project Installation 2: Activate Venv" title="project_installation_2" width="75%">

#### Install package

Then install the package.

        pip install qub-amphibian-report-generator

<img src="docs/images/install_report_generator.gif" alt="Project Installation 3: Install Package" title="project_installation_3" width="75%">

### Installation from Git Repository

To install the project: first download the project code from the repository. Extract or pull the code into the directory of your choice. Open a terminal in this directory.

Next set up the virtual environment. This allows us to install the project's libraries without affecting the broader Python environment on the computer. (In example code Python's venv is used.)

    python3 -m venv {venv-name}

This will create a virtual environment to install the project's required libraries.

#### Linux/Mac
We then activate it through the following command:

    source {venv-name}/bin/activate

#### Windows

We then activate it through the following command:

        venv\Scripts\activate.bat

We then install the required files:

    pip install requirements.txt

Then install package:

    pip install -e .

When this process has been completed it is now possible to use the program.


## Use

### GUI

Once the package has been installed and setup the Report Generator program can be used from venv with the command:

        report-generator

This will start the GUI application for the report generator. If the report-generator command has not been run before it will begin the project setup process.

#### Project Setup

The user will need to enter some project settings information:

<img src="docs/images/project_setup_1.gif" alt="Project Setup 1: Enter project settings" title="project_setup_1" width="75%">

The process will download relevant data files and create and insert data into project databases:

<img src="docs/images/project_setup_2.gif" alt="Project Setup 2: Enter project settings" title="project_setup_2" width="75%">

<img src="docs/images/project_setup_3.gif" alt="Project Setup 3: Enter project settings" title="project_setup_3" width="75%">

<img src="docs/images/project_setup_complete.gif" alt="Project Setup 4: Enter project settings" title="project_setup_4" width="75%">

#### Create Report

This will then allow the user to run the report generator again and produce the outputted pdf file.

<img src="docs/images/create_report.gif" alt="Create Report: Demo Report creation" title="create report" width="75%">

### CLI

If the user wants to use the CLI:

        report-generator --cli [options]

#### CLI default report

<img src="docs/images/report_cli_1.gif" alt="CLI Report creation" title="create report 1" width="75%">

#### CLI filtered report

<img src="docs/images/report_cli_2.gif" alt="CLI Report creation" title="create report 2" width="75%">

#### CLI options

CLI options can be found with the command:

        report-generator -h
        report-generator -help

<img src="docs/images/report_cli_3.gif" alt="CLI Report creation" title="create report 3" width="75%">

Or can be found in the projects documentation.

#### New Project with CLI

If the user wants to set up a new project:

        create-report-generator

<img src="docs/images/create_report_generator.gif" alt="CLI New Report Project" title="CLI new project" width="75%">

## Documentation

Project documentation can be found [here](https://ccushnahan.github.io/report_generator/)


## Versions

Archived versions of the Report Generator Program can be found in links to repositories below
- [Report Generator V1](https://gitlab2.eeecs.qub.ac.uk/13067079/report_generator_v1)
- [Report Generator V2](https://gitlab2.eeecs.qub.ac.uk/13067079/report-generator-v2)


## Changelog

