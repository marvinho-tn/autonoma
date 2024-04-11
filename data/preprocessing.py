# data_preprocessing.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def load_data(file_path):
    """Carrega os dados de um arquivo."""
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    preprocess_numerical_data(data)
    preprocess_categorical_data(data)
    return data

def preprocess_numerical_data(data, scaler=StandardScaler()):
    """Realiza o pré-processamento de dados numéricos."""
    numerical_columns = data.select_dtypes(include=['int64', 'float64']).columns
    numerical_data = data[numerical_columns]
    scaled_data = scaler.fit_transform(numerical_data)
    data[numerical_columns] = scaled_data
    return data

def preprocess_categorical_data(data, encoder=OneHotEncoder()):
    """Realiza o pré-processamento de dados categóricos."""
    categorical_columns = data.select_dtypes(include=['object']).columns
    categorical_data = data[categorical_columns]
    encoded_data = encoder.fit_transform(categorical_data)
    encoded_data = np.hstack(encoded_data.toarray())
    data[categorical_columns] = encoded_data
    return data

def split_data(data, target_column, test_size=0.2, random_state=42):
    """Divide os dados em conjunto de treinamento e teste."""
    X = data.drop(target_column, axis=1)
    y = data[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X
