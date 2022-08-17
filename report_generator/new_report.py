"""Setup configuration files and directories for report project.

Will have more info soon

"""

import os
import pathlib

import yaml


def create_new_project() -> None:
    """Create new report project.

    Creates a new report project.

    Examples:
        Example of use.

    """
    HOME_DIR = pathlib.Path.home()

    try:
        settings = get_project_settings()
        dir_path = create_project_directories(HOME_DIR, settings["project_name"])
        settings["dir_path"] = dir_path
        create_project_config_file(settings)
        insert_default_data()

    except FileExistsError as e:
        print(e)


def get_project_settings(settings: dict = None) -> None:
    """CLI to query project setup from user.

    Gets a series of user inputs to set up the config
    files for the project.

    Examples:
        Example of use.

    Args:
        Settings (dict): Settings dict that is provided if user doing set up
                         from the GUI applicaiton rather than the CLI.

    """
    if settings is None:

        print("Creating new project")
        project_name = input("Please enter project name: ")
        report_name = input("Please enter report name: ")
        author_name = input("Please enter author name: ")
        school_name = input("Please enter School name: ")
        uni_name = input("Please enter uni name: ")
        data_set = input("Please enter path to data_set file: ")

        settings = {
            "project_name": project_name,
            "report_name": report_name,
            "author_name": author_name,
            "school_name": school_name,
            "uni_name": uni_name,
            "data_set": data_set,
        }

    return settings


def create_project_directories(home_dir: str, directory_name: str) -> str:
    """Create the project directories.

    Creates directories for project files to be inserted.

    Examples:
        Example of use.

    Args:
        home_dir (str):         String value for the path to the
                                home directory.

        directory_name (str):   String value for the name of the
                                directory that is created.
    Returns:
        dir_path (str):         String value for the path to the
                                project's directory
    """
    dir_path = os.path.join(home_dir, directory_name)

    if check_if_dir_exists(dir_path):
        raise FileExistsError(f"Directory {directory_name} already exists")

    os.makedirs(dir_path)
    os.makedirs(os.path.join(dir_path, "data"))
    os.makedirs(os.path.join(dir_path, "data", "images"))
    os.makedirs(os.path.join(dir_path, "data", "fonts"))
    os.makedirs(os.path.join(dir_path, "data", "locations"))
    os.makedirs(os.path.join(dir_path, "data", "database"))
    os.makedirs(os.path.join(dir_path, "data", "excel_src"))
    os.makedirs(os.path.join(dir_path, "report"))


def check_if_dir_exists(dir_path: str) -> bool:
    """Check if directory exists.

    Args:
        dir_path (str):     String with path to the directory to check
                            if it exists.

    Returns:
        dir_exists (bool):  Boolean value representing whether the directory
                            exists or not.
    """
    dir_exists = os.path.exists(dir_path)
    return dir_exists


def create_project_config_file(settings: dict) -> None:
    """Create the project config file.

    Creates a Yaml file containing all project's
    basic settings.

    Examples:
        Example of use.

    """
    with open("config.yaml", "w") as file:
        yaml.dump(settings, file)


def download_location_data_files() -> None:
    """Download location data files.

    Download location data file from the geocodes website.
    """


def insert_default_data(dir_path: str) -> None:
    """Insert default data.

    Inserts default data files into the data folder by copying files
    from the packages data file.

    Args:
        dir_path (str): String path to the project directory.

    """
    old_image_path = os.path.join(os.getcwd(), "data", "images")
    old_font_path = os.path.join(os.getcwd(), "data", "fonts")
    old_locations_path = os.path.join(os.getcwd(), "data", "locations")

    new_image_path = os.path.join(dir_path, "data", "images")
    new_font_path = os.path.join(dir_path, "data", "fonts")
    new_locations_path = os.path.join(dir_path, "data", "locations")

    for file in os.getdir(old_image_path):
        copy_file(file, new_image_path)

    for file in os.getdir(old_font_path):
        copy_file(file, new_font_path)

    for file in os.getdir(old_locations_path):
        copy_file(file, new_locations_path)


def copy_file(file: str, new_file_path: str) -> None:
    """Copy a file."""


def main():
    """Create new Report.

    Main method for module.

    Example:
        Example use case.
    """
    create_new_project()


if __name__ == "__main__":
    main()
