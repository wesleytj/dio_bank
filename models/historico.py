from datetime import datetime
from typing import List, Dict

class Historico:
    def __init__(self):
        self._transacoes: List[Dict] = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        # transacao é objeto (Deposito ou Saque)
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now()
        })
