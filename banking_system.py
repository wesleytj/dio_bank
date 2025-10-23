from datetime import datetime, timedelta, date

# -----------------
# Constantes e Estado Global (Listas de Dados)
# -----------------

AGENCIA = "0001"
usuarios = []  # Lista para armazenar dicionários de usuários (clientes)
contas = []    # Lista para armazenar dicionários de contas correntes

# Dicionário de configuração de limites (Pode ser transferido para a conta no futuro)
CONFIG_LIMITE = {
    "limite_saque_diario": 3,
    "limite_transacoes_diario": 10,
    "limite_valor_saque": 500
}

conta = {
    "saldo": 0,
    "qtd_saque": 0,
    "transacao_diario": 0,
    "movimentacoes": []
}

# -----------------
# Telas / Menus
# -----------------

def exibir_menu():
    menu = f"""
################ DIO BANK V2.0.0 ################
#                Seja Bem-Vindo                 #
#################################################
# Escolha uma das opções a seguir:              #
# [c] Novo Usuário (Cliente)                    #
# [n] Nova Conta                                #
# [l] Listar Contas                             #
# -----------------------------------------------
# [d] Depositar                                 #
# [s] Sacar                                     #
# [e] Extrato                                   #
# -----------------------------------------------
# [q] Sair                                      #
#################################################
=> """
    return input(menu)

def telas(tipo, conta=None):
    match tipo:
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
# Saldo atual: R${conta["saldo"]:.2f}#
# ------------------------------------
{get_movimentacoes(conta)}
# ------------------------------------ 
#                                    #
#                                    #
######################################
=> """

# -----------------
# Funções
# -----------------

def add_movimentacoes(conta, data, tipo, valor):
    conta["movimentacoes"].append((data, tipo, valor))

def get_movimentacoes(conta):
    if len(conta["movimentacoes"]) == 0:
        return "Nenhuma movimentação realizada."
    else:
        extrato_formatado = ""        
        # Data armazenada em formato datetime object.
        for data_obj, tipo, valor in conta["movimentacoes"]:
            
            # Converte a data e hora para formato ptBR
            data_hora_str = data_obj.strftime('%d/%m/%Y %H:%M')            
            # Formato: [Data e Hora] Tipo - R$ Valor
            extrato_formatado += f"[{data_hora_str}] {tipo}: R${valor:.2f}\n"
        
        
        return extrato_formatado

def bloqueado(conta):
    if conta["movimentacoes"]:
        ultima_data_obj = conta["movimentacoes"][-1][0] 
    else:
        ultima_data_obj = datetime.now() 
        
    # Adiciona mais um dia
    data_retorno = ultima_data_obj + timedelta(days=1)    
    # Converte em formato ptBR
    data_retorno_formatada = data_retorno.strftime('%d/%m/%Y %H:%M')
    
    msg_bloqueado = f"""
######################################
#            DIO Bank                #
#             Bloqueado              #
######################################
# Você atingiu o limite de transações#
# diárias ({conta["config"]["limite_transacoes_diario"]}).                   #
#                                    #
# Tente novamente, a partir de:      #
# {data_retorno_formatada}           #
#                                    #
######################################
=> """
    return msg_bloqueado

def cadastrar_usuario_cliente():
    pass

def cadastrar_conta_bancaria():
    pass

while True:
    opcao = exibir_menu()

    if opcao in ("d", "s"):
        # Aplica a validação de limite de transações diárias APENAS para transações
        if conta["transacao_diario"] >= CONFIG_LIMITE["limite_transacoes_diario"]:
            print(bloqueado(conta))
            # Se a transação estiver bloqueada, volta para o menu principal
            continue  # Volta ao início do 'while True'
    
    # Entra na validação para ação de DEPÓSITO        
    if(opcao == "d"):
        while True:            
            valor_deposito = float(input(telas(tipo = "deposito"))) # Informa o valor a ser depositado
            if(valor_deposito > 0):
                conta["saldo"] += valor_deposito # Adiciona o valor na conta
                data_hora = datetime.now() # Registra a data e hora da movimentação
                add_movimentacoes(conta, data_hora, "Depósito", valor_deposito) # Registra a movimetação para inserir no extrato posteriormente
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
        if conta["qtd_saque"] >= CONFIG_LIMITE["limite_saque_diario"]:
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
            elif(valor_saque > CONFIG_LIMITE["limite_valor_saque"]): # Verifica o valor do saque
                print("Limite do valor de saque excedido.")
            else:
                conta["saldo"] -= valor_saque  # Remove o valor sacado do saldo em conta                
                conta["qtd_saque"] += 1 # Contabiliza a quantidade de saques
                conta["transacao_diario"] += 1 # Contabiliza a transação
                data_hora = datetime.now() # Registra a data e hora da movimentação               
                add_movimentacoes(conta, data_hora, "Saque", valor_saque) # Registra a movimetação para inserir no extrato posteriormente
                print("Saque realizado com sucesso!")
                break
            
    elif(opcao == "e"):
        print(telas(tipo = "extrato", conta = conta))
    elif(opcao == "q"):
        print("Nos vemos em breve. Até mais!")
        break
    else:
        print("Opção inválida! Digite uma opção dentro do menu.")