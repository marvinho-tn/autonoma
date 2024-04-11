# utils/logger.py

import logging

def setup_logger(logger_name, log_file, level=logging.INFO):
    """
    Configura o logger do projeto.

    :param logger_name: Nome do logger.
    :param log_file: Caminho do arquivo de log.
    :param level: Nível de log.
    """
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(asctime)s : %(message)s')
    fileHandler = logging.FileHandler(log_file, mode='w')
    fileHandler.setFormatter(formatter)

    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    l.setLevel(level)
    l.addHandler(fileHandler)
    l.addHandler(streamHandler)
