import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def split_data(data, target_column, test_size=0.2, random_state=42):
    """Divide os dados em conjunto de treinamento e teste."""
    X = data.drop(target_column, axis=1)
    y = data[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X

def load_data(file_name):
    """
    Carrega os dados do arquivo CSV.

    :param file_name: Nome do arquivo CSV a ser carregado.
    :return: Dados carregados como um DataFrame do Pandas.
    """
    data = pd.read_csv(file_name)
    return data

def preprocess_numerical_data(data):
    """
    Pre-processa os dados numéricos.

    :param data: Dados a serem pre-processados.
    :return: Dados pre-processados.
    """
    # Verifica se o arquivo data.csv contém dados numéricos
    if data.select_dtypes(include=['int64', 'float64']).empty:
        print("O arquivo data.csv não contém dados numéricos.")
        return None

    # Seleciona as colunas numéricas
    numerical_columns = data.select_dtypes(include=['int64', 'float64']).columns
    numerical_data = data[numerical_columns]

    # Normaliza os dados numéricos
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(numerical_data)

    # Adiciona os dados normalizados de volta à tabela original
    scaled_data = pd.DataFrame(scaled_data, columns=numerical_columns)
    data = pd.concat([data.drop(columns=numerical_columns), scaled_data], axis=1)

    return data

def preprocess_categorical_data(data):
    """
    Pre-processa os dados categóricos.

    :param data: Dados a serem pre-processados.
    :return: Dados pre-processados.
    """
    # Verifica se os dados não são None
    if data is None:
        return None

    # Seleciona as colunas categóricas
    categorical_columns = data.select_dtypes(include=['object']).columns
    categorical_data = data[categorical_columns]

    # Converte os dados categóricos em um formato que o algoritmo de aprendizado de máquina possa entender
    encoder = OneHotEncoder(sparse=False)
    encoded_data = encoder.fit_transform(categorical_data)

    # Adiciona os dados codificados de volta à tabela original
    encoded_data = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(categorical_columns))
    data = pd.concat([data.drop(columns=categorical_columns), encoded_data], axis=1)

    return data

def preprocess_data(data):
    """
    Pre-processa os dados.

    :param data: Dados a serem pre-processados.
    :return: Dados pre-processados.
    """
    # Pre-processa os dados numéricos
    data = preprocess_numerical_data(data)

    # Pre-processa os dados categóricos
    data = preprocess_categorical_data(data)

    return data
