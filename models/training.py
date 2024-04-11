# model_training.py

import tensorflow as tf

def build_model(input_shape, hidden_layers, activation_function='relu'):
    """Constrói o modelo de IA."""
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Input(shape=input_shape))
    
    for units in hidden_layers:
        model.add(tf.keras.layers.Dense(units, activation=activation_function))
    
    model.add(tf.keras.layers.Dense(1))  # Saída
    
    return model

def compile_model(model, optimizer='adam', loss='mean_squared_error'):
    """Compila o modelo de IA."""
    model.compile(optimizer=optimizer, loss=loss)
    
    return model

def train_model(model, X_train, y_train, epochs=10, batch_size=32):
    """Treina o modelo de IA."""
    model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)
    
    return model
