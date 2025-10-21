# 🏦 Sistema Bancário em Python (DIO Bank - Versão 1.1.0)

Um projeto desenvolvido em Python que simula as operações básicas de um sistema bancário: Depósito, Saque e Visualização de Extrato. Esta versão foi **refatorada** para melhorar a organização do código e a modularidade.

## 🌟 Destaques da Versão 1.1.0

Esta versão representa uma grande evolução estrutural e de regras de negócio em relação à V1:

* **Estrutura Refatorada:** Migração de variáveis globais para um **Dicionário Centralizado (`conta`)** que armazena o estado e as regras de configuração.
* **Novas Regras de Limite:** Implementação do **Limite de Transações Diárias** (total de depósitos + saques).
* **Melhor Lógica de Bloqueio:** As operações de consulta (Extrato) não são mais bloqueadas ao atingir limites.

## 🚀 Funcionalidades e Regras de Negócio

O sistema implementa as seguintes regras de operação:

| Funcionalidade       | Descrição e Regras                                                                                                                                                                                                                                        |
|:-------------------- |:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Depósito** (`[d]`) | Permite adicionar fundos à conta. <br> **Regra Nova:** Sujeito ao **Limite de Transações Diárias**.                                                                                                                                                       |
| **Saque** (`[s]`)    | Permite retirar fundos da conta. <br> <ul><li>Limite de **3 saques** por dia (Configurável).</li><li>Valor máximo de **R$ 500,00** por saque (Configurável).</li><li>Verificação de saldo.</li><li>Sujeito ao **Limite de Transações Diárias**.</li></ul> |
| **Extrato** (`[e]`)  | Visualiza o histórico de transações e saldo atual. <br> **Melhoria:** Sempre acessível, mesmo após limites de movimentação.                                                                                                                               |
| **Sair** (`[q]`)     | Encerra a execução do sistema.                                                                                                                                                                                                                            |

## 🛠️ Tecnologias e Arquitetura

O projeto foi refatorado utilizando:

* **Python 3.x** e sintaxe `match/case` para telas (se versão 3.10+).
* **Estrutura de Dados:** Dicionário para encapsular o estado da conta e as configurações.
* **Modularização:** Funções recebem o estado da conta como parâmetro, diminuindo a dependência de variáveis globais.

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

Os planos para a V2 agora se concentram em aprimoramentos mais avançados, como:

1. **Programação Orientada a Objetos (POO):** Substituir o dicionário de estado por classes e métodos para encapsular a lógica de conta, cliente e histórico.
2. **Tratamento de Exceções:** Implementar validação de entrada robusta (ex: evitar erros ao digitar letras em valores numéricos).
3. **Novas Funcionalidades:** Adicionar recursos como múltiplos usuários e contas.

---

Feito com ❤️ e 🐍 por Wesley Treib Jacques
