menu = """
[c] Criar Usuário
[f] Filtrar Usuário
[d] Depositar
[s] Sacar
[e] Extrato
[n] Criar Conta
[l] Listar Contas
[q] Sair

=> """

usuarios = []
contas = []

def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    cpf = input("Digite o CPF do usuário: ")
    usuarios.append({"nome": nome, "cpf": cpf})
    print("Usuário criado com sucesso!")

def filtrar_usuario():
    cpf_busca = input("Digite o CPF do usuário que deseja buscar: ")
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario["cpf"] == cpf_busca:
            usuario_encontrado = usuario
            break

    if usuario_encontrado:
        print("Usuário encontrado:")
        print(f"Nome: {usuario_encontrado['nome']}")
        print(f"CPF: {usuario_encontrado['cpf']}")
    else:
        print("Usuário não encontrado!")

def criar_conta():
    cpf_titular = input("Digite o CPF do titular da conta: ")
    titular_encontrado = None
    for usuario in usuarios:
        if usuario["cpf"] == cpf_titular:
            titular_encontrado = usuario
            break

    if titular_encontrado:
        saldo_inicial = float(input("Digite o saldo inicial da conta: "))
        contas.append({"titular": titular_encontrado, "saldo": saldo_inicial, "extrato": "", "numero_saques": 0})
        print("Conta criada com sucesso!")
    else:
        print("Titular não encontrado! Crie o usuário primeiro.")

def listar_contas():
    print("\n============== LISTA DE CONTAS ===============")
    for i, conta in enumerate(contas, 1):
        print(f"\nConta {i}:")
        print(f"Titular: {conta['titular']['nome']}")
        print(f"CPF do Titular: {conta['titular']['cpf']}")
        print(f"Saldo: R$ {conta['saldo']:.2f}")
    print("==============================================")

def extrato_conta():
    listar_contas()
    numero_conta = int(input("Digite o número da conta que deseja visualizar o extrato: "))
    if 1 <= numero_conta <= len(contas):
        conta_selecionada = contas[numero_conta - 1]
        print("\n=============== EXTRATO ===============")
        print("Não foram realizadas movimentações." if not conta_selecionada['extrato'] else conta_selecionada['extrato'])
        print(f"\nSaldo: R$ {conta_selecionada['saldo']:.2f}")
        print("======================================")
    else:
        print("Número de conta inválido!")

def sacar():
    listar_contas()
    numero_conta = int(input("Digite o número da conta para sacar: "))
    if 1 <= numero_conta <= len(contas):
        conta_selecionada = contas[numero_conta - 1]
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > conta_selecionada['saldo']
        excedeu_limite = valor > limite
        excedeu_saques = conta_selecionada['numero_saques'] >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            conta_selecionada['saldo'] -= valor
            conta_selecionada['extrato'] += f"Saque: R$ {valor:.2f}\n"
            conta_selecionada['numero_saques'] += 1
        else:
            print("Operação falhou! O valor informado é inválido.")
    else:
        print("Número de conta inválido!")

def depositar():
    listar_contas()
    numero_conta = int(input("Digite o número da conta para depositar: "))
    if 1 <= numero_conta <= len(contas):
        conta_selecionada = contas[numero_conta - 1]
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            conta_selecionada['saldo'] += valor
            conta_selecionada['extrato'] += f"Depósito de R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")
    else:
        print("Número de conta inválido!")

while True:
    opcao = input(menu)

    if opcao == "c":
        criar_usuario()
    elif opcao == "f":
        filtrar_usuario()
    elif opcao == "d":
        depositar()
    elif opcao == "s":
        sacar()
    elif opcao == "e":
        extrato_conta()
    elif opcao == "n":
        criar_conta()
    elif opcao == "l":
        listar_contas()
    elif opcao == "q":
        print("Saindo...")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
