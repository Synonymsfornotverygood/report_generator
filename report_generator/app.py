"""Report Generator.

A tool to create pdf reports from excel (.xlsx) spreadsheet.

Usage:
    report-generator
    report-generator --gui
    report-generator --new
    report-generator --no-db
    report-generator --cli [--order_name=<ordname>]
                    [--family_name=<famname>]
                    [--genus_name=<genname>]
                    [--species_name_latin=specname]
                    [--size_max=<sm>]...
                    [--size_max_male=<smm>]...
                    [--size_max_female=<smf>]...
                    [--clutch_min=<cmn>]...
                    [--clutch_max=<cmx]...
                    [--clutch_avg=<ca>]...
                    [--parity_mode_desc=<pmd>]...
                    [--egg_diameter=<ed>]...
                    [--longevity_min=<lmn>]
                    [--longevity_max=<lmx>]
                    [--nesting_site_desc=<nsd>]
                    [--micro_habitat_name=<mhn>]
                    [--activity_kind=<ak>]
                    [--GeographicRegion=<gr>]
                    [--iucn_status=<iucn>]
                    [--pop_trend_status=<pt>]


Options:
    -h --help               Show this screen.
    --version               Show version.
    --gui                   Use GUI
    --cli                   Use CLI
    --new                   Create new report project
    --no-db                 Do not check for db settings
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
    print(arguments)
    # check if gui option selected
    if arguments["--gui"] is True:
        report_generator.report_generator_gui.test.main()
    if arguments["--cli"] is True:
        print("Report Generator CLI")
        report_generator.report_generator_cli.main.main(arguments)
    else:
        print("Invalid option chosen! For help type: 'report-generator --help'")


if __name__ == "__main__":
    main()
