# Instalação do Python no macOS

## Verifique se o Python já está instalado no seu macOS

Abra o terminal e digite `python --version` ou `python3 --version`. Se o Python estiver instalado, ele exibirá a versão instalada.

## Instale o Anaconda Python

Anaconda é uma distribuição do Python que inclui muitas bibliotecas e ferramentas úteis para ciência de dados e aprendizado de máquina. Siga as etapas abaixo para instalar o Anaconda Python:

1. Acesse o site do Anaconda e baixe a versão mais recente do Anaconda Python para macOS: [https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual)
2. Após o download, abra o instalador e siga as instruções para instalar o Anaconda Python.
3. Depois de instalar o Anaconda Python, abra o terminal e digite `conda --version` para verificar se o Anaconda foi instalado corretamente.

## Crie um ambiente virtual do Python

É recomendável criar um ambiente virtual do Python para cada projeto que você trabalhar. Isso ajuda a manter as dependências separadas entre os projetos. Siga as etapas abaixo para criar um ambiente virtual do Python:

1. Abra o terminal e digite `conda create --name nome_do_ambiente python=3.x` (substitua `nome_do_ambiente` pelo nome do seu ambiente e `3.x` pela versão do Python que você deseja instalar).
2. Ative o ambiente virtual digitando `conda activate nome_do_ambiente`.

## Instale as bibliotecas necessárias

Depois de ativar o ambiente virtual, você pode instalar as bibliotecas necessárias usando o pip ou o conda. Por exemplo, para instalar o TensorFlow, digite `pip install tensorflow` ou `conda install tensorflow`.

## Verifique se as bibliotecas foram instaladas corretamente

Depois de instalar as bibliotecas, você pode verificar se elas foram instaladas corretamente digitando `python -c "import biblioteca"` no terminal. Por exemplo, para verificar se o TensorFlow foi instalado corretamente, digite `python -c "import tensorflow"`. Se a biblioteca for importada sem erros, ela foi instalada corretamente.

Referências:
[1] <https://www.tensorflow.org/learn?hl=pt-br>
[2] <https://www.tensorflow.org/js?hl=pt-br>
[3] <https://www.tensorflow.org/tutorials/keras/classification?hl=pt-br>
[4] <https://www.youtube.com/watch?v=oLY192SRxBM>
[5] <https://www.youtube.com/watch?v=0YQtFfovCZw>
