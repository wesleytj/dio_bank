# banking_system_poo.py
from datetime import datetime, date
from abc import ABC, abstractmethod

# =============================
# CLASSES DO SISTEMA BANCÁRIO
# =============================

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento

    def __str__(self):
        return f"{self._nome} ({self._cpf})"


class Conta:
    _contador_conta = 0

    def __init__(self, numero, cliente):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente):
        cls._contador_conta += 1
        return cls(cls._contador_conta, cliente)

    def depositar(self, valor):
        if valor <= 0:
            print("\n❌ Valor inválido para depósito.")
            return False

        self._saldo += valor
        print(f"\n✅ Depósito de R$ {valor:.2f} realizado com sucesso!")

        self._historico.adicionar_transacao(Deposito(valor))
        return True

    def sacar(self, valor):
        if valor <= 0:
            print("\n❌ Valor inválido para saque.")
            return False

        if valor > self._saldo:
            print("\n❌ Saldo insuficiente para realizar o saque.")
            return False

        self._saldo -= valor
        print(f"\n✅ Saque de R$ {valor:.2f} realizado com sucesso!")

        self._historico.adicionar_transacao(Saque(valor))
        return True

    def saldo(self):
        return self._saldo

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        transacoes = self._historico.transacoes
        if not transacoes:
            print("Nenhuma movimentação registrada.")
        else:
            for t in transacoes:
                data_fmt = t["data"].strftime("%d/%m/%Y %H:%M:%S")
                print(f"{data_fmt} - {t['tipo']}: R$ {t['valor']:.2f}")
        print(f"\nSaldo atual: R$ {self._saldo:.2f}")
        print("=========================================\n")


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite_valor_saque=500.0, limite_saque_diario=3):
        super().__init__(numero, cliente)
        self._limite_valor_saque = limite_valor_saque
        self._limite_saque_diario = limite_saque_diario

    def sacar(self, valor):
        numero_saques_hoje = len([
            transacao for transacao in self._historico.transacoes
            if transacao["tipo"] == Saque.__name__
            and transacao["data"].date() == date.today()
        ])

        excedeu_valor_saque = valor > self._limite_valor_saque
        excedeu_saques_diarios = numero_saques_hoje >= self._limite_saque_diario

        if excedeu_valor_saque:
            print("\n❌ Operação falhou! O valor do saque excede o limite permitido.")
        elif excedeu_saques_diarios:
            print("\n❌ Operação falhou! Número máximo de saques diários excedido.")
        else:
            # chama a lógica comum de sacar (verifica saldo, decrementa, registra histórico)
            return super().sacar(valor)

        return False


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        # Retorna a lista de dicionários de transações
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now()  
        })


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        conta.sacar(self.valor)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        conta.depositar(self.valor)


# =============================
# FUNÇÕES DE INTERFACE (MENU)
# =============================

def menu():
    print("""
========== DIO BANK ==========
[c] Criar Cliente
[n] Nova Conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
==============================
""")
    return input("Escolha uma opção: ").lower()


# =============================
# FUNÇÃO PRINCIPAL (INTERAÇÃO)
# =============================

def main():
    modo_teste_ = False  # Altere para True para criar cliente e conta de teste automaticamente

    clientes = []
    contas = []
    conta_ativa = None

    if modo_teste_:
        print("⚙️ Modo de teste ativado. Criando cliente e conta de teste...\n")
        # Criando cliente e conta de teste
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
            # Criar Cliente
            nome = input("Digite o nome: ")
            cpf = input("Digite o CPF: ")
            data_nasc = input("Digite a data de nascimento (DD/MM/AAAA): ")
            endereco = input("Digite o endereço: ")

            novo_cliente = PessoaFisica(nome, cpf, data_nasc, endereco)
            clientes.append(novo_cliente)
            print(f"\n✅ Cliente {nome} criado com sucesso!")

        elif opcao == "n":
            # Nova Conta (vincular a último cliente criado)
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
            # Depositar
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
            # Sacar
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
            # Exibir extrato
            if not conta_ativa:
                print("\n❌ Nenhuma conta ativa para realizar operações. Crie uma conta primeiro.")
                continue
            conta_ativa.exibir_extrato()

        elif opcao == "q":
            print("\n👋 Obrigado por usar o DIO Bank! Até logo.")
            break

        else:
            print("\n❌ Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
