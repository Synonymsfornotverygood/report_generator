'''

Application to create report based on parameters passed

'''

import openpyxl
import pandas
import os
from jinja2 import Template, Environment, FileSystemLoader
from amphibian import AmphibianData

filename = "AMPH PILOT DATASET_V5_25.June.2022.xlsx"


df = pandas.read_excel(filename)
df["comb_name"] = df["Order"] +" " + df["Family"]
comb = df["comb_name"]
comb_names = comb.value_counts().index.tolist()


amps = []


for row in df.iterrows():
    vals = []
    for value in row:
        if (isinstance(value, int)):
            vals.append(value)
        else:
            vals = [*vals, *value.values]
    for i in range(len(vals)):
        if (pandas.isna(vals[i])):
            vals[i] = "Unknown"
    a = AmphibianData(vals)
    amps.append(a)

report_name= "Test Report"
report_author = "Daniel Pincheira-Donoso"
university_name = "Queen's University Belfast"
university_school = "School Of Biological Sciences"

env = Environment(loader=FileSystemLoader('templates'))
rendered = env.get_template("template.html").render(report_name=report_name, report_author=report_author, university_name=university_name, university_school=university_school,  amp_list=amps)


with open("report.html", "w") as file:
    file.write(rendered)



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