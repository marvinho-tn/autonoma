import pandas as pd
import numpy as np

def generate_real_data(n_rows=1000):
    """
    Gera dados reais para o arquivo data.csv.
    """
    # Gera dados para a coluna feature
    feature = np.random.normal(size=n_rows)

    # Gera dados para a coluna target como uma função da coluna feature
    target = feature * 2 + np.random.normal(size=n_rows)

    # Cria o DataFrame com as colunas feature e target
    data = pd.DataFrame({'feature': feature, 'target': target})

    return data

def save_data_to_csv(data, file_name='data.csv'):
    """
    Salva os dados no arquivo data.csv.
    """
    data.to_csv(file_name, index=False)

def load_data_from_csv(file_name='data.csv'):
    """
    Carrega os dados do arquivo data.csv.
    """
    data = pd.read_csv(file_name)
    return data

def main(args):
    """
    Gera os dados, salva-os no arquivo data.csv e carrega-os novamente.
    """
    data = generate_real_data()
    save_data_to_csv(data)
    loaded_data = load_data_from_csv()
    print(loaded_data.head())
