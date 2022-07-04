'''

Application to create report based on parameters passed into it

@Params:
        data_source
        report_name
        report_author
        university_name
        university_school
        full_report

@Todo:
    - Implement passing params - statically implemented currently
    - Implement detect data source type to allow for differing file types/sources?
    - Abstract source reading into a different class - excel extraction for one 

'''
import os
import subprocess
from time import sleep
from venv import create
import write_report
import pdf_creator

if __name__ == "__main__":

    data_source = "AMPH PILOT DATASET_V5_25.June.2022.xlsx"
    report_name = "Test Report"
    report_author = "Daniel Pincheira-Donoso"
    university_name = "Queen's University Belfast"
    university_school = "School Of Biological Sciences"

    write_report.write_report(data_source, report_name, report_author, university_name, university_school)

    folder_name = "_".join(report_name.split(" "))
    files = os.listdir(folder_name)
    for file in files:
        html_file_name = f"{folder_name}/{file}"
        html_file_path = pdf_creator.get_file_path(html_file_name)
        pdf_file_path = f"{folder_name}/{file.split('.')[0]}.pdf"

        print(html_file_path)
        print(pdf_file_path)
        sleep(2)
        process_str = f"python3 application/pdf_creator.py '{html_file_path}' '{pdf_file_path}'"
        # print(process_str)
        subprocess.call(process_str, shell=True)
        print("Finished")

























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