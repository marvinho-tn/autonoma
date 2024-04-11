# utils.py

import logging

def setup_logger(log_file, level=logging.INFO):
    """Configura o logger do projeto."""
    logger = logging.getLogger()
    logger.setLevel(level)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

def load_data(file_path):
    """Carrega os dados de um arquivo."""
    # Implemente a lógica para carregar os dados do arquivo especificado
    pass

def save_model(model, model_path):
    """Salva o modelo treinado em um arquivo."""
    # Implemente a lógica para salvar o modelo treinado no arquivo especificado
    pass

def load_model(model_path):
    """Carrega um modelo treinado de um arquivo."""
    # Implemente a lógica para carregar um modelo treinado do arquivo especificado
    pass

def preprocess_data(data):
    """Realiza o pré-processamento dos dados."""
    # Implemente a lógica para pré-processar os dados, como normalização ou codificação
    pass

def generate_report(metrics):
    """Gera um relatório com as métricas de avaliação do modelo."""
    # Implemente a lógica para gerar um relatório com as métricas de avaliação do modelo
    pass
