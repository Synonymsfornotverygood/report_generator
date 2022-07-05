'''

Application to create report based on parameters passed into it

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

'''
import create_report

if __name__ == "__main__":

    data_source = "AMPH PILOT DATASET_V5_25.June.2022.xlsx"
    report_name = "Test Report"
    report_author = "Daniel Pincheira-Donoso"
    university_name = "Queen's University Belfast"
    university_school = "School Of Biological Sciences"

    create_report.create_report(data_source, report_name, report_author, university_name, university_school)

























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