# Criar usuário
# Criar conta corrente  
# Separar em funções

import re

saldo = 0
limite = 500
extrato = ""
numerosaques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
numero_conta = 0
AGENCIA = '0001'

def apenas_numeros(s):
    return re.sub(r'\D', '', s) 

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta_corrente(AGENCIA, numero_conta, usuarios):
    cpf = input("Digite o cpf do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if not usuario:
        print("Usuário não encontrado")
        return
    agencia = AGENCIA
    numero_conta += 1
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    dt_nascimento = input("Data de nascimento: ")
    cpf = input("Digite cpf: ")
    cpf = apenas_numeros(cpf)
    if cpf in [usuario['cpf'] for usuario in usuarios]:
        print("CPF já cadastrado! \n")
        return
    
    logradouro = input("Digite o endereço (Logradouro): ")
    numero = input("Digite o endereço (Número): ")
    bairro = input("Digite o endereço (Bairro): ")
    cidade = input("Digite o endereço (Cidade): ")
    estado = input("Digite o endereço (Estado): ")

    usuarios.append({
        "nome": nome,
        "dt_nascimento": dt_nascimento,
        "cpf": cpf,
        "endereco": logradouro + ", " + numero + " - " + bairro + " - " + cidade + " - " + estado
    })

    print("Usuário cadastrado com sucesso: ")
    print(nome, dt_nascimento, cpf, logradouro + ", " + numero + " - " + bairro + " - " + cidade + " - " + estado ) 

def mostrar_saldo(saldo):
    print(f"Saldo atual: R$ {saldo:.2f}")
    return saldo

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    # keyword only
    if valor > limite:
        print("Valor acima do limite permitido")
        return saldo, extrato

    if numero_saques == limite_saques:
        print("Limite de saques diários atingido")
        return saldo, extrato

    if float(valor) > float(saldo):
        print("Saldo insuficiente")
        return saldo, extrato
    
    numero_saques += 1
    saldo -= valor
    print("\n=== Saque realizado com sucesso! ===")
    extrato += f"Saque:\t\tR$ {valor:.2f}\n"

    return saldo, extrato
    
def depositar(saldo, valor, extrato, /):
    # positional only
    if valor <= 0:
        print("Valor inválido")
        return saldo, extrato
    saldo += valor
    extrato += f"Depósito:\t\tR$ {valor:.2f}\n"
    
    
    return saldo, extrato



menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuário
[c] Criar Conta Corrente
[l] Listar Usuários
[q] Sair

=> """



while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depositar")
        valor = float(input("Digite o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)
        #extrato += f"Depósito: R$ {valor:.2f}\n"

        print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "s":
        valor = float(input("Digite o valor do saque: "))

        saldo, extrato = sacar(
            saldo=saldo, 
            valor=valor, 
            extrato=extrato, 
            limite=limite, 
            numero_saques=numerosaques, 
            limite_saques=LIMITE_SAQUES)
        


    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        
    elif opcao == "q":
        print("Saindo...")
        break
    elif opcao == "u":
        print("Criar Usuário")
        criar_usuario()
    elif opcao == "c":
        conta = criar_conta_corrente(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)
            print(contas)
    elif opcao == "l":
        print("Listar Usuários")
        for usuario in usuarios:
            print(usuario)
            for conta in contas:
                if usuario["cpf"] == conta["usuario"]['cpf']:
                    print(conta)
            print('\n')
            
    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")


    


