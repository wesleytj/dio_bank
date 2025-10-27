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

def depositar(saldo, valor, extrato, /):
    # Função que realiza depósito utilizando apenas argumentos posicionais
    if(valor > 0):
        saldo += valor # Adiciona o valor na conta
        data_hora = datetime.now() # Registra a data e hora da movimentação
        extrato.append((data_hora, "Depósito", valor))
        print(f"\n✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
        return saldo, extrato
    else:
        print("\n❌ Operação falhou! O valor informado é inválido (negativo ou zero).")
        return saldo, extrato 


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

def filtrar_usuario(cpf, usuarios):
    """Retorna o usuário se o CPF for encontrado, ou None."""
    cpf_formatado = "".join(filter(str.isdigit, cpf))
    for usuario in usuarios:
        if usuario["cpf"] == cpf_formatado:
            return usuario
    return None

def criar_usuario(usuarios):
    """Cria um novo usuário e armazena na lista global."""
    cpf = input("Informe o CPF (somente números): ")
    cpf_formatado = "".join(filter(str.isdigit, cpf))
    
    if filtrar_usuario(cpf_formatado, usuarios):
        print("\n❌ CPF já cadastrado! Não é possível cadastrar dois usuários com o mesmo CPF.")
        return

    nome = input("Informe o nome completo: ")
    dia_nascimento = input("Informe o dia de nascimento (dd): ")
    mes_nascimento = input("Informe o mês de nascimento (mm): ")
    ano_nascimento = input("Informe o ano de nascimento (aaaa): ")
    data_nascimento = f"{dia_nascimento}/{mes_nascimento}/{ano_nascimento}"
    logradouro = input("Informe o logradouro (rua, avenida, etc): ")
    nro = input("Informe o número: ")
    bairro = input("Informe o bairro: ")
    cidade = input("Informe a cidade: ")
    sigla_estado = input("Informe a sigla do estado (UF): ")
    endereco_completo = f"{logradouro}, {nro} - {bairro} - {cidade}/{sigla_estado}"

    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf_formatado,
        "endereco": endereco_completo
    }
    usuarios.append(novo_usuario)
    print("\n✅ Usuário cadastrado com sucesso!")

def criar_conta_corrente(AGENCIA, numero_conta, usuarios, contas):
    """Cria uma nova conta e a vincula a um usuário existente."""
    
    cpf = input("Informe o CPF do usuário para vincular a conta: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        nova_conta = {
            "agencia": AGENCIA,
            "numero_conta": numero_conta,
            "usuario": usuario,  # Armazena o dicionário do usuário
            "saldo": 0,
            "extrato": [],
            "numero_saques": 0,
            "transacoes_hoje": 0,
            "data_ultima_transacao": None # Para resetar limite diário no futuro
        }
        contas.append(nova_conta)
        print(f"\n✅ Conta Corrente criada com sucesso!")
        print(f"Agência: {AGENCIA} | Número: {numero_conta}")
        return nova_conta
    else:
        print("\n❌ Usuário não encontrado com o CPF informado. Cadastro de conta cancelado.")
        return None

def listar_contas(contas):
    """Exibe todas as contas cadastradas."""
    if not contas:
        print("\nNão há contas cadastradas.")
        return

    print("\n======== CONTAS CADASTRADAS ========")
    for conta in contas:
        print(f"Agência:\t{conta['agencia']}")
        print(f"C/C:\t\t{conta['numero_conta']}")
        print(f"Titular:\t{conta['usuario']['nome']}")
        print(f"CPF:\t\t{conta['usuario']['cpf']}")
        print("------------------------------------")
    print("====================================")






while True:
    opcao = exibir_menu()

    if opcao in ("d", "s"):
        # Aplica a validação de limite de transações diárias APENAS para transações
        if conta["transacao_diario"] >= CONFIG_LIMITE["limite_transacoes_diario"]:
            print(bloqueado(conta))
            # Se a transação estiver bloqueada, volta para o menu principal
            continue  # Volta ao início do 'while True'
    
    if(opcao == "c"):
        criar_usuario(usuarios)
    elif(opcao == "n"):
        numero_conta = len(contas) + 1  # Gera o número da conta sequencialmente
        nova_conta = criar_conta_corrente(AGENCIA, numero_conta, usuarios, contas)
        if nova_conta:
            conta = nova_conta  # Define
    # Entra na validação para ação de DEPÓSITO        
    elif(opcao == "d"):
        while True:            
            # CHAMADA DE FUNÇÃO POSITIONAL-ONLY (Apenas por Posição!)
            conta["saldo"], conta["extrato"] = \
            depositar(conta["saldo"], valor, conta["extrato"])

            # Se a transação foi válida (valor > 0), contabiliza
            if valor > 0:
                conta["transacoes_hoje"] += 1
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