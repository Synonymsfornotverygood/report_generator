"""Report Generator.

Application to create report based on parameters passed into it.

@Params:
        data_source         - Data source for report creation
        report_name         - Title of the report and the file name
        report_author       - Author of the report
        university_name     - Name of the university
        university_school   - Name of the university school

@Todo:
    - Implement passing params - statically implemented currently
    - Implement detect data source type to allow for differing file types/sources?
    - Abstract source reading into a different class - excel extraction for one

"""
import time

import yaml

import report_generator.report_generator_cli.create_report as create_report


def main(arguments: dict) -> None:

    startTime = time.time()
    config = None
    with open("config.yaml", "r") as file:
        config = yaml.load(file, Loader=yaml.loader.SafeLoader)

    data_source = config["data_set"]
    report_name = config["report_name"].upper()
    report_author = config["author_name"].upper()
    university_name = config["uni_name"].upper()
    university_school = config["school_name"].upper()

    print(f"Creating Report: {report_name}.pdf")
    create_report.create_report(
        data_source,
        arguments,
        report_name,
        report_author,
        university_name,
        university_school,
    )
    print(f"Report Complete: {report_name}.pdf")

    executionTime = time.time() - startTime
    print("Report creation time in seconds: " + str(executionTime))


if __name__ == "__main__":
    main()


# parse params

# open/create new document

# perform query

# transform json response to list of object

# work through list

# pass data to template based on style parameters

# process according to template

# add to document

# finish process

# save document

# end message
