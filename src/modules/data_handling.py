import pandas as pd
import numpy as np

def load_data(file_path):
    """
    Carrega os dados de um arquivo CSV e retorna um DataFrame do Pandas contendo os dados.
    :param file_path: Caminho para o arquivo CSV.
    :return: DataFrame do Pandas contendo os dados.
    """
    data = pd.read_csv(file_path)

    # Tratamento de dados ausentes
    data.fillna(data.mean(), inplace=True)

    return data

def preprocess_data(data):
    """
    Preprocessa os dados para serem usados em um modelo de machine learning.
    :param data: DataFrame do Pandas contendo os dados.
    :return: DataFrame do Pandas preprocessado.
    """
    # Normalização dos dados
    data_normalized = (data - data.min()) / (data.max() - data.min())

    # Separação dos dados em features e marcadores
    X = data_normalized.drop('marcador', axis=1)
    y = data_normalized['marcador']

    return X, y