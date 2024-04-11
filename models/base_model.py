# models/base_model.py

import tensorflow as tf

class BaseModel(tf.keras.Model):
    """
    Classe base para modelos de IA.

    Essa classe define a estrutura básica de um modelo de IA, incluindo a inicialização do modelo, a definição das camadas e a compilação do modelo.

    """

    def __init__(self, input_shape, output_shape, hidden_layers, activation_function):
        """
        Inicializa o modelo de IA.

        :param input_shape: Forma da entrada do modelo.
        :param output_shape: Forma da saída do modelo.
        :param hidden_layers: Lista de forma das camadas ocultas do modelo.
        :param activation_function: Função de ativação das camadas do modelo.
        """
        super(BaseModel, self).__init__()

        # Camada de entrada
        self.input_layer = tf.keras.layers.Input(shape=input_shape)

        # Camadas ocultas
        self.hidden_layers = []
        for hidden_layer in hidden_layers:
            self.hidden_layers.append(tf.keras.layers.Dense(hidden_layer, activation=activation_function))

        # Camada de saída
        self.output_layer = tf.keras.layers.Dense(output_shape)

        # Construção do modelo
        self.model = tf.keras.Sequential([self.input_layer] + self.hidden_layers + [self.output_layer])

        # Compilação do modelo
        self.compile_model()

    def compile_model(self, optimizer='adam', loss='mean_squared_error'):
        """
        Compila o modelo de IA.

        :param optimizer: Otimizador a ser usado no modelo.
        :param loss: Função de perda a ser usada no modelo.
        """
        self.model.compile(optimizer=optimizer, loss=loss)
