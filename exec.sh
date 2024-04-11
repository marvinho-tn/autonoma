#!/bin/bash

# Instalar o Python
sudo apt-get update
sudo apt-get install python3.9

# Instalar o pip
sudo apt-get install python3-pip

# Checar instalaçao dos modulos
pip freeze

# Instalar todas as bibliotecas necessárias
sudo pip3 install -r requirements.txt

# Checar se o ambiente está preparado para executar os modulos
which python

# Configurar o ambiente, se necessário
# Exemplo: Definir variáveis de ambiente, configurar permissões de arquivos, etc.

# Executar o automa.py
python3.9 src/automa.py