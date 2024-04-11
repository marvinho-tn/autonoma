from modules.data_handling import load_data, preprocess_data
from modules.model_training import build_model, train_model
from modules.model_evaluation import evaluate_model

# Carregar e pré-processar os dados
data = load_data('data.csv')
preprocessed_data = preprocess_data(data)

# Dividir dados em treinamento e teste
X_train, y_train = preprocessed_data[:80, :-1], preprocessed_data[:80, -1]
X_test, y_test = preprocessed_data[80:, :-1], preprocessed_data[80:, -1]

# Construir e treinar o modelo
model = build_model()
train_model(model, X_train, y_train)

# Avaliar o modelo
loss = evaluate_model(model, X_test, y_test)
print(f"Loss: {loss}")