# Importing required libraries
import csv
import fireducks.pandas as pd

def check_file(source_file):
    """"Function to read source file and get simple information
    Args:
        source_file (string): Full path where the source file is
    Returns:
        int: Number of rows in file
        int: Number of columns in file
    Raises:
        ExceptionType: None
    """
    
    # Opening CSV file and extracting information
    with open(source_file) as f: data = list(csv.reader(f,delimiter=';'))
    return len(data) - 1, len(data[0])
    
def load_file(source_file):
    """Function to load souce file into pandas dataframe
    Args:
        source_file (string): Full path where the source file is
    Returns:
        dataframe: Dataframe loaded with source data
    Raises:
        ExceptionType: None
    """
    
    # Loading CSV file into pandas dataframe
    dataframe = pd.read_csv(source_file, delimiter=';', on_bad_lines='warn', na_filter=False)
    return dataframe

def df_empty_records(dataframe):
    """Function to clean and replace empty records from pandas dataframe
    Args:
        dataframe (pandas dataframe): Loaded dataframe from source file
    Returns:
        dataframe: Dataframe loaded with cleaned data
    Raises:
        ExceptionType: None
    """
    
    # Cleaning vales to empty records
    dataframe.fillna("null", inplace = True)
    dataframe.replace('N/A', '', inplace=True)
    dataframe.replace('None', '', inplace=True)
    return dataframe

def df_line_content(dataframe):
    """Function to clean and replace characters from text fields in pandas dataframe
    Args:
        dataframe (pandas dataframe): Loaded and transformed dataframe from source file
    Returns:
        dataframe: Dataframe with cleaned and replaced data
    Raises:
        ExceptionType: None
    """
    
    # Cleaning and replacing content in dataframe from extra symbols
    dataframe.replace(r'\\r+|\\n+|\\t+',' ', regex=True, inplace=True)
    dataframe.replace(r'|','', regex=True, inplace=True)
    dataframe.replace(r'§+|Ø+','', regex=True, inplace=True) 
    return dataframe

def df_trim(dataframe):
    """Function to trim values in dataframe
    Args:
        dataframe (pandas dataframe): Loaded dataframe
    Returns:
        dataframe: Dataframe with trimed data
    Raises:
        ExceptionType: None
    """
    dataframe = dataframe.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    return dataframe

def df_columns_underscore(dataframe):
    """Function to replace empty spaces with underscored in dataframe column names
    Args:
        dataframe (pandas dataframe): Loaded dataframe
    Returns:
        dataframe: Dataframe column names with underscores instead of spaces
    Raises:
        ExceptionType: None
    """
    dataframe.columns = map(lambda x : x.replace("-", "_").replace(" ", "_"), dataframe.columns)
    return dataframe