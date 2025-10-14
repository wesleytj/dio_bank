# 🏦 Sistema Bancário em Python (DIO Bank - Versão 1)

Um projeto desenvolvido em Python que simula as operações básicas de um sistema bancário: Depósito, Saque e Visualização de Extrato. Este é a **primeira versão (V1)**, focada em atender os requisitos mínimos do desafio.

## 🌟 Destaques do Projeto

Este sistema, apelidado de "DIO Bank", foi construído em Python puro e segue a arquitetura solicitada pelo desafio, utilizando funções para modularizar as operações e estruturas de controle para implementar as regras de negócio.

## 🚀 Funcionalidades

O sistema implementa três operações principais com regras específicas:

| Funcionalidade       | Descrição                            | Regras de Negócio                                                                                                                |
|:-------------------- |:------------------------------------ |:-------------------------------------------------------------------------------------------------------------------------------- |
| **Depósito** (`[d]`) | Permite adicionar fundos à conta.    | Aceita apenas valores positivos.                                                                                                 |
| **Saque** (`[s]`)    | Permite retirar fundos da conta.     | <ul><li>Limite de **3 saques** por dia.</li><li>Valor máximo de **R$ 500,00** por saque.</li><li>Verificação de saldo.</li></ul> |
| **Extrato** (`[e]`)  | Visualiza o histórico de transações. | Exibe todos os depósitos e saques, além do saldo atual no formato `R$ xxx.xx`. Exibe mensagem se não houver movimentações.       |
| **Sair** (`[q]`)     | Encerra a execução do sistema.       |                                                                                                                                  |

## 🛠️ Tecnologias Utilizadas

O projeto foi desenvolvido inteiramente com:

* **Python 3.x**
* Utilização de variáveis globais (para estado do sistema) e funções (para modularização).

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

## 📚 Próximos Passos (Próxima Versão - V2)

Apesar de funcional, esta V1 será a base para aprimoramentos futuros. As melhorias planejadas incluem:

1. **Melhores Práticas de Código:**
   * Substituir o uso de variáveis globais por classes e métodos (Programação Orientada a Objetos) para encapsular o estado da conta.
   * Uso de *docstrings* e tipagem para melhor legibilidade.
2. **Refatoração do Extrato:**
   * Utilizar passagem de argumentos em vez de depender de variáveis globais para a função de extrato.
3. **Tratamento de Exceções:**
   * Implementar validação de entrada robusta (ex: evitar erros ao digitar letras em valores numéricos).

## 🔗 Referência Utilizada

Para aprimoramento e consultas durante o desenvolvimento, foi utilizado o seguinte recurso:

* [W3Schools Python Tutorial](https://www.w3schools.com/python/default.asp) - Referência em sintaxe e funções básicas de Python.

---

Feito com ❤️ e 🐍 por Wesley Treib Jacques
