from socket import *

# Configuração da conexão
HOST = '0.0.0.0'
PORTA = 5000

# Credenciais válidas
MATRICULA_CORRETA = '1152026200079'
SENHA_CORRETA = '12345'

# Cria o socket
sockobj = socket(AF_INET, SOCK_STREAM)

# Vincula IP e porta
sockobj.bind((HOST, PORTA))

# Coloca o servidor para aguardar conexões
sockobj.listen(1)

print("Servidor aguardando conexão...")

while True:

    # Aceita conexão do cliente
    conexao, endereco = sockobj.accept()

    print("Cliente conectado:", endereco)

    while True:

        # Recebe a matrícula
        matricula = conexao.recv(1024).decode()

        if not matricula:
            break

        print("Matrícula recebida:", matricula)

        # Recebe a senha
        senha = conexao.recv(1024).decode()

        print("Senha recebida:", senha)

        # Verifica as credenciais
        if matricula == MATRICULA_CORRETA and senha == SENHA_CORRETA:

            resposta = "Login realizado com sucesso!"
            conexao.send(resposta.encode())

            print("Login realizado com sucesso.")

            # Encerra a autenticação
            break

        else:

            resposta = "Falha no login. Matrícula ou senha incorreta."
            conexao.send(resposta.encode())

            print("Falha no login.")

    # Fecha a conexão
    conexao.close()

    print("Cliente desconectado.")