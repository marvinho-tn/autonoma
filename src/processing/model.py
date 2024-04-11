import tensorflow as tf

def build_model():
    # Construir e compilar o modelo de IA
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(10,)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def train_model(model, X_train, y_train):
    # Treinar o modelo com os dados de treinamento
    model.fit(X_train, y_train, epochs=10, batch_size=32)