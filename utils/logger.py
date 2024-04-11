# utils/logger.py

import logging

def setup_logger(logger_name, log_file):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s : %(message)s')
    fileHandler = logging.FileHandler(log_file, mode='w')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger
