# Tutorial - Installation and Usage

## Requirements

Python3 installation is required. The Python3 Venv package is recommended.

If Python3 is not available - the project can be run by downloading the executables folder that matches the OS that your computer uses. The project can be started by opening the report-generator file.

## Installation

### Installation from PyPI

To install from PyPI and using pip it is recommended to initially set up a virtual environment or use a package manager like poetry.

#### Create Venv

        python3 -m venv {venv-name}

![Project Installation 1: Create Venv](https://github.com/ccushnahan/report_generator/raw/main/docs/images/create_venv.gif)

#### Activate Venv

Then activate the venv.

        source {venv-name}/bin/activate

![Project Installation 2: Activate Venv](https://github.com/ccushnahan/report_generator/raw/main/docs/images/activate_venv.gif)

#### Install package

Then install the package.

        pip install qub-amphibian-report-generator

![Project Installation 3: Install Package](https://github.com/ccushnahan/report_generator/raw/main/docs/images/install_report_generator.gif)

## Use

### GUI

Once the package has been installed and setup the Report Generator program can be used from venv with the command:

        report-generator

This will start the GUI application for the report generator. If the report-generator command has not been run before it will begin the project setup process.

#### Project Setup

The user will need to enter some project settings information:

![Project Setup 1: Enter project settings](https://github.com/ccushnahan/report_generator/raw/main/docs/images/project_setup_1.gif)

The process will download relevant data files and create and insert data into project databases:

![Project Setup 2: Enter project settings](https://github.com/ccushnahan/report_generator/raw/main/docs/images/project_setup_2.gif)

![Project Setup 3: Enter project settings](https://github.com/ccushnahan/report_generator/raw/main/docs/images/project_setup_3.gif)

![Project Setup 4: Enter project settings](https://github.com/ccushnahan/report_generator/raw/main/docs/images/project_setup_4.gif)

#### Create Report

This will then allow the user to run the report generator again and produce the outputted pdf file.

![Create Report: Demo Report creation](https://github.com/ccushnahan/report_generator/raw/main/docs/images/create_report.gif)

### CLI

If the user wants to use the CLI:

        report-generator --cli [options]

#### CLI default report

![CLI Create Report](https://github.com/ccushnahan/report_generator/raw/main/docs/images/report_cli_1.gif)

#### CLI filtered report

![CLI Filtered Create Report](https://github.com/ccushnahan/report_generator/raw/main/docs/images/report_cli_2.gif)

#### CLI options

CLI options can be found with the command:

        report-generator -h
        report-generator -help

![CLI Options](https://github.com/ccushnahan/report_generator/raw/main/docs/images/report_cli_3.gif)

Or can be found in the projects documentation.

#### New Project with CLI

If the user wants to set up a new project:

        create-report-generator

![CLI New Report Project](https://github.com/ccushnahan/report_generator/raw/main/docs/images/create_report_generator.gif)
