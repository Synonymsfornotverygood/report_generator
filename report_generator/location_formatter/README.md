# Location Formatter

## Requirements

- Python3
- Pandas
- openpyexcel

<br>


## Installation

### In Code

Use git pull or download files from the GitLab repository.

Place the folder's contents in the relevant place in the project directory.

Install requirements.txt

    pip install requirements.txt

### Independent Package

Use git pull or download files and extract into chosen directory

    mkdir {{chosen_dir_name}}
    cd {{chosen_dir_name}}
    git pull {{link to package}}

Create virtual environment:

    python3 -m venv location-venv

Activate virtual environment:

    source location-venv/bin/activate

*If this does not work check how to activate the virtual environment in the OS you are using*

Install requirements.txt

    pip install requirements.txt

If there is no 'location.json' file in directory create it by running

    python3 setup/locations_setup.py

<br>

## Example Use

### In Project Code

In project code use the following:

        import pandas as pd
        from location_updater import update_location


        df = pandas.read_excel(file_name)
        updated_df = update_location(df)

### Independent/Commandline


Open directory with package in the terminal

Activate the virtual environment

        source location-venv/bin/activate

Run program from the command line

        python3 main.py {{input_file_path}} {{output_file_path}}


From examples folder:

        python3 main.py example/example_dataset_2_10000.xlsx example/updated.xlsx


## Output

The formatted section should look like the following format:

    {continent}-{country}-{region}/{continent}-{country}-{region}/etc


In dataset example

    South America--Chiloe/South America--Chonos Island

Neither of the examples has a recognisable country string so we are left with blank strings for the country section.


## Sources

wikipedia.org
geonames.org


## Using Geonames

### What
Geonames has a database of 11 million placenames that can be downloaded. It has a free dataset available. To search for placenames that are not a country or a continent or a region we can use this database to get the best approximation of the actual location.

### Why

This follows on from our decision to try and implement location search ourselves. The primary issue is that as the dataset scales using a service like the google maps api (even though we would only maybe need to run it once) would place us over their free api limits.

Even accounting for just countries and continents the unknown regions are


append to start of split file names
'geoname_id\tplace_name\tascii_name\talternate_names\tlatitude\tlongitude\tfeature_class\tfeature_code\tcountry_code\tcc2\tadmin1_code\tadmin2_code\tadmin3_code\tadmin4_code\tpopulation_info\televation\tdem\ttimezone\tmodification\n'
"""
