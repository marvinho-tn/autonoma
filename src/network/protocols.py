import requests

# Definir o endereço URL do servidor
url = 'https://www.exemplo.com'

# Fazer uma solicitação HTTP GET
response = requests.get(url)

# Verificar o status da resposta
if response.status_code == 200:
    # Obter o conteúdo da resposta
    content = response.content
    print(f"Conteúdo da resposta: {content}")
else:
    print(f"Erro na solicitação: {response.status_code}")