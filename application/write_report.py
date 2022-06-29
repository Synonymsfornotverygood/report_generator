import openpyxl
import pandas
import os
from jinja2 import Template, Environment, FileSystemLoader
from amphibian import AmphibianData



def write_report(data_source: str, report_title: str, report_author: str, uni_name: str, school_name: str, full_report=False) -> None :

    file_name = data_source
    report_name= report_title
    report_author = report_author
    university_name = uni_name
    university_school = school_name

    df = read_data_source(file_name)


    if (full_report):
        create_full_html_report(df)
    else: 
        report_sections = create_report_sections(df)
        create_html_reports(report_sections, report_name, report_author, university_name, university_school)


def read_data_source(file_name: str) -> object:

    df = pandas.read_excel(file_name)
    df["comb_name"] = df["Order"] +" " + df["Family"]

    return df

def create_report_sections(data_frame: object) -> list:

    comb = data_frame["comb_name"]
    comb_names = comb.value_counts().index.tolist()
    sections = []

    for name in comb_names:
        data_section = data_frame[data_frame["comb_name"] == name]
        section_amphibians = create_amphibian_list(data_section)
        sections.append((name, section_amphibians))

    return sections


def create_amphibian_list(data_section: object) -> list:
    amphibian_list = []
    for row in data_section.iterrows():
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
        amphibian_list.append(a)
    return amphibian_list

def generate_contents_page_list(report_data: list) -> list:
    
    diff_vals = []
    diff_genus = []
    contents_sections = []

    for i in range(len(report_data)):
        amp = report_data[i]
        genus = amp.genus
        if genus not in diff_vals:
            diff_vals.append(genus)
            diff_genus.append((amp.position, amp.genus))
    
    for i in range(0, len(diff_genus), 25):
        contents_sections.append(diff_genus[i: i+25])

    return contents_sections


def generate_index_section_list(report_data: list) -> list:

    index_sections = []
    
    for i in range(0, len(report_data), 30):
        index_sections.append(report_data[i: i+30])

    return index_sections


def check_section_size(section: tuple, max_size: int) -> bool:
    return len(section[1]) < max_size

def create_html_report(report_section: tuple,  report_name: str, report_author: str, university_name: str, university_school:str) -> None:

    report_sub_name = report_section[0]
    report_data = report_section[1]

    contents_info = generate_contents_page_list(report_data)
    index_info = generate_index_section_list(report_data)

    env = Environment(loader=FileSystemLoader('templates'))
    rendered = env.get_template("template.html").render(report_name=report_name, report_sub_name=report_sub_name, report_author=report_author, university_name=university_name, university_school=university_school, report_data=report_data, contents_info=contents_info, index_info=index_info)

    folder_name = "_".join(report_name.split(" ")) 
    file_name = "_".join(f"{report_name} - {report_sub_name}.html".split(" "))
    with open(f"{folder_name}/{file_name}", "w") as file:
        file.write(rendered)


def create_sub_sections(section: tuple) -> list:

    sub_section_list = []

    for i in range(0, len(section[1]), 400):
        sub_section_data = section[1][i: i + 400]
        sub_section_name = f"{section[0]} - {len(sub_section_list) + 1}"
        sub_section_list.append((sub_section_name, sub_section_data))

    return sub_section_list

def create_html_reports(report_sections: list, report_name: str, report_author: str, university_name: str, university_school:str) -> None:
    try:
        os.mkdir("_".join(report_name.split(" ")))
    except Exception:
        print("Dir exists")

    for section in report_sections:
        if check_section_size(section, 400):
            create_html_report(section, report_name, report_author, university_name, university_school)
        else:
            sub_sections = create_sub_sections(section)
            for sub_section in sub_sections:
                create_html_report(sub_section, report_name, report_author, university_name, university_school)


def create_full_html_report(data_frame: object, report_name: str, report_author: str, university_name: str, university_school:str): 
    amp_list = create_amphibian_list(data_frame)
    report_section = (report_name, amp_list)
    create_html_report(report_section, report_name, report_author, university_name, university_school)
