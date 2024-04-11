# data/loader.py

import pandas as pd

def load_data(file_path):
    """
    Carrega os dados de um arquivo CSV e retorna um DataFrame do Pandas.

    :param file_path: Caminho do arquivo CSV a ser carregado.
    :return: DataFrame do Pandas contendo os dados.
    """
    data = pd.read_csv(file_path)
    return data
