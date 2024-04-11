import socket

# Definir o endereço IP e a porta do servidor
HOST = 'www.exemplo.com'  # Endereço IP do servidor
PORT = 80  # Porta do servidor

# Criar um socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar ao servidor
server_address = (HOST, PORT)
print(f"Conectando a {server_address}")
sock.connect(server_address)

# Enviar dados para o servidor
message = "Olá, servidor!"
print(f"Enviando: {message}")
sock.sendall(message.encode())

# Receber resposta do servidor
data = sock.recv(1024)
print(f"Recebido: {data.decode()}")

# Fechar a conexão
print("Fechando conexão")
sock.close()