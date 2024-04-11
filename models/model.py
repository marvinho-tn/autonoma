import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def build_model(input_shape, hidden_layers):
    """
    Constrói um modelo de rede neural com camadas densas.

    :param input_shape: Formato da entrada.
    :param hidden_layers: Lista com o número de neurônios em cada camada oculta.
    :return: Modelo construído.
    """
    model = Sequential()

    # Adiciona a camada de entrada
    model.add(Dense(hidden_layers[0], input_shape=input_shape, activation='relu'))

    # Adiciona as camadas ocultas
    for neurons in hidden_layers[1:]:
        model.add(Dense(neurons, activation='relu'))

    # Adiciona a camada de saída
    model.add(Dense(1, activation='sigmoid'))

    return model
