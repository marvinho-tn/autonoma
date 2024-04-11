# config.py

# Configurações gerais
APP_NAME = "Autonoma"
VERSION = "3.0.0"

# Configurações de dados
DATA_DIR = "data"
TRAIN_DATA_FILE = "train.csv"
TEST_DATA_FILE = "test.csv"

# Configurações de modelo
MODEL_DIR = "models"
MODEL_NAME = "autonoma_model"
MODEL_TYPE = "sequential"
HIDDEN_LAYERS = [64, 32]
ACTIVATION_FUNCTION = "relu"
LOSS_FUNCTION = "mean_squared_error"
OPTIMIZER = "adam"
BATCH_SIZE = 32
EPOCHS = 10

# Configurações de avaliação
EVAL_DIR = "evaluation"
EVAL_METRICS = ["loss", "accuracy"]

# Configurações de logging
LOGGING_DIR = "logs"
LOGGING_LEVEL = "INFO"

# Configurações de outros
RANDOM_SEED = 42
