import socket
import ssl

# Definir o endereço IP e a porta do servidor
HOST = 'www.exemplo.com'  # Endereço IP do servidor
PORT = 443  # Porta do servidor

# Criar um socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar ao servidor
server_address = (HOST, PORT)
print(f"Conectando a {server_address}")
sock.connect(server_address)

# Criar um contexto SSL
context = ssl.create_default_context()

# Estabelecer uma conexão SSL/TLS
wrapped_sock = context.wrap_socket(sock, server_hostname=HOST)

# Enviar dados para o servidor
message = "Olá, servidor!"
print(f"Enviando: {message}")
wrapped_sock.sendall(message.encode())

# Receber resposta do servidor
data = wrapped_sock.recv(1024)
print(f"Recebido: {data.decode()}")

# Fechar a conexão
print("Fechando conexão")
wrapped_sock.close()