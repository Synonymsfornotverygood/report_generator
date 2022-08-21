"""Report Generator.

A tool to create pdf reports from excel (.xlsx) spreadsheet.

Usage:
    report-generator --gui
    report-generator --new
    report-generator --cli
    report-generator --no-setup
    report_generator

Options:
    -h --help   Show this screen.
    --version   Show version.
    --gui       Use GUI
    --cli       Use CLI
    --new       Create new report project
    --no-setup  Do not check for config settings
                instead supply string values to create project
                works directly from Excel(.xlsx) file.
"""


from docopt import docopt

import report_generator.report_generator_cli.main
import report_generator.report_generator_gui.test


def main():
    """Driver function.

    Main function for application. Takes no arguments currently.
    """

    arguments = docopt(__doc__, version="Report Generator 1.0")

    # check if gui option selected
    if arguments["--gui"] is True:
        report_generator.report_generator_gui.test.main()
    if arguments["--cli"] is True:
        print("cli")
        report_generator.report_generator_cli.main.main()
    else:
        print("Invalid option chosen! For help type: 'report-generator --help'")


if __name__ == "__main__":
    main()
