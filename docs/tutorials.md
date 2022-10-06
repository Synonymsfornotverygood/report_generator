## Installation

### Installation from PyPI

To install from PyPI and using pip it is recommended to initially set up a virtual environment or use a package manager like poetry.

                python3 -m venv {venv-name}

Then activate the venv.

                source {venv-name}/bin/activate


Then install the package.

                pip install qub-amphibian-report-generator

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