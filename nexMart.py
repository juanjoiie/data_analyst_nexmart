# Importing required libraries
import dataManipulation, solutionLogs, util, nexMartAnalysis

# Loading current working directory and configuration file
wd = util.work_directory()
config = util.config_file()

def get_full_path(work_dir, config_param):
    """Function to return full path
    Args:
        work_dir (string): Current working directory
        config_param (string): Configuration file location 
    Returns:
        string: Concatenation of 2 parameters
    Raises:
        ExceptionType: None
    """
    
    full_path = work_dir + config_param
    return full_path
    
def load_product_catalog(path, file, logger):
    """"Function to load source data
    Args:
        path (string): Full path where the source file is
        file (string): Source filename with extension
        logger(object): Object to log details into logfile
    Returns:
        dataframe: Dataframe loaded with source data
    Raises:
        ExceptionType: None
    """
    
    logger.debug("Filename: " + file)
    
    # Checking .CSV files in source folder
    src_row, src_col = dataManipulation.check_file(path + file)
    logger.debug("Columns in source: " + str(src_col))
    logger.debug("Records in source: " + str(src_row))
    
    # Loading source files as pandas dataframes
    df = dataManipulation.load_file(path + file)
    logger.debug("Headers : " + ','.join(map(str, df.columns.tolist())))
    logger.debug("Columns in dataframe: " + str(len(df.columns)))
    logger.debug("Records in dataframe: " + str(len(df)))
    return df

def pipeline_product_catalog(dataframe):
    """"Function the normalize and clean source dataframe (pipeline)
    Args:
        dataframe (pandas dataframe): Loaded dataframe from source file
    Returns:
        dataframe: Transformed and cleaned dataframe
    Raises:
        ExceptionType: None
    """
    
    # Normalizing, transforming and cleaning pandas dataframe
    df_filled = dataManipulation.df_empty_records(dataframe)
    df_clean_text = dataManipulation.df_line_content(df_filled)
    df_final = dataManipulation.df_trim(df_clean_text)
    
    return df_final

def analysis_product_catalog(dataframe, sourcefilename, logger):
    """"Function to load transformed and exported data for analysis purposes
    Args:
        dataframe (pandas dataframe): Transformed and exported dataframe
        sourcefilename (string): Source filename with extension to get required data
        logger(object): Object to log details into logfile
    Returns:
        dataframe: Adapted dataframe for analysis
    Raises:
        ExceptionType: None
    """
    
    # Getting filenames without extension
    table_name = nexMartAnalysis.df_check_table(sourcefilename)
    # Validating if files exist for analysis
    if table_name != 'None':
        logger.debug("Table: " + table_name)
        # Filtering dataframe with valid primery keys only and transforming headers name
        df_clean = nexMartAnalysis.df_clean_tables(dataframe, table_name)
        df_final = dataManipulation.df_columns_underscore(df_clean)
    
        logger.debug("Headers : " + ','.join(map(str, df_final.columns.tolist())))
        logger.debug("Columns in dataframe: " + str(len(df_final.columns)))
        logger.debug("Records in dataframe: " + str(len(df_final)))
        
        return df_final
    
    else:
        logger.debug("THERE IS NO ANALYSIS FOR THIS FILE")
        return dataframe

# Main code to trigger the code (pipeline)
def main():    
    try:
        # Defining paths
        input_path = get_full_path(wd, config['INPUT']['pathname'])
        output_path = get_full_path(wd, config['OUTPUT']['pathname'])
        logging_path = get_full_path(wd, config['LOG']['pathname'] + config['LOG']['filename'])
        # Defining logs
        logger = solutionLogs.set_logger(logging_path)
        # Reading files from source folder
        sources_files = util.get_source_files(input_path, config['INPUT']['extension'])
        # Looping into every file within source folder
        for filename in sources_files:
            # Loading source files into Dataframes
            df_raw = load_product_catalog(input_path, filename, logger)
            
            # Cleaning and exporting transformed (cleaned) data
            final_df = pipeline_product_catalog(df_raw)             
            util.export_dataframe(final_df, output_path, 'clean_' + filename)           
            print("Exported file: " + output_path + 'clean_' + filename)
            logger.debug("Exported filename: " + output_path + 'clean_' + filename)
            
            # Creating and exporting cleaned data for analysis purposes
            analysis_df = analysis_product_catalog(final_df, filename, logger)
            util.export_dataframe(analysis_df, output_path, 'analysis_' + filename) 
            print("Exported analysis file: " +output_path + 'analysis_' + filename)
            logger.debug("Exported filename: " + output_path + 'analysis_' + filename)
        print("Logs: " + logging_path)
        print("Finished")
    except Exception as error:
        print("An exception occurred:", error)
    
# Excecuting main script    
if __name__ == '__main__':
    main()