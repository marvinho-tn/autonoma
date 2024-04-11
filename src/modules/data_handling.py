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
    # Inicializar a variável X
    X = pd.DataFrame()

    # Verificar se as colunas relevantes são numéricas
    numeric_columns = ['sensor1', 'sensor2', 'sensor3', 'latitude', 'longitude', 'acao', 'recompensa']
    if all(data[col].dtype == 'float64' for col in numeric_columns):
        # Converter as colunas relevantes em valores numéricos
        data[numeric_columns] = data[numeric_columns].apply(pd.to_numeric, errors='coerce')

        # Normalizar os dados
        data_normalized = (data[numeric_columns] - data[numeric_columns].min()) / (data[numeric_columns].max() - data[numeric_columns].min())

        # Verificar se a coluna 'marcador' existe antes de tentar removê-la
        if 'marcador' in data.columns:
            X = data_normalized.drop('marcador', axis=1)
        else:
            X = data_normalized
    else:
        print("Algumas colunas não puderam ser convertidas em valores numéricos.")

    return X