saldo = 0
qtd_saque = 0
movimentacoes = []

def exibir_menu():
    menu = """
######################################
#          Seja Bem-Vindo            #
#             DIO Bank               #
######################################
# Escolha uma das opções a seguir:   #
#                                    #
#   [d] Depositar                    #
#   [s] Sacar                        #
#   [e] Extrato                      #
#   [q] Sair                         #
#                                    #
######################################
=> """
    return menu

def depositar():
    depositar = """
######################################
#             DIO Bank               #
#         💰  Depósito               #
######################################
# Quanto você gostaria de depositar? #
#                                    #
# 💰 Digite o valor de depósito:     #
#    [0] Cancelar                    #
#                                    #
######################################
=> """
    return depositar

def sacar():
    sacar = """
######################################
#             DIO Bank               #
#          💸  Saque                 #
######################################
# Quanto você gostaria de sacar?     #
#                                    #
# 💸 Digite o valor de saque:        #
#    [0] Cancelar                    #
#                                    #
######################################
=> """
    return sacar

def exibir_extrato():
    extrato = f"""
######################################
#             DIO Bank               #
#     📄  Extrato Bancário           #
######################################
# Saldo atual: R${saldo}    \n       #
#    {get_movimentacoe()}            #
#                                    #
#                                    #
#                                    #
######################################
=> """
    return extrato

def add_movimentacoes(tipo, valor):
    movimentacoes.append((tipo, valor))

def get_movimentacoe():
    if len(movimentacoes) == 0:
        return "Nenhuma movimentação realizada."
    else:
        linha = """"""
        for tipo, valor in movimentacoes:
            linha += f"{tipo} - R${valor:.2f}\n#    "
        return linha

while True:
    opcao = input(exibir_menu())

    if(opcao == "d"):
        while True:
            valor_deposito = float(input(depositar()))
            if(valor_deposito > 0):
                saldo += valor_deposito
                add_movimentacoes("Depósito", valor_deposito)
                print("Depósito realizado com sucesso!")
                break
            elif(valor_deposito == 0):
                print("Operação cancelada!")
                break
            else:
                print("O valor de depósito não pode ser negativo.")
    elif(opcao == "s"):
        while True:            
            valor_saque = float(input(sacar()))
            if(qtd_saque < 3):
                if(valor_saque < 0):
                    print("Não é possível realizar um saque de valor negativo. Digite um valor válido.")
                elif(valor_saque == 0):
                    print("Operação cancelada!")
                    break
                elif(valor_saque > saldo):
                    print("Saldo insuficiente para realização do saque.")
                elif(valor_saque > 500):
                    print("Limite do valor de saque excedido.")
                else:
                    saldo -= valor_saque                    
                    qtd_saque += 1
                    add_movimentacoes("Saque", valor_saque)
                    print(f"Quantidade de saques: {qtd_saque}")
                    print("Saque realizado com sucesso!")
                    break
            else:
                print("Limite de saques diários excedidos.")
                break
    elif(opcao == "e"):
        print(exibir_extrato())
    elif(opcao == "q"):
        print("Nos vemos em breve. Até mais!")
        break
    else:
        print("Opção inválida! Digite uma opção dentro do menu.")
