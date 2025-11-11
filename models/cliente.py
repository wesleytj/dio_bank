from typing import List

class Cliente:
    def __init__(self, endereco: str):
        self._endereco = endereco
        self._contas: List = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome: str, cpf: str, data_nascimento: str, endereco: str):
        super().__init__(endereco)
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento

    def __str__(self):
        return f"{self._nome} ({self._cpf})"
