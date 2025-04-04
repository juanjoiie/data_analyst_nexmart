# Importing required librariesf
from datetime import datetime
import logging

def set_logger(log_filename):
    """"Function to create logs and write them in logfile
    Args:
        log_filename (string): full path of logfile
    Returns:
        object: logger object to register code statements
    Raises:
        ExceptionType: None
    """
    
    # Define logs levels
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create a file handler that logs even debug messages
    fh = logging.FileHandler(log_filename + '_' + f'{datetime.now():%Y-%m-%d_%H-%M-%S}')
    fh.setLevel(logging.DEBUG)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # Add the handler to the logger and return object
    logger.addHandler(fh)
    return logger