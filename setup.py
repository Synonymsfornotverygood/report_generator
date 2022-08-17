"""Python setup file to organise package setup."""


import os

from setuptools import find_packages, setup

setup(
    name="report-generator",
    version="0.0.1",
    description="Generate reports from amphibian info dataset",
    long_description=open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")
    ).read(),
    long_description_content_type="text/markdown",
    author="Ciaran Cushnahan",
    packages=find_packages(exclude=["report_generator.tests"]),
    install_requires=[
        "setuptools",
        "docopt",
        "pyQt5",
        "pandas",
        "openpyxl",
        "black",
        "loguru",
        "fpdf2",
    ],
    entry_points={
        "console_scripts": [
            "report-generator = report_generator.app:main",
        ]
    },
)
