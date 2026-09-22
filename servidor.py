from socket import *

# Configuração da conexão
HOST = '0.0.0.0'
PORTA = 5000

# Dados de login
MATRICULA_CORRETA = '1152026200079'
SENHA_CORRETA = '12345'

# Saldo inicial do usuário
saldo = 0.0

# Criação do socket
sockobj = socket(AF_INET, SOCK_STREAM)

# Vincula o servidor ao IP e à porta
sockobj.bind((HOST, PORTA))

# Coloca o servidor para aguardar conexões
sockobj.listen(1)

print("Servidor aguardando conexão...")

# Aceita a conexão do cliente
conexao, endereco = sockobj.accept()

print("Cliente conectado:", endereco)

# ==================================================
# LOGIN
# ==================================================

login_realizado = False

while not login_realizado:

    # Recebe a matrícula
    matricula = conexao.recv(1024).decode()

    # Recebe a senha
    senha = conexao.recv(1024).decode()

    print("Matrícula recebida:", matricula)
    print("Senha recebida:", senha)

    # Verifica matrícula e senha
    if matricula == MATRICULA_CORRETA and senha == SENHA_CORRETA:

        conexao.send("LOGIN_OK".encode())

        print("Login realizado com sucesso!")

        login_realizado = True

    else:

        conexao.send("LOGIN_ERRO".encode())

        print("Falha no login.")

# ==================================================
# MENU DE OPERAÇÕES
# ==================================================

while login_realizado:

    # Recebe a opção escolhida pelo cliente
    opcao = conexao.recv(1024).decode()

    # ----------------------------------------------
    # OPÇÃO 1 - DEPOSITAR
    # ----------------------------------------------

    if opcao == "1":

        # Solicita o valor ao cliente
        conexao.send("Digite o valor do deposito:".encode())

        # Recebe o valor
        valor = conexao.recv(1024).decode()

        try:
            valor = float(valor)

            if valor > 0:

                # Adiciona o valor ao saldo
                saldo = saldo + valor

                # Retorna o saldo atualizado
                resposta = f"Deposito realizado com sucesso! Saldo atual: R$ {saldo:.2f}"

            else:

                resposta = "O valor do deposito deve ser maior que zero."

        except ValueError:

            resposta = "Valor invalido."

        # Envia a resposta ao cliente
        conexao.send(resposta.encode())

    # ----------------------------------------------
    # OPÇÃO 2 - SACAR
    # ----------------------------------------------

    elif opcao == "2":

        # Solicita o valor ao cliente
        conexao.send("Digite o valor do saque:".encode())

        # Recebe o valor
        valor = conexao.recv(1024).decode()

        try:
            valor = float(valor)

            if valor <= 0:

                resposta = "O valor do saque deve ser maior que zero."

            elif valor > saldo:

                resposta = "Saldo insuficiente."

            else:

                # Retira o valor do saldo
                saldo = saldo - valor

                # Retorna o novo saldo
                resposta = f"Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}"

        except ValueError:

            resposta = "Valor invalido."

        # Envia a resposta ao cliente
        conexao.send(resposta.encode())

    # ----------------------------------------------
    # OPÇÃO 3 - VISUALIZAR SALDO
    # ----------------------------------------------

    elif opcao == "3":

        # Envia o saldo atual
        resposta = f"Saldo atual: R$ {saldo:.2f}"

        conexao.send(resposta.encode())

    # ----------------------------------------------
    # OPÇÃO 4 - SAIR
    # ----------------------------------------------

    elif opcao == "4":

        print("Cliente solicitou encerramento.")

        conexao.send("Conexao encerrada.".encode())

        break

    # ----------------------------------------------
    # OPÇÃO INVÁLIDA
    # ----------------------------------------------

    else:

        resposta = "Opcao invalida. Escolha entre 1 e 4."

        conexao.send(resposta.encode())


# ==================================================
# ENCERRAMENTO
# ==================================================

conexao.close()
sockobj.close()

print("Conexao encerrada.")
print("Servidor finalizado.")