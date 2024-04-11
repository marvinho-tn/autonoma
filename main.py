import argparse
import logging
import sys

import numpy as np
import pandas as pd
import tensorflow as tf

from utils import config
from data.preprocessing import load_data, preprocess_data, split_data
from models.model import build_model
from utils.logger import setup_logger

def main(args):
    # Carrega os dados
    data = load_data(args.data_file)

    # Pre-processa os dados
    data = preprocess_data(data)

    # Divide os dados em conjuntos de treino e teste
    X_train, X_test, y_train, y_test = split_data(data, args.target_column)

    # Verifica se os dados foram divididos corretamente
    if X_train is None or X_test is None or y_train is None or y_test is None:
        print("Não foi possível dividir os dados em conjuntos de treino e teste.")
        return

    # Constroi o modelo
    model = build_model(X_train.shape[1:], args.hidden_layers)

    # Compila o modelo
    model.compile(loss=args.loss, optimizer=args.optimizer, metrics=['accuracy'])

    # Treina o modelo
    model.fit(X_train, y_train, epochs=args.epochs, batch_size=args.batch_size, validation_data=(X_test, y_test))

    # Avalia o modelo
    _, accuracy = model.evaluate(X_test, y_test)
    print(f"Acurácia: {accuracy}")

    if __name__ == "__main__":
        # Configura o logger
        logger = setup_logger(config.APP_NAME, args.log_file)

        # Configura o parser de argumentos
        parser = argparse.ArgumentParser(description="Treina um modelo de regressão linear com dados fornecidos.")
        parser.add_argument("--data_file", type=str, required=True, help="Nome do arquivo CSV contendo os dados.")
        parser.add_argument("--target_column", type=str, required=True, help="Nome da coluna alvo.")
        parser.add_argument("--hidden_layers", type=int, nargs="+", help="Número de camadas ocultas do modelo.")
        parser.add_argument("--optimizer", type=str, default="adam", help="Optimizador a ser usado no treinamento do modelo.")
        parser.add_argument("--loss", type=str, default="mean_squared_error", help="Função de perda a ser usada no treinamento do modelo.")
        parser.add_argument("--epochs", type=int, default=100, help="Número de épocas de treinamento do modelo.")
        parser.add_argument("--batch_size", type=int, default=32, help="Tamanho do lote de treinamento do modelo.")
        args = parser.parse_args()

    # Inicia a execução do programa
    main(args)
