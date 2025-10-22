# 🏦 Sistema Bancário em Python (DIO Bank - Versão 1.2.0)

Este projeto simula as operações básicas de um sistema bancário (Depósito, Saque, Extrato) e serve como base para o desafio do Bootcamp de Python da DIO. Esta versão foi significativamente refatorada e aprimorada com novas regras de negócio e a dimensão do tempo.

## 🌟 Destaques da Versão 1.2.0

Esta versão foca na robustez das regras de negócio e em uma experiência do usuário (UX) mais informativa:

* **Registro de Tempo:** Todas as transações agora registram a data e hora exatas da operação.
* **Extrato Detalhado:** O extrato exibe o histórico de movimentações com a data e hora formatada em padrão brasileiro (DD/MM/AAAA HH:MM).
* **Bloqueio Inteligente:** A mensagem de limite excedido informa ao usuário a data e hora exata em que o limite será redefinido, baseada na hora da última transação.
* **Estrutura Centralizada:** Utiliza um dicionário (`conta`) para centralizar o estado e as configurações do sistema, facilitando a manutenção.

## 🚀 Funcionalidades e Regras de Negócio

| Funcionalidade       | Regras de Negócio Implementadas                                                                                                                                                            |
|:-------------------- |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Depósito** (`[d]`) | Sujeito ao **Limite de Transações Diárias** (10). Aceita apenas valores positivos. Registra data e hora.                                                                                   |
| **Saque** (`[s]`)    | Limite de **3 saques por dia** e valor máximo de **R$ 500,00** por saque. Sujeito ao **Limite de Transações Diárias** (10). Registra data e hora.                                          |
| **Extrato** (`[e]`)  | Visualiza o histórico de transações, incluindo data e hora. Sempre acessível, mesmo após atingir os limites de movimentação.                                                               |
| **Limite Diário**    | **Limite de 10 transações** (Depósito + Saque) por dia. Ao atingir o limite, o usuário é bloqueado para novas movimentações e informado da data e hora exata para o retorno (próximo dia). |

## 🛠️ Arquitetura e Tecnologias

O projeto utiliza:

* **Python 3.x** e o módulo `datetime` para manipulação de tempo.
* **Estrutura de Dados:** Dicionário (`conta`) para gerenciar o estado e configurações.
* **Modularização:** Funções recebem o estado da conta como parâmetro, mantendo o código organizado.

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

3. **Interaja com o Menu:**
   O sistema exibirá um menu interativo onde você pode escolher entre as opções `[d]`, `[s]`, `[e]` ou `[q]`.

4. 

## 📚 Próximos Passos (Próxima Versão - V2)

Os planos para a V2 se consolidam no próximo desafio do bootcamp:

1. **Programação Orientada a Objetos (POO):** Migrar a arquitetura atual (dicionário) para um modelo com Classes (`Conta`, `Cliente`, `Historico`) para encapsulamento e melhor design de código.
2. **Múltiplos Usuários:** Implementar o cadastro e login para múltiplos clientes.

---

Feito com ❤️ e 🐍 por Wesley Treib Jacques
