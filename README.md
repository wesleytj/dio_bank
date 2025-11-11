# 🏦 DIO Bank - Sistema Bancário POO Modularizado (Versão 3.0.0)

Projeto didático que evoluiu de uma implementação procedural para uma arquitetura orientada a objetos (POO) e, agora, para um **pacote Python modularizado e extensível**.

Este projeto implementa as principais entidades e operações bancárias (`Cliente`, `Conta`, `Transacao`), separadas em módulos coesos, e adiciona uma funcionalidade de câmbio de moeda em um pacote utilitário externo.

---

## ➤ Arquitetura e Estrutura

O código foi refatorado e organizado no pacote principal `dio_bank`, seguindo o princípio de responsabilidade única:

* **`dio_bank/models/`**: Contém todas as classes de domínio (`Cliente`, `Conta`, `Transacao`, `Historico`) que definem o sistema bancário.
* **`dio_bank/currency_converter_package/`**: Novo pacote utilitário, totalmente desacoplado do domínio bancário, responsável apenas pela lógica de conversão de moedas.
* **`dio_bank/main.py` e `run.py`**: Arquivos de interface e execução do sistema.

---

## 🚀 Funcionalidades da Versão 3.0.0

### 1. Operações Bancárias POO (Base)

* **Clientes:** Criação de clientes `PessoaFisica`.
* **Contas:** Criação de `ContaCorrente` (Agência `0001`, número sequencial).
* **Transações:** Depósito e Saque registrados como classes (`Deposito`, `Saque`) que utilizam o padrão *Strategy* para interagir com a conta.
* **Limites de Saque:** Validação de limite por operação (R$ 500,00) e limite de 3 saques diários.
* **Extrato:** Exibição completa do histórico de transações com data/hora e saldo final.

### 2. Novo Módulo: Conversor de Moedas (Câmbio)

* Permite a conversão entre o Real (BRL) e moedas estrangeiras (USD, EUR, GBP, ARS).
* As taxas são simuladas e mantidas em um módulo separado, facilitando a atualização futura (simulação de taxas: 1 X = TAXA em BRL).

---

## 💡 Como Executar (Modularizado)

Para rodar o sistema modularizado, você deve executar o pacote principal a partir da **raiz do projeto** utilizando a *flag* `-m` do Python.

1. **Clone o Repositório:**
   
   ```bash
   git clone https://github.com/wesleytj/dio_bank.git
   cd dio_bank/
   ```

2. **Execute o Módulo `run`:**
   
   ```bash
   python -m dio_bank.run
   ```

---

## ⚙️ Notas Técnicas e Próximos Passos

* **Modo Teste:** A função `main()` em `dio_bank/main.py` possui a variável `modo_teste_`. Altere para `True` para iniciar com um cliente e conta pré-cadastrados, ideal para testes rápidos.
* **Próximo Passo:** Implementar a persistência de dados (JSON ou SQL) e adicionar a funcionalidade de Câmbio ao menu principal do banco.

---

**Feito com ❤️ e 🐍 por Wesley Treib Jacques**
