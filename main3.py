''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''

def calcular_saldo(transacoes):
    saldo = 0
    for linha in transacoes:
      saldo += linha
    
    return f'Saldo R$ {saldo:.2f}'
    # TODO: Itere sobre cada transação na lista:
    
        # TODO: Adicione o valor da transação ao saldo
        

    # TODO: Retorne o saldo formatado em moeda brasileira com duas casas decimais:
    

entrada_usuario = input()

entrada_usuario = entrada_usuario.strip("[]").replace(" ", "")

transacoes = [float(valor) for valor in entrada_usuario.split(",")]

# TODO: Calcule o saldo com base nas transações informadas:
resultado = calcular_saldo(transacoes)

print(resultado)
