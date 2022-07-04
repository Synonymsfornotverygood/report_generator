
import os
from amphibian import AmphibianData
from jinja2 import Template, Environment, FileSystemLoader
from xhtml2pdf import pisa
import pdf_creator
import pandas
from weasyprint import HTML, CSS
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger



def create_report(data_source, report_name):
    
    file_name = data_source
    df = read_data_source(file_name)
    amp_list = create_amphibian_list(df)
    create_report_folder(report_name)
    create_report_pages(amp_list, report_name)

# create report folder

def create_report_folder(report_name: str) -> None:

    """
    Creates the directories for the report and its components
    """
    try:
        os.mkdir(report_name)
        os.mkdir(f"{report_name}/title")
        os.mkdir(f"{report_name}/contents")
        os.mkdir(f"{report_name}/pages")
        os.mkdir(f"{report_name}/index")
    except Exception:
        print("folder exists")


def create_report_pages(data_list: list, report_name: str) -> None:
    """
    Creates pages from list of data sent 
    """

    for i in range(len(data_list)):
        data_entry = data_list[i]
        create_report_page(data_entry, i + 1, report_name)


def create_report_page(data_row: object, page_number: int, report_name: str) -> None:

    """
    Takes a row of data from data source and passes to template and renders it as a report page
    """

    rendered_html = create_report_page_html(data_row, page_number, report_name)
    create_report_page_pdf(page_number, report_name, rendered_html) 


def create_report_page_html(data_row: object, page_number: int, report_name: str) -> str:
    print(f"Creating Page: {report_name} - page_{page_number}.html")
    path = "file://" + os.getcwd()
    env = Environment(loader=FileSystemLoader('templates'))
    rendered = env.get_template("partials/species_report.html").render(n=data_row, path=path)

    with open(f"{report_name}/pages/page_{page_number}.html", "w") as file:
        file.write(rendered)

    return rendered

def image_fetcher(location):
    pass

def create_report_page_pdf(page_number: int, report_name: str, rendered_html: str) -> str:
    print(f"Creating Page: {report_name} - page_{page_number}.pdf")
    input_filename = f"{report_name}/pages/page_{page_number}.html"
    output_filename = f"{report_name}/pages/page_{page_number}.pdf"

    HTML(string=rendered_html).write_pdf(output_filename, stylesheets=[CSS(filename="templates/styles/entireframework.min.css"), CSS(filename="templates/styles/style.css")])

def create_title_page(title_info: object) -> None:

    """
    Takes an object with title information passes it to template and renders it as a report title page
    """


def create_chapters(chapter_info) -> None:

    """
    Structures a chapter
    """

def read_data_source(file_name: str) -> object:
    """
    Read the data_source file and transform it into a pandas dataframe
    """

    df = pandas.read_excel(file_name)
    df["comb_name"] = df["Order"] +" " + df["Family"]

    return df

def create_amphibian_list(data_section: object) -> list:
    
    """
    Takes a row of data from the dataframe and extracts values and instantiates an instance of the AmphibianData class
    """

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

def merge_pages(report_name: str, output_file: str) -> None:


    pdf_files = os.listdir(report_name + "/pages")

    pdf_files.sort()

    sections = []

    for i in range(0, len(pdf_files), 500):
        sections.append(pdf_files[i:i+500])


    for i in range(len(sections)):
        pdf_merger = PdfFileMerger()
        for file in sections[i]:
            if "pdf" in file:
                print(file)
                pdf_reader = PdfFileReader(f"{report_name}/pages/{file}")
                pdf_merger.append(pdf_reader, "wb")

        with open(f"{report_name}/merger/{report_name}-{i}.pdf", "wb") as out:
            pdf_merger.write(out)



if __name__ == "__main__":
    

    create_report("AMPH PILOT DATASET_V5_25.June.2022.xlsx", "test_report")
    merge_pages("test_report", "test_output.pdf")