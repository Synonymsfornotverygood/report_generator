import os
import sys
import time

from loguru import logger

sys.path.append(
    "/home/cush/dev/dissertation/project_applications/report_generator/report_generator_cli/application"
)
import create_report


def create_5000_page_report():
    startTime = time.time()
    data_source = os.getcwd() + "/examples/" + "example_dataset_1_5000.xlsx"
    report_name = "Example 5000".upper()
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


def create_10000_page_report():
    startTime = time.time()
    data_source = os.getcwd() + "/examples/" + "example_dataset_2_10000.xlsx"
    report_name = "Example 10000 (Compact 2)".upper()
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


def create_50000_page_report():
    startTime = time.time()
    data_source = os.getcwd() + "/examples/" + "example_dataset_3_50000.xlsx"
    report_name = "Example 50000 (Compact 2)".upper()
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


def create_100000_page_report():
    startTime = time.time()
    data_source = os.getcwd() + "/examples/" + "example_dataset_4_100000.xlsx"
    report_name = "Example 100000 (Compact 2)".upper()
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


def create_500000_page_report():
    startTime = time.time()
    data_source = os.getcwd() + "/examples/" + "example_dataset_5_500000.xlsx"
    report_name = "Example 500000 (Compact 2)".upper()
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


if __name__ == "__main__":

    logger.add("examples/test.log", rotation="500 MB")

    # create_5000_page_report()
    create_10000_page_report()
    create_50000_page_report()
    create_100000_page_report()
    create_500000_page_report()
