"""

Application to create pdf report based on parameters passed into it

@Params:
        data_source         - Data source for report creation
        report_name         - Title of the report and the file name
        report_author       - Author of the report 
        university_name     - Name of the university
        university_school   - Name of the university school

@Todo:
    - Implement detect data source type to allow for differing file types/sources?
    - Error handling
    - Remove hardcoded elements
    - Split functions further or into their own file
    - Refactor the create_x_section functions into one function that takes a section arg 

"""





# Library Imports
from fpdf import FPDF, TitleStyle, errors, TextMode
from fpdf.outline import build_outline, outline_as_str
from fpdf.syntax import iobj_ref as pdf_ref
import pandas
import os
import sys


# Local Imports
from amphibian import AmphibianData

# Create report

def create_report(data_source: str, report_name: str, report_author: str, university_name: str, university_school: str) -> None:

    """
    Primary function that creates pdf object, sets fonts, calls component creation methods and saves output.

    Args:
        data_source         - Data source for report creation
        report_name         - Title of the report and the file name
        report_author       - Author of the report 
        university_name     - Name of the university
        university_school   - Name of the university school

    """


    ds = read_data_source(data_source)
    pdf = FPDF()
    pdf.add_font("OpenSans", fname="fonts/OpenSans-VariableFont_wdth,wght.ttf")
    pdf.add_font("OpenSansBold", fname="fonts/static/OpenSans/OpenSans-Bold.ttf")
    pdf = create_title_page(report_name, report_author, university_name, university_school, pdf)
    pdf= create_contents_page(pdf)
    pdf = create_report_order_sections(ds, pdf)
    pdf.output(f"{'_'.join(report_name.split(' '))}.pdf")

# create title page

def create_title_page(report_name: str, report_author: str, university_name: str, university_school: str, pdf: object) -> object:

    """
    Creates a title page based upon passed args. Adds text and images to pdf.page() then returns pdf object.

    Process:
        Adds page
        Designates contents section
        Adds background image
        Adds banner image
        Adds Text
        Returns pdf obj



    Args:
        data_source         - Data source for report creation
        report_name         - Title of the report and the file name
        report_author       - Author of the report 
        university_name     - Name of the university
        university_school   - Name of the university school


    Return:
        pdf(obj) - pdf object
    """

    pdf = FPDF()
    pdf.add_page()
    pdf.start_section(name="Title Page", level=0)
    with pdf.local_context(fill_opacity=0.5, stroke_opacity=0.5):
        pdf.image("images/back.png",x=0, y=0, h=300)
    pdf.image("images/school_banner.png",x=30, y=250, h=50)
    with pdf.local_context(
        text_mode=TextMode.FILL, text_color=(227,6,19), line_width=2
    ):
        pdf.add_font("OpenSans", fname="fonts/OpenSans-VariableFont_wdth,wght.ttf")
        pdf.add_font("OpenSansBold", fname="fonts/static/OpenSans/OpenSans-Bold.ttf")
        pdf.set_font("OpenSansBold", "", 56)

        pdf.set_draw_color(255,255,255)
        pdf.ln(30)
        # pdf.write(20, report_name)
        pdf.cell(w=20)
        pdf.cell(w=150,txt=report_name, align="L", border=0)
        pdf.ln(105)
        pdf.set_font("OpenSansBold", "", 28)
        # pdf.write(10, report_author)
        pdf.cell(w=20)
        pdf.cell(w=150,txt=report_author, align="L", border=0)
        pdf.set_font("OpenSans", "", 22)

        pdf.ln(20)
        # pdf.write(10, university_name)
        pdf.cell(w=20)
        pdf.cell(w=150,txt=university_name, align="L", border=0)

        pdf.ln(10)
        # pdf.write(10, university_school)
        pdf.cell(w=20)
        pdf.cell(w=150,txt=university_school, align="L", border=0)


    return pdf

# Contents page

def create_contents_page(pdf: object) -> object:

    """
    Creates space for contents to be created in the document. Currently hardcoded. Will throw exception if the space isn't the correct amount.

    Args:
        pdf - pdf object

    Return:
        pdf - pdf object
    """

    pdf.add_page()
    pdf.set_text_color(0,0,0)
    pdf.start_section(name="Table Of Contents", level=0)
    pdf.insert_toc_placeholder(render_toc, 9)
    return pdf



def create_report_order_sections(ds: object, pdf: object) -> object:

    """
    Filter function that splits the data frame (ds) into smaller dataframes based on the 'Order' column in the dataframe.  

    Process:
        Creates dataframe subsections
        Sorts the new dataframes.
        Loops through each of smaller dataframes to create contents section and level
        Writes section title 
        Passes section to the next filter function.

    Args:
        ds - Pandas Dataframe object
        pdf - pdf object

    Returns:
        pdf - pdf object
    """

    order = ds["Order"]
    order_names = order.value_counts().index.tolist()
    order_names.sort()
    order_sections = []
    for name in order_names:
        sect = ds[ds["Order"] == name]
        pdf.add_page()
        pdf.start_section(name=name, level=0)
        pdf.set_font('OpenSansBold', "", 48)
        pdf.ln(20)
        pdf.write(30, f"Order: {name}", "C")
        pdf.ln(20)
        pdf = create_report_family_sections(sect, pdf)

    return pdf

def create_report_family_sections(section_list: object, pdf:object) -> object:

    """
    Filter function that splits the data frame (section_list) into smaller dataframes based on the 'Family' column in the dataframe.  

    Process:
        Creates dataframe subsections
        Sorts the new dataframes.
        Loops through each of smaller dataframes to create contents section and level
        Writes section title 
        Passes section to the next filter function.

    Args:
        section_list - Pandas Dataframe object
        pdf - pdf object

    Returns:
        pdf - pdf object
    """

    family = section_list["Family"]
    family_names = family.value_counts().index.tolist()
    family_names.sort()
    for name in family_names:
        sect = section_list[section_list["Family"] == name]
        pdf.start_section(name=name, level=1)
        pdf.set_font('OpenSansBold', "", 36)
        pdf.ln(20)
        pdf.write(10, f"Family: {name}", "C")
        pdf.add_page()
        pdf = create_report_genus_sections(sect, pdf)

    return pdf

def create_report_genus_sections(section_list: object, pdf: object) -> object:

    """
    Filter function that splits the data frame (ds) into smaller dataframes based on the 'Family' column in the dataframe.  

    Process:
        Creates dataframe subsections
        Sorts the new dataframes.
        Loops through each of smaller dataframes to create contents section and level
        Writes section title 
        Passes section to the create report pages function.

    Args:
        section_list - Pandas Dataframe object
        pdf - pdf object

    Returns:
        pdf - pdf object
    """

    genus = section_list["Genus"]
    genus_names = genus.value_counts().index.tolist()
    genus_names.sort()
    for name in genus_names:
        sect = section_list[section_list["Genus"] == name]
        pdf.set_font('OpenSansBold', "", 36)
        pdf.ln(10)
        pdf.write(10, f"Genus: {name}")
        pdf.start_section(name=name, level=2)
        pdf = create_report_section_pages(sect, pdf)

    return pdf


# Create pages
def create_report_section_pages(section, pdf):

    """
    Takes the section passed to it. Passes section to 'create_amphibian_list' function to get the data transformed into a list of amphibian objects. Sorts the list by name. Loops through list of amphibian objects and passes them to the 'create_report_section_page' function.

    Args:
        section - pandas dataframe object
        pdf - pdf object

    Return: 
        pdf - pdf object

    """


    amp_list = create_amphibian_list(section)
    amp_list = sorted(amp_list, key=lambda a: a.species)

    # Hardcoded example image will have to replace this 
    amp_list[0].image_url_male = "images/f1.jpg"
    amp_list[0].image_url_female = "images/f2.jpg"

    for amp in amp_list:
        pdf = create_report_section_page(amp, pdf)
    return pdf

# create page
def create_report_section_page(amp, pdf):

    """
    Takes an instance of Amphibian and creates a page. Adds title. Adds images (insert_species_images). Adds data table (create_report_page_table). Then returns pdf object. 

    Args:
        amp - Amphibian object
        pdf - pdf object

    Return: 
        pdf - pdf object
    """

    pdf.start_section(name=amp.get_short_name(), level=3)
    pdf.set_font('OpenSansBold', "", 24)
    pdf.ln(20)
    pdf.write(10, amp.get_short_name())
    pdf = insert_species_images(amp, pdf)
    pdf = create_report_page_table(amp, pdf)
    pdf.add_page()

    return pdf

# add images

def insert_species_images(amp, pdf):

    """
    Takes an instance of Amphibian and pdf. Adds images (insert_species_images) to current pdf page. Then returns pdf object. 

    FUNCTION CURRENTLY HARDCODED IMAGE VALUES

    Args:
        amp - Amphibian object
        pdf - pdf object

    Return: 
        pdf - pdf object
    """

    WIDTH = 210
    pdf.ln(20)
    pdf.set_font("OpenSansBold", "", 16)
    pdf.write(5, "Species Images:")
    pdf.ln(75)
    if (amp.has_image_url()):
        pdf.image(f"{amp.image_url_male}",x=10, y=70, w=(WIDTH / 2) - 25, h= 50)
        pdf.image(f"{amp.image_url_female}", x=WIDTH/2, y=70 , w=(WIDTH / 2) - 25, h= 50)
        tcell_width = 60
        tcell_height = 5
        pdf.set_font('OpenSansBold', "", 10)
        pdf.cell(tcell_width, tcell_height, "Male Image", align="C", border=0)
        pdf.cell(tcell_width - 20, tcell_height)
        pdf.cell(tcell_width, tcell_height, "Female Image", align="C", border=0)
    else:
        pdf.image("images/frogsil1.png",x=10, y=70, w=(WIDTH / 2) - 25, h= 50)
        pdf.image("images/frogsil2.png", x=WIDTH/2, y=70 , w=(WIDTH / 2) - 25, h= 50)
        tcell_width = 60
        tcell_height = 5
        pdf.set_font('OpenSansBold', "", 10)
        pdf.cell(tcell_width, tcell_height, "Missing Male Image", align="C", border=0)
        pdf.cell(tcell_width - 20, tcell_height)
        pdf.cell(tcell_width, tcell_height, "Missing Female Image", align="C", border=0)


    return pdf


# create data table
def create_report_page_table(amphibian_data, pdf):

    """
    Takes an instance of Amphibian and pdf. Adds the data in object to current pdf page in tabular format. Then returns pdf object. 

    Args:
        amp - Amphibian object
        pdf - pdf object

    Return: 
        pdf - pdf object
    """


    pdf.ln(20)
    pdf.set_font("OpenSansBold", "", 16)
    pdf.write(5, "Species Data:")
    pdf.ln(10)
    tcell_width = 88
    tcell_height = 5

    pdf.set_font('OpenSansBold', "", 8)

    for key, value in amphibian_data.__dict__.items():
        if (key not in ["position", "image_url_male", "image_url_female"]):
            key = " ".join(key.split("_")).title()
            pdf.set_font('OpenSansBold', "", 8)
            pdf.cell(tcell_width, tcell_height, str(key), align="L", border=1)
            pdf.set_font('OpenSans', "", 8)
            pdf.cell(tcell_width, tcell_height, str(value), align="L", border=1)
            pdf.ln(tcell_height)

    return pdf

# create index
def create_report_index():
    pass


def read_data_source(file_name: str) -> object:
    """
    Read the data_source file and transform it into a pandas dataframe

    Args:
        file_name - String path to file

    Return
        df - Pandas dataframe object
    """

    df = pandas.read_excel(file_name)
    df["comb_name"] = df["Order"] +" " + df["Family"]

    return df

def create_amphibian_list(data_section: object) -> list:
    
    """
    Takes a row of data from the dataframe and extracts values and instantiates an instance of the AmphibianData class

    Args:
        data_section - Pandas dataframe object

    Return:
        amphibian_list - list of amphibian objects
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


def render_toc(pdf, outline):

    """
    Function to render table of contents - taken from example code of FPDF2 documentation

    Args:
        pdf - pdf object
        outline - outline object
    """

    pdf.ln(20)
    pdf.set_font("Helvetica", size=24)
    pdf.underline = False
    pdf.write(5, "Table of contents:")
    pdf.underline = False
    pdf.ln(20)
    pdf.set_font("Courier", size=12)

    for section in outline:
        if section.level < 3:

            link = pdf.add_link()
            pdf.set_link(link, page=section.page_number)
            text = f'{" " * section.level * 2}{section.name}'
            text += (
                f' {"." * (60 - section.level*2 - len(section.name))} {section.page_number}'
            )
            pdf.multi_cell(
                w=pdf.epw,
                h=pdf.font_size,
                txt=text,
                new_x="LMARGIN",
                new_y="NEXT",
                align="C",
                link=link,
            )



if __name__ == "__main__":

    args = sys.argv


    data_source = args[1]
    report_name = args[2].upper()
    report_author = args[3].upper()
    university_name = args[4].upper()
    university_school = args[5].upper()


    print(f"Creating Report: {report_name}.pdf")
    create_report(data_source, report_name, report_author, university_name, university_school)
    print(f"Report Complete: {report_name}.pdf")
