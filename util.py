# Importing required libraries
import os, glob
import yaml
from pathlib import Path

def work_directory():
    """Function to return current working directory
    Args:
        None
    Returns:
        string: Fullpath to current directory
    Raises:
        ExceptionType: None
    """
    
    # get current working directory
    wd = os.getcwd()
    return wd + '/'

def config_file():
    """Function to load configuration file
    Args:
        None
    Returns:
        object: Loaded configuration file object
    Raises:
        ExceptionType: None
    """
    
    # Getting working directory and looking for YAML configuration file
    current = work_directory()   
    conf = glob.glob(current + '/*.YAML', recursive=True)
    
    # Opening and loading configuration file
    with open(conf[0], 'r') as file: 
        configuration = yaml.safe_load(file) 
                    
    return configuration

def get_source_files(source_path, ext):
    """Function to get source files names
    Args:
        source_path (string): Full sourcepath where the source files are
        ext (string): Required extension from filenames
    Returns:
        string: List with source filenames
    Raises:
        ExceptionType: None
    """
    
    # Getting filenames and loading them into list
    files = [f for f in os.listdir(source_path) if f.endswith(ext)]
    return files

def export_dataframe(dataframe, path, file):
    """Function to export dataframe to CSV into specified location
    Args:
        dataframe (pandas dataframe): Final dataframe ready to be exported
        path (string): Fullpath where the output filed will be saved
        file (string): Filename for exported CSV
    Returns:
        None
    Raises:
        ExceptionType: None
    """
    
    # Exporting pandas dataframe to CSV in defined exported folder
    dataframe.to_csv(path + file, encoding='utf-8', index=False)