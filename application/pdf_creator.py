from fileinput import filename
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEnginePage
import os


def create_pdf(path_to_html: str, pdf_filename: str) -> None:

    app = QApplication(sys.argv)
    page = QWebEnginePage()
    ps = QPageSize(QPageSize.A4)
    layout = QPageLayout(ps, QPageLayout.Portrait, QMarginsF())

    def handle_create_pdf_finished(pdf_filename: str, process_status: str) -> None:
        print(f"Finished {pdf_filename}: ", process_status)
        QApplication.quit()

    def handle_load_finished(process_status: str) -> None:
        if process_status:
            page.printToPdf(pdf_filename, pageLayout=layout)
        else:
            print("Failed")
            QApplication.quit()

    page.pdfPrintingFinished.connect(handle_create_pdf_finished)
    page.loadFinished.connect(handle_load_finished)
    page.load(QUrl.fromLocalFile(path_to_html))
    app.exec()

def get_file_path(file_name):
    current_dir = os.path.dirname(os.getcwd())
    file_str = f"report_generator/{file_name}"
    file_path = os.path.join(current_dir, file_str)
    return file_path

file_path1 = get_file_path("report.html")
file_path2 = get_file_path("test.html")

create_pdf(file_path1, "brokenreport.pdf")
# create_pdf(file_path2, "test.pdf")






