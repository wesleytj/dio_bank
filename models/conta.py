from .historico import Historico
from .transacao import Deposito, Saque

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

    def depositar(self, valor: float):
        if valor <= 0:
            print("\n❌ Valor inválido para depósito.")
            return False
        self._saldo += valor
        print(f"\n✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
        self._historico.adicionar_transacao(Deposito(valor))
        return True

    def sacar(self, valor: float):
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
