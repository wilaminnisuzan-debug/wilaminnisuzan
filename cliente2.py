from socket import *

# Configuração da conexão
HOST = '127.0.0.1'
PORTA = 5000

# Cria o socket
conexao = socket(AF_INET, SOCK_STREAM)

# Conecta ao servidor
conexao.connect((HOST, PORTA))

print("Conectado ao servidor!")
print("--------------------------------")

while True:

    # Solicita matrícula
    matricula = input("Digite sua matrícula: ")

    # Solicita senha
    senha = input("Digite sua senha: ")

    # Envia matrícula para o servidor
    conexao.send(matricula.encode())

    # Envia senha para o servidor
    conexao.send(senha.encode())

    # Recebe resposta do servidor
    data = conexao.recv(1024)

    resposta = data.decode()

    print("--------------------------------")
    print("Servidor:", resposta)
    print("--------------------------------")

    # Se o login estiver correto, encerra
    if resposta == "Login realizado com sucesso!":
        break

# Fecha a conexão
conexao.close()

print("Conexão encerrada.")