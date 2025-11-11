from .models.cliente import PessoaFisica
from .models.conta_corrente import ContaCorrente
from .models.transacao import Deposito, Saque
from .currency_converter_package.converter import converter # Importa o conversor de moedas

def menu():
    print("""
========== DIO BANK ==========
[c] Criar Cliente
[n] Nova Conta
[d] Depositar
[s] Sacar
[e] Extrato
[x] Converter Moeda
[q] Sair
==============================
""")
    return input("Escolha uma opção: ").lower()


def main():
    modo_teste_ = True  # Altere para True para criar cliente e conta de teste automaticamente

    clientes = []
    contas = []
    conta_ativa = None

    if modo_teste_:
        print("⚙️ Modo de teste ativado. Criando cliente e conta de teste...\n")
        cliente = PessoaFisica(
            nome="Fulano de Tal",
            cpf="12345678900",
            data_nascimento="01/01/1990",
            endereco="Rua da Sabedoria, 777 - Reino/DE"
        )

        conta = ContaCorrente.nova_conta(cliente)
        cliente.adicionar_conta(conta)
        conta_ativa = conta

        print(f"✅ Conta criada com sucesso para {cliente}")
        print(f"Agência: {conta._agencia} | Número: {conta._numero}\n")
    else:
        print("👋 Bem-vindo ao DIO Bank!")

    while True:
        opcao = menu()

        if opcao == "c":
            nome = input("Digite o nome: ")
            cpf = input("Digite o CPF: ")
            data_nasc = input("Digite a data de nascimento (DD/MM/AAAA): ")
            endereco = input("Digite o endereço: ")

            novo_cliente = PessoaFisica(nome, cpf, data_nasc, endereco)
            clientes.append(novo_cliente)
            print(f"\n✅ Cliente {nome} criado com sucesso!")

        elif opcao == "n":
            if not clientes:
                print("\n❌ Nenhum cliente cadastrado. Crie um cliente primeiro.")
                continue

            cliente_selecionado = clientes[-1]
            nova_conta = ContaCorrente.nova_conta(cliente_selecionado)
            cliente_selecionado.adicionar_conta(nova_conta)
            contas.append(nova_conta)
            conta_ativa = nova_conta

            print(f"\n✅ Nova Conta Corrente criada para {cliente_selecionado}!")
            print(f"Agência: {nova_conta._agencia} | Número: {nova_conta._numero}")
            print("Conta definida como ativa.")

        elif opcao == "d":
            if not conta_ativa:
                print("\n❌ Nenhuma conta ativa para realizar operações. Crie uma conta primeiro.")
                continue
            try:
                valor = float(input("Informe o valor do depósito: "))
                cliente_ativa = conta_ativa._cliente
                cliente_ativa.realizar_transacao(conta_ativa, Deposito(valor))
            except ValueError:
                print("\n❌ Valor inválido. Digite um número.")

        elif opcao == "s":
            if not conta_ativa:
                print("\n❌ Nenhuma conta ativa para realizar operações. Crie uma conta primeiro.")
                continue
            try:
                valor = float(input("Informe o valor do saque: "))
                cliente_ativa = conta_ativa._cliente
                cliente_ativa.realizar_transacao(conta_ativa, Saque(valor))
            except ValueError:
                print("\n❌ Valor inválido. Digite um número.")

        elif opcao == "e":
            if not conta_ativa:
                print("\n❌ Nenhuma conta ativa para realizar operações. Crie uma conta primeiro.")
                continue
            conta_ativa.exibir_extrato()

        elif opcao == "q":
            print("\n👋 Obrigado por usar o DIO Bank! Até logo.")
            break

        elif opcao == "x":
            try:
                valor_original = float(input("Informe o valor a ser convertido: "))
                moeda_origem = input("Informe a moeda de origem (ex: USD, EUR, BRL): ").upper()
                moeda_destino = input("Informe a moeda de destino (ex: USD, EUR, BRL): ").upper()

                valor_convertido = converter(valor_original, moeda_origem, moeda_destino)
                print(f"\n✅ {valor_original:.2f} {moeda_origem} equivalem a {valor_convertido:.2f} {moeda_destino}.")
            except ValueError:
                print("\n❌ Valor inválido. Digite um número.")
            except Exception as e:
                print(f"\n❌ Ocorreu um erro na conversão: {e}")

        else:
            print("\n❌ Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
