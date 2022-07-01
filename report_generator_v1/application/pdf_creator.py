"""

Functions to take a html_file_path and a pdf_file_path and load and convert the html_file into a pdf in the specified location


"""



from fileinput import filename
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEnginePage
import os


def create_pdf(path_to_html: str, pdf_filename: str) -> None:

    """
    Open html_file and convert it to pdf_file
    """


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
    return "Completed"

def get_file_path(file_name):

    """
    Take a file_name and return the absolute path
    """
    current_dir = os.path.dirname(os.getcwd())
    file_str = f"report_generator/{file_name}"
    file_path = os.path.join(current_dir, file_str)
    return file_path

if __name__ == "__main__":
    args = sys.argv
    # print(args)
    message = create_pdf(args[1], args[2])
    print(f"{message}: {args[2]}")





