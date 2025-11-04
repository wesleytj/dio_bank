# 🏦 Sistema Bancário em Python (DIO Bank - Versão 2.1.0)

Projeto didático que evoluiu do estilo procedural para uma implementação orientada a objetos (POO).  
Implementa as entidades e operações bancárias conforme a modelagem UML: `Cliente`, `Conta`, `ContaCorrente`, `Historico` e `Transacao` (com `Deposito` e `Saque`).



---

## ➤ Funcionalidades principais

- Criar clientes (Pessoa Física).
- Criar contas correntes vinculadas a clientes (agência fixa `0001`, número sequencial).
- Depositar (via `Deposito`).
- Sacar (via `Saque`) com:
  - limite por operação (R$ 500,00 por padrão),
  - limite de saques por dia (3 por padrão),
  - validação de saldo.
- Exibir extrato com data/hora e saldo.
- Histórico com armazenamento de transações e data (permite contagem por dia).



---

## Regras de negócio destacadas

- **Depósito:** aceita apenas valores positivos.
- **Saque:** somente valores positivos, respeitando saldo e limites.
- **Limite diário de transações (depósito + saque):** configurável (ex.: 10/dia).
- **Conta:** números gerados sequencialmente via `Conta.nova_conta()`.



---

## 💡 Como Executar

Para rodar o sistema em sua máquina local, siga os passos abaixo:

1. **Clone o Repositório:**
   
   ```bash
   git clone https://github.com/wesleytj/sistema_bancario.git
   cd sistema_bancario
   ```

2. **Execute o Arquivo Python:**
   
   ```bash
   python banking_system.py
   ```

O arquivo principal contém a variável `modo_teste` na função `main()`.

* Com `modo_teste = True` (útil para testes): um cliente e conta são criados automaticamente.

* Com `modo_teste = False`: você deverá criar um cliente (`[c]`) e depois uma conta (`[n]`) antes de fazer transações.



---

## ⚙️ Nota Importante: Modo de Teste

O arquivo `banking_system.py` na função `main()` contém a variável `modo_teste_ = False`.

**Com `modo_teste_ = True` (Padrão):** 

Uma conta genérica (Ag 0001 | C/C 1) e seu usuário são criados automaticamente para permitir testes imediatos de depósito/saque/extrato.

**Para Desativar:** Altere `modo_teste_` para `False` em `main()`. 

O sistema iniciará sem contas cadastradas, exigindo que você use as opções `[c]` (Novo Usuário) e `[n]` (Nova Conta) antes de fazer qualquer transação.



---

## 📚 Observações técnicas e sugestões futuras

* Próximo passo: adicionar persistência (arquivo JSON ou banco), login por CPF e interface web.



---

**Feito com ❤️ e 🐍 por Wesley Treib Jacques**
