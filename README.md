# 🏦 Sistema Bancário em Python (DIO Bank - Versão 2.0.0)

Um projeto que evoluiu da arquitetura procedural simples (V1) para uma **arquitetura modular funcional** (V2), implementando funções específicas para operações (Depósito, Saque, Extrato) e funções para a gestão de entidades (Usuários e Contas).

A principal mudança é a separação das responsabilidades e a aplicação de boas práticas de Python, como o uso de **argumentos posicionais e *keyword*** (posição-única e nome-único) nas funções de transação.

## 🌟 Destaques da Versão 2.0.0

* **Modularização Avançada:** Uso de funções separadas para cada tarefa, incluindo a gestão de entidades (`filtrar_usuario`, `criar_usuario`, `criar_conta_corrente`).
* **Controle de Transações Diárias:** Implementado um novo limite para o total de transações (`Depósito` + `Saque`) por dia.
* **Boas Práticas:** Uso de argumentos *Positional-Only* (`/`) e *Keyword-Only* (`*`) nas assinaturas de funções (`depositar` e `sacar`).
* **Geração Sequencial de Contas:** Remoção de variáveis globais complexas, utilizando o tamanho da lista de contas para garantir a numeração sequencial.

## 🚀 Funcionalidades e Regras de Negócio

| Funcionalidade           | Tipo                 | Descrição                            | Regras de Negócio                                                                                                                |
|:------------------------ |:-------------------- |:------------------------------------ |:-------------------------------------------------------------------------------------------------------------------------------- |
| **Depósito** (`[d]`)     | Positional-Only      | Adiciona fundos à conta.             | Aceita apenas valores positivos.                                                                                                 |
| **Saque** (`[s]`)        | Keyword-Only         | Retira fundos da conta.              | <ul><li>Limite de **3 saques** por dia.</li><li>Valor máximo de **R$ 500,00** por saque.</li><li>Verificação de saldo.</li></ul> |
| **Transações** (Geral)   | -                    | -                                    | Limite de **10 transações** (Depósito/Saque) por dia.                                                                            |
| **Extrato** (`[e]`)      | Positional + Keyword | Visualiza o histórico e saldo.       | Exibe data/hora e valores formatados.                                                                                            |
| **Novo Usuário** (`[c]`) | -                    | Cria um novo cliente.                | CPF deve ser único no sistema.                                                                                                   |
| **Nova Conta** (`[n]`)   | -                    | Vincula uma conta 0001 a um usuário. | Conta é sequencial e exige usuário existente.                                                                                    |

---

## 💡 Como Executar

Para rodar o sistema em sua máquina local, siga os passos abaixo:

1. **Clone o Repositório:**
   
   ```bash
   git clone [https://github.com/seu-usuario/sistema_bancario.git](https://github.com/seu-usuario/sistema_bancario.git)
   cd sistema_bancario
   ```

2. **Execute o Arquivo Python:**
   
   ```bash
   python banking_system.py
   ```

---

## ⚙️ Nota Importante: Modo de Teste

O arquivo `banking_system.py` na função `main()` contém a variável `modo_teste_ = True`.

**Com `modo_teste_ = True` (Padrão):** 

Uma conta genérica (Ag 0001 | C/C 1) e seu usuário são criados automaticamente para permitir testes imediatos de depósito/saque/extrato.

**Para Desativar:** Altere `modo_teste_` para `False` em `main()`. 

O sistema iniciará sem contas cadastradas, exigindo que você use as opções `[c]` (Novo Usuário) e `[n]` (Nova Conta) antes de fazer qualquer transação.

---

## 📚 Próximos Passos (V3 - POO)

 O próximo e mais importante passo é a refatoração para **Programação Orientada a Objetos (POO)**. 

As listas globais (`usuarios` e `contas`) serão substituídas por classes (`Cliente`, `Conta`, etc.) e a gestão de estado será feita através de instâncias de objetos, eliminando de vez o uso de variáveis globais.

---

**Feito com ❤️ e 🐍 por Wesley Treib Jacques**


