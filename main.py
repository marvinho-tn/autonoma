# main.py

import argparse
import logging
import sys

from utils import setup_logger
from data_preprocessing import load_data, preprocess_data, split_data
from model_training import build_model, compile_model, train_model
from model_evaluation import evaluate_model, predict, calculate_metrics

def main(args):
    """Executa o projeto Autonoma."""

    # Configuração do logger
    logger = setup_logger(args.log_file)

    # Carregamento dos dados
    logger.info("Carregando dados...")
    data = load_data(args.data_file)

    # Pré-processamento dos dados
    logger.info("Pré-processando dados...")
    data = preprocess_data(data)

    # Divisão dos dados em treinamento e teste
    logger.info("Dividindo dados em treinamento e teste...")
    X_train, X_test, y_train, y_test = split_data(data, args.target_column)

    # Construção do modelo de IA
    logger.info("Construindo modelo de IA...")
    model = build_model(X_train.shape[1:], args.hidden_layers)

    # Compilação do modelo de IA
    logger.info("Compilando modelo de IA...")
    model = compile_model(model, args.optimizer, args.loss)

    # Treinamento do modelo de IA
    logger.info("Treinando modelo de IA...")
    model = train_model(model, X_train, y_train, args.epochs, args.batch_size)

    # Avaliação do desempenho do modelo de IA
    logger.info("Avaliando desempenho do modelo de IA...")
    loss, accuracy = evaluate_model(model, X_test, y_test)
    logger.info(f"Loss: {loss:.4f}, Accuracy: {accuracy:.4f}")

    # Realização de previsões com o modelo de IA
    logger.info("Realizando previsões com o modelo de IA...")
    predictions = predict(model, X_test)

    # Cálculo das métricas de desempenho do modelo de IA
    logger.info("Calculando métricas de desempenho do modelo de IA...")
    metrics = calculate_metrics(y_test, predictions)

    logger.info("Projeto Autonoma concluído com sucesso!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Projeto Autonoma")

    parser.add_argument("--data_file", type=str, required=True,
                        help="Caminho do arquivo de dados")

    parser.add_argument("--target_column", type=str, required=True,
                        help="Nome da coluna alvo")

    parser.add_argument("--log_file", type=str, required=True,
                        help="Caminho do arquivo de log")

    parser.add_argument("--hidden_layers", type=int, nargs="+",
                        help="Número de unidades nas camadas ocultas do modelo de IA")

    parser.add_argument("--optimizer", type=str, default="adam",
                        help="Otimizador usado no modelo de IA")

    parser.add_argument("--loss", type=str, default="mean_squared_error",
                        help="Função de perda usada no modelo de IA")

    parser.add_argument("--epochs", type=int, default=10,
                        help="Número de épocas de treinamento do modelo de IA")

    parser.add_argument("--batch_size", type=int, default=32,
                        help="Tamanho do lote de treinamento do modelo de IA")

    args = parser.parse_args()

    main(args)
