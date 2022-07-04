
# Library Imports
from fpdf import FPDF, TitleStyle, errors, TextMode
from fpdf.outline import build_outline, outline_as_str
from fpdf.syntax import iobj_ref as pdf_ref
import pandas
import os


# Local Imports
from amphibian import AmphibianData






# Create report

def create_report(data_source, report_name, report_author, university_name, university_school):

    ds = read_data_source(data_source)
    pdf = FPDF()
    pdf.add_font("OpenSans", fname="fonts/OpenSans-VariableFont_wdth,wght.ttf")
    pdf.add_font("OpenSansBold", fname="fonts/static/OpenSans/OpenSans-Bold.ttf")
    pdf = create_title_page(report_name, report_author, university_name, university_school, pdf)
    pdf= create_contents_page(pdf)
    pdf = create_report_order_sections(ds, pdf)
    pdf.output(f"{'_'.join(report_name.split(' '))}.pdf")

# create title page
# #e30613
def create_title_page(report_name, report_author, university_name, university_school, pdf) -> object:
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


def create_contents_page(pdf):
    pdf.add_page()
    pdf.set_text_color(0,0,0)
    pdf.start_section(name="Table Of Contents", level=0)
    pdf.insert_toc_placeholder(render_toc, 9)
    return pdf


def create_report_order_sections(ds, pdf):

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

def create_report_family_sections(section_list, pdf):
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

def create_report_genus_sections(section_list, pdf):
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
    amp_list = create_amphibian_list(section)
    amp_list = sorted(amp_list, key=lambda a: a.species)
    amp_list[0].image_url_male = "images/f1.jpg"
    amp_list[0].image_url_female = "images/f2.jpg"
    for amp in amp_list:
        pdf = create_report_section_page(amp, pdf)
    return pdf

# create page
def create_report_section_page(amp, pdf):
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


def render_toc(pdf, outline):
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

    data_source = "AMPH PILOT DATASET_V5_25.June.2022.xlsx"
    report_name = "Test Report".upper()
    report_author = "Daniel Pincheira-Donoso".upper()
    university_name = "Queen's University Belfast".upper()
    university_school = "School Of Biological Sciences".upper()



    create_report(data_source, report_name, report_author, university_name, university_school)