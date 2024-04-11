#!/bin/bash

# Instalar o Python
sudo apt-get update
sudo apt-get install python3.9

# Instalar o pip
sudo apt-get install python3-pip

# Instalar todas as bibliotecas necessárias
sudo pip3 install -r requirements.txt

# Configurar o ambiente, se necessário
# Exemplo: Definir variáveis de ambiente, configurar permissões de arquivos, etc.

# Executar o main.py
python3.9 autonoma.py