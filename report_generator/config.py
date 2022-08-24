"""Module to load configuration data.

Functions:
    load_config:    Loads the configuration file
"""
import yaml


def load_config() -> dict:
    config = None
    try:
        with open("config.yaml", "r") as file:
            config = yaml.load(file, Loader=yaml.loader.SafeLoader)
        return config
    except FileNotFoundError:
        return config
