from datetime import datetime, timedelta, date

# -----------------
# Estado da conta
# -----------------

conta = {
    "saldo": 0,
    "qtd_saque": 0,
    "transacao_diario": 0,
    "movimentacoes": [],
    "config": {
        "limite_saque_diario": 3,
        "limite_transacoes_diario": 10,
        "limite_valor_saque": 500
    }
}

# -----------------
# Telas / Menus
# -----------------

def telas(tipo, conta=None):
    match tipo:
        case "menu":
            return """
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
        case "deposito":
            return """
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
        case "saque":
            return """
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
        case "extrato":
            return f"""
######################################
#             DIO Bank               #
#     📄  Extrato Bancário           #
######################################
# Saldo atual: R${conta["saldo"]}    \n       #
#    {get_movimentacoes(conta)}            #
#                                    #
#                                    #
#                                    #
######################################
=> """

# -----------------
# Funções
# -----------------

def add_movimentacoes(conta, tipo, valor):
    conta["movimentacoes"].append((tipo, valor))

def get_movimentacoes(conta):
    if len(conta["movimentacoes"]) == 0:
        return "Nenhuma movimentação realizada."
    else:
        linha = """"""
        for tipo, valor in conta["movimentacoes"]:
            linha += f"{tipo} - R${valor:.2f}\n#    "
        return linha

def bloqueado():
    msg_bloqueado = f"""
######################################
#             DIO Bank               #
#             Bloqueado              #
######################################
# Você atingiu o limite de transações#
# diárias.                           #
#                                    #
# Volte novamente, a partir          #
# de: {f"{datetime.strptime(f"{datetime.now().strftime('%d/%m/%Y %H:%M')}", "%d/%m/%Y %H:%M") + timedelta(days=1)}"}            #
#                                    #
######################################
=> """

    return msg_bloqueado

while True:
    opcao = input(telas(tipo = "menu"))

    if opcao in ("d", "s"):
        # Aplica a validação de limite de transações diárias APENAS para transações
        if conta["transacao_diario"] >= conta["config"]["limite_transacoes_diario"]:
            print(bloqueado())
            # Se a transação estiver bloqueada, volta para o menu principal
            continue  # Volta ao início do 'while True'
    
    # Entra na validação para ação de DEPÓSITO        
    if(opcao == "d"):
        while True:            
            valor_deposito = float(input(telas(tipo = "deposito"))) # Informa o valor a ser depositado
            if(valor_deposito > 0):
                conta["saldo"] += valor_deposito # Adiciona o valor na conta
                add_movimentacoes(conta, "Depósito", valor_deposito) # Registra a movimetação para inserir no extrato posteriormente
                conta["transacao_diario"] += 1 # Contabiliza a transação
                print("Depósito realizado com sucesso!")
                break
            elif(valor_deposito == 0):
                print("Operação cancelada!")
                break
            else:
                print("O valor de depósito não pode ser negativo.")
    # Entra na validação para ação de SAQUE
    elif(opcao == "s"):
        if conta["qtd_saque"] >= conta["config"]["limite_saque_diario"]:
            print("Limite de saques diários excedidos.")
            continue

        while True:            
            valor_saque = float(input(telas(tipo = "saque"))) # Informa o valor a ser sacado
            # Valida as regras para o saque
            if(valor_saque < 0): # Se tentar sacar um valor negativo
                print("Não é possível realizar um saque de valor negativo. Digite um valor válido.")
            elif(valor_saque == 0): # Para cancelar a operação
                print("Operação cancelada!")
                break
            elif(valor_saque > conta["saldo"]): # Verifica se há saldo suficiente
                print("Saldo insuficiente para realização do saque.")
            elif(valor_saque > conta["config"]["limite_valor_saque"]): # Verifica o valor do saque
                print("Limite do valor de saque excedido.")
            else:
                conta["saldo"] -= valor_saque  # Remove o valor sacado do saldo em conta                
                conta["qtd_saque"] += 1 # Contabiliza a quantidade de saques
                conta["transacao_diario"] += 1 # Contabiliza a transação
                add_movimentacoes(conta, "Saque", valor_saque) # Registra a movimetação para inserir no extrato posteriormente
                print("Saque realizado com sucesso!")
                break
            
    elif(opcao == "e"):
        print(telas(tipo = "extrato", conta = conta))
    elif(opcao == "q"):
        print("Nos vemos em breve. Até mais!")
        break
    else:
        print("Opção inválida! Digite uma opção dentro do menu.")