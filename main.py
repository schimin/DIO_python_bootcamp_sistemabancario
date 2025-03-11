# deposito, saque e extrato
# 3 saques diarios com limite maximo de 500 reais por saque
# listagem deve exibir o saldo atual da conta formato R$

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numerosaques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depositar")
        valor = float(input("Digite o valor do depósito: "))
        saldo += valor
    elif opcao == "s":
        if (LIMITE_SAQUES == numerosaques):
            print("Limite de saques diários atingido")
            continue
        numerosaques += 1
        valor = float(input("Digite o valor do saque: "))
        if valor > saldo:
            print("Saldo insuficiente")
        else:
            saldo -= valor
            print("Saque realizado com sucesso")        
        #print("Sacar")
    elif opcao == "e":
        print("Extrato")
    elif opcao == "q":
        print("Saindo...")
        break
    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")

    print(f"Saldo atual: R$ {saldo:.2f}")
class Banco:
    def __init__(self):
        self.saldo = 0

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def extrato(self):
        print(f"Seu saldo é de: {self.saldo}")
