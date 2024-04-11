def evaluate_model(model, X_test, y_test):
    """
    Avalia o modelo usando os dados de teste.
    :param model: Modelo a ser avaliado.
    :param X_test: Dados de teste.
    :param y_test: Marcadores de teste.
    :return: Métricas de avaliação do modelo.
    """
    # Avalia o modelo
    metrics = model.evaluate(X_test, y_test)

    # Imprime as métricas de avaliação
    print("Métricas de avaliação: ", metrics)

    return metrics