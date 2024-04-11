# Implementação da camada de estatística

import numpy as np

def calculate_mean(data):
    # Calcular a média dos dados
    return np.mean(data)

def calculate_std(data):
    # Calcular o desvio padrão dos dados
    return np.std(data)

def calculate_correlation(data1, data2):
    # Calcular a correlação entre dois conjuntos de dados
    return np.corrcoef(data1, data2)[0, 1]