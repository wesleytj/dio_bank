from datetime import date
from .conta import Conta
from .transacao import Saque

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite_valor_saque=500.0, limite_saque_diario=3):
        super().__init__(numero, cliente)
        self._limite_valor_saque = limite_valor_saque
        self._limite_saque_diario = limite_saque_diario

    def sacar(self, valor: float):
        numero_saques_hoje = len([
            transacao for transacao in self._historico.transacoes
            if transacao["tipo"] == Saque.__name__
            and transacao["data"].date() == date.today()
        ])

        if valor > self._limite_valor_saque:
            print("\n❌ Operação falhou! O valor do saque excede o limite permitido.")
            return False
        if numero_saques_hoje >= self._limite_saque_diario:
            print("\n❌ Operação falhou! Número máximo de saques diários excedido.")
            return False

        return super().sacar(valor)
