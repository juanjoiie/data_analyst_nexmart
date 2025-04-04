# Importing required libraries
import fireducks.pandas as pd
import numpy as np
import util

# Loading configuration data to read defined data for analysis purposes
config = util.config_file()
tables = config['ANALYSIS']['tables']
table = [item.lower() for item in tables]

def df_check_table(filename):
    """"Function to read source filename
    Args:
        filename (string): CSV filename
    Returns:
        string: Validated filename if exists
    Raises:
        ExceptionType: None
    """
    
    # Check if filename exists in list from configuration file
    final_name = filename.rpartition('.')[0].lower()
    if final_name in table:          
        return final_name
    else:
        return "None"

def df_clean_tables(dataframe, tablename):
    """"Function to drop empty records and trim their primary key based on specific columns
    Args:
        dataframe (pandas dataframe): Loaded dataframe from cleaned source data
        tablename (string): Original filename without extension (from configuration file)
    Returns:
        dataframe: Final dataframe with valid records ready to be analysed
    Raises:
        ExceptionType: None
    """
    
    # Get column names from pandas dataframe
    df=dataframe.mask(dataframe == '')
    columns = [item for item in df.columns]
    # Drop empty values and trim specific fields based on the analysis
    if 'Manufacturernumber' in columns:
        df.dropna(subset=['Manufacturernumber'], inplace=True)
        df['Manufacturernumber'] = df['Manufacturernumber'].apply(lambda x: x.replace(' ', ''))
        df['Manufacturernumber'] = df['Manufacturernumber'].str.strip()
    if 'Articlenumber' in columns:
        df.dropna(subset=['Articlenumber'], inplace=True)
        df['Articlenumber'] = df['Articlenumber'].apply(lambda x: x.replace(' ', ''))
        df['Articlenumber'] = df['Articlenumber'].str.strip()

    return df