"""Report Generator.

A tool to create pdf reports from excel (.xlsx) spreadsheet.

Usage:
    report-generator
    report-generator --gui
    report-generator --new
    report-generator --no-db
    report-generator --cli [--order_taxon_name=<ordname>]
                    [--Family=<famname>]
                    [--Genus=<genname>]
                    [--Species=specname]
                    [--SVLMx=<sm>]...
                    [--SVLMMx=<smm>]...
                    [--SVLFMx=<smf>]...
                    [--ClutchMin=<cmn>]...
                    [--ClutchMax=<cmx]...
                    [--Clutch=<ca>]...
                    [--ParityMode=<pmd>]...
                    [--EggDiameter=<ed>]...
                    [--Longevity=<lmn>]...
                    [--NestingSite=<nsd>]
                    [--MicroHabitat=<mhn>]
                    [--Activity=<ak>]
                    [--GeographicRegion=<gr>]
                    [--IUCN=<iucn>]
                    [--PopTrend=<pt>]


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
import report_generator.report_generator_gui.main


def main():
    """Driver function.

    Main function for application. Takes no arguments currently.
    """

    arguments = docopt(__doc__, version="Report Generator 1.0")
    # check if gui option selected
    if arguments["--gui"] is True:
        report_generator.report_generator_gui.main.main()
    if arguments["--cli"] is True:
        print("Report Generator CLI")
        report_generator.report_generator_cli.main.main(arguments)
    else:
        report_generator.report_generator_gui.main.main()


if __name__ == "__main__":
    main()
