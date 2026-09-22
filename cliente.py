from socket import *

# Configuração da conexão
HOST = '127.0.0.1'
PORTA = 5000

# Criação do socket
conexao = socket(AF_INET, SOCK_STREAM)

# Conecta ao servidor
conexao.connect((HOST, PORTA))

print("========================================")
print("        SISTEMA BANCARIO")
print("========================================")
print("Conectado ao servidor.")
print()

# ==================================================
# LOGIN
# ==================================================

login_realizado = False

while not login_realizado:

    # Solicita matrícula
    matricula = input("Digite sua matricula: ")

    # Solicita senha
    senha = input("Digite sua senha: ")

    # Envia matrícula
    conexao.send(matricula.encode())

    # Envia senha
    conexao.send(senha.encode())

    # Recebe resposta do servidor
    resposta = conexao.recv(1024).decode()

    if resposta == "LOGIN_OK":

        print()
        print("Login realizado com sucesso!")
        print()

        login_realizado = True

    else:

        print()
        print("Falha no login!")
        print("Matricula ou senha incorreta.")
        print("Tente novamente.")
        print()

# ==================================================
# MENU
# ==================================================

while login_realizado:

    print()
    print("========================================")
    print("                MENU")
    print("========================================")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Visualizar Saldo")
    print("4 - Sair")
    print("========================================")

    opcao = input("Escolha uma opcao: ")

    # Envia a opção para o servidor
    conexao.send(opcao.encode())

    # ----------------------------------------------
    # OPÇÃO 1 - DEPOSITAR
    # ----------------------------------------------

    if opcao == "1":

        # Recebe solicitação do servidor
        mensagem = conexao.recv(1024).decode()

        print()
        print(mensagem)

        # Solicita valor
        valor = input("R$ ")

        # Envia valor para o servidor
        conexao.send(valor.encode())

        # Recebe saldo atualizado
        resposta = conexao.recv(1024).decode()

        print()
        print(resposta)

    # ----------------------------------------------
    # OPÇÃO 2 - SACAR
    # ----------------------------------------------

    elif opcao == "2":

        # Recebe solicitação do servidor
        mensagem = conexao.recv(1024).decode()

        print()
        print(mensagem)

        # Solicita valor
        valor = input("R$ ")

        # Envia valor para o servidor
        conexao.send(valor.encode())

        # Recebe resposta do servidor
        resposta = conexao.recv(1024).decode()

        print()
        print(resposta)

    # ----------------------------------------------
    # OPÇÃO 3 - VISUALIZAR SALDO
    # ----------------------------------------------

    elif opcao == "3":

        # Recebe o saldo do servidor
        resposta = conexao.recv(1024).decode()

        print()
        print(resposta)

    # ----------------------------------------------
    # OPÇÃO 4 - SAIR
    # ----------------------------------------------

    elif opcao == "4":

        # Recebe confirmação do servidor
        resposta = conexao.recv(1024).decode()

        print()
        print(resposta)

        login_realizado = False

    # ----------------------------------------------
    # OPÇÃO INVÁLIDA
    # ----------------------------------------------

    else:

        resposta = conexao.recv(1024).decode()

        print()
        print(resposta)


# ==================================================
# ENCERRAMENTO
# ==================================================

conexao.close()

print("Cliente encerrado.")