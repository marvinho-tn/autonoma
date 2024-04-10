# Configurar o Python para instalar pacotes

## Instalar o Python

- Baixe e instale a versão mais recente do site oficial do Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)

## Instalar o pip

- Instale o pip executando o seguinte comando no terminal ou prompt de comando:

python -m ensurepip --upgrade


## Criar um ambiente virtual

- Crie um ambiente virtual executando o seguinte comando no terminal ou prompt de comando:

python -m venv nome_do_ambiente


Substitua "nome\_do\_ambiente" pelo nome desejado para o ambiente virtual.

## Ativar o ambiente virtual

- Ative o ambiente virtual executando o seguinte comando no terminal ou prompt de comando:

- **Windows**:

  ```
  nome_do_ambiente\Scripts\activate
  ```

- **Linux/Mac**:

  ```
  source nome_do_ambiente/bin/activate
  ```

## Instalar os pacotes

- Instale os pacotes usando o pip. Por exemplo, para instalar o TensorFlow, execute o seguinte comando no terminal ou prompt de comando:

pip install tensorflow

Para instalar outros pacotes, substitua "tensorflow" pelo nome do pacote desejado.

## Desativar o ambiente virtual

- Desative o ambiente virtual executando o seguinte comando no terminal ou prompt de comando:

deactivate