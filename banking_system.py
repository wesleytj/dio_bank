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

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Realiza o saque. Argumentos apenas por nome (keyword only).
    """
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saques:
        print("\n❌ Operação falhou! Número máximo de saques diários excedido.")
    elif excedeu_saldo:
        print("\n❌ Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print(f"\n❌ Operação falhou! O valor do saque excede o limite (R$ {limite:.2f}).")
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        data_hora = datetime.now()
        extrato.append((data_hora, "Saque", valor))
        print(f"\n✅ Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("\n❌ Operação falhou! O valor informado é inválido (negativo ou zero).")

    return saldo, extrato, numero_saques

def bloqueado(conta):
    # BUG FIX: Alterado "movimentacoes" para "extrato"
    if conta["extrato"]:
        # Pega a data da última transação no extrato
        ultima_data_obj = conta["extrato"][-1][0] 
    else:
         # Se não há extrato, usa a data atual
        ultima_data_obj = datetime.now() 

    # Adiciona mais um dia para estimar a data de retorno
    data_retorno = ultima_data_obj + timedelta(days=1)
    # Converte em formato ptBR
    data_retorno_formatada = data_retorno.strftime('%d/%m/%Y %H:%M')

    msg_bloqueado = f"""
######################################
#           DIO Bank                #
#         🚫 Bloqueado              #
######################################
# Você atingiu o limite de transações#
# diárias ({conta['config']['limite_transacoes_diario']}).                  #
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
            "data_ultima_transacao": None, # Para resetar limite diário no futuro
            "config": CONFIG_LIMITE,
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

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for data, tipo, valor in extrato:
            data_fmt = data.strftime("%d/%m/%Y %H:%M:%S")
            print(f"{data_fmt} - {tipo}: R$ {valor:.2f}")
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("=========================================\n")


def main():
    modo_teste_ = True  # Modo de teste ativado/desativado

    global contas, usuarios

    if modo_teste_:
        print("⚠️  Modo de Teste Ativado! Dados mock serão criados automaticamente.\n")
    # Usuário generico para testes
        mock_usuario = {
            "nome": "Wesley Jacques",
            "data_nascimento": "01/01/1990",
            "cpf": "12345678900",
            "endereco": "Rua Exemplo, 123 - Bairro - Cidade/UF"
        }
        usuarios.append(mock_usuario)

        # Conta genérica para testes
        mock_conta = {
            "agencia": AGENCIA,
            "numero_conta": 1,
            "usuario": mock_usuario,
            "saldo": 0,
            "extrato": [],
            "numero_saques": 0,
            "transacoes_hoje": 0,
            "data_ultima_transacao": None, # Para resetar limite diário no futuro
            "config": CONFIG_LIMITE,
        }
        contas.append(mock_conta)
        conta = mock_conta  # Define a conta atual como a conta de teste
    else:
        conta = None  # Nenhuma conta selecionada inicialmente

    while True:
        opcao = exibir_menu()

        if opcao in ("d", "s"):
            if conta is None: # Verifica se há uma conta ativa
                print("⚠️ Nenhuma conta está ativa! Crie uma conta primeiro.")
                continue
            if conta["transacoes_hoje"] >= CONFIG_LIMITE["limite_transacoes_diario"]: # Verifica se atingiu o limite diário de transações
                print(bloqueado(conta))
                continue  # Volta ao início do 'while True'
        
        # ---------------------------------       
        # Entra na validação para ação de NOVO USUÁRIO
        # ---------------------------------
        if(opcao == "c"):
            criar_usuario(usuarios)
        
        # ---------------------------------       
        # Entra na validação para ação de NOVA CONTA
        # ---------------------------------
        elif(opcao == "n"):
            numero_conta = len(contas) + 1  # Gera o número da conta sequencialmente
            nova_conta = criar_conta_corrente(AGENCIA, numero_conta, usuarios, contas)
            if nova_conta:
                conta = nova_conta  # Define a nova conta como a conta ativa

        # ---------------------------------
        # Entra na validação para ação de DEPÓSITO   
        # ---------------------------------     
        elif(opcao == "d"):
            if conta is None: # Verifica se há uma conta ativa
                print("⚠️ Nenhuma conta ativa! Crie uma conta primeiro.")
                continue

            while True:
                valor = float(input(telas(tipo="deposito")))
                if valor == 0:
                    print("\nℹ️  Operação cancelada pelo usuário.")
                    break
                novo_saldo, novo_extrato = depositar(conta["saldo"], valor, conta["extrato"])
                conta["saldo"] = novo_saldo
                conta["extrato"] = novo_extrato

        # ---------------------------------       
        # Entra na validação para ação de SAQUE
        # ---------------------------------
        elif(opcao == "s"):
            if conta is None:
                print("⚠️ Nenhuma conta ativa! Crie uma conta primeiro.")
                continue

            while True:
                valor = float(input(telas(tipo="saque")))
                if valor == 0:
                    print("\nℹ️  Operação cancelada pelo usuário.")
                    break

                novo_saldo, novo_extrato, novo_saques = sacar(
                    saldo=conta["saldo"],
                    valor=valor,
                    extrato=conta["extrato"],
                    limite=conta["config"]["limite_valor_saque"],
                    numero_saques=conta["numero_saques"],
                    limite_saques=conta["config"]["limite_saque_diario"]
                )

                conta["saldo"] = novo_saldo
                conta["extrato"] = novo_extrato
                conta["numero_saques"] = novo_saques

        # ---------------------------------       
        # Entra na validação para ação de EXTRATO
        # ---------------------------------        
        elif opcao == "e":
            if conta is None:
                print("⚠️ Nenhuma conta ativa! Crie uma conta primeiro.")
                continue
            exibir_extrato(conta["saldo"], extrato=conta["extrato"])

        elif opcao == "l":
            listar_contas(contas)

        # ---------------------------------       
        # Entra na validação para ação de LOGOUT
        # ---------------------------------
        elif opcao == "q":
            print("Nos vemos em breve. Até mais!")
            break

        else:
            print("Opção inválida! Digite uma opção dentro do menu.")

if __name__ == "__main__":
    main()