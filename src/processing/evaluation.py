def evaluate_model(model, X_test, y_test):
    # Avaliar o desempenho do modelo
    loss = model.evaluate(X_test, y_test)
    return loss