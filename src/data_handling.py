import numpy as np

def load_data(file_path):
    # Carregar dados do arquivo
    data = np.loadtxt(file_path)
    return data

def preprocess_data(data):
    # Pré-processamento dos dados
    # Normalização, tratamento de missing values, etc.
    return data