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
import os
import time

import create_report

if __name__ == "__main__":
    startTime = time.time()
    data_source = os.getcwd() + "/" + "GABiP DATABASE_V5_06.July.2022-1.xlsx"
    # data_source = os.getcwd() + "/" +  "test.xlsx"
    report_name = "Updated Data-Set Test".upper()
    # report_name = "Big Data"
    report_author = "Daniel Pincheira-Donoso".upper()
    university_name = "Queen's University Belfast".upper()
    university_school = "School Of Biological Sciences".upper()

    print(f"Creating Report: {report_name}.pdf")
    create_report.create_report(
        data_source, report_name, report_author, university_name, university_school
    )
    print(f"Report Complete: {report_name}.pdf")

    executionTime = time.time() - startTime
    print("Report creation time in seconds: " + str(executionTime))


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
