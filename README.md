# Desafio: Sistema Bancário em Python

Projeto desenvolvido como parte do desafio da DIO (NTT DATA), com o objetivo de implementar operações fundamentais de um sistema bancário utilizando a linguagem Python.

## 📌 Funcionalidades
- **Depósito:** Permite realizar depósitos de valores positivos no saldo.
- **Saque:** Permite realizar saques respeitando o limite diário de operações e o valor máximo por saque.
- **Extrato:** Exibe o histórico de movimentações e o saldo atual da conta.
- **PIX:** Funcionalidade de transferência via PIX.
- **Simulação de Rendimentos:** Simulação de rendimento do saldo.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.x
- **Ambiente de Desenvolvimento:** Visual Studio Code / GitHub Desktop

## 🚀 Como Executar o Projeto
1. Certifique-se de ter o Python instalado na sua máquina.
2. Clone o repositório:
   ```bash
   git clone [https://github.com/wagnerss13-afk/Desafio-sistema-bancario-python.git](https://github.com/wagnerss13-afk/Desafio-sistema-bancario-python.git)

# Sistema Bancário em Python - Versão 2 (Modularizado)

Projeto desenvolvido como parte do desafio do bootcamp na **DIO (Digital Innovation One)**. A versão 2 evoluiu o script inicial para uma estrutura modular baseada em funções e introduziu o cadastro de usuários (clientes) e contas bancárias.

## 🚀 Funcionalidades da Versão 2

- **Modularização por Funções:**
  - `depositar`: Entrada de valores com passagem de argumentos *positional-only* (`/`).
  - `sacar`: Validação de saldo, limite por saque e limite diário com argumentos *keyword-only* (`*`).
  - `exibir_extrato`: Exibição dos lançamentos e saldo com combinação de argumentos posicionais e nomeados.
- **Gestão de Clientes e Contas:**
  - `criar_usuario`: Cadastro de clientes com validação de CPF único.
  - `criar_conta`: Vinculação de novas contas (Agência `0001`) a usuários já cadastrados.
  - `listar_contas`: Listagem de todas as contas cadastradas com os dados do titular.

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Git & GitHub** (Versionamento de código)

## 💻 Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone [https://github.com/wagnerss13-afk/Desafio-sistema-bancario-python.git](https://github.com/wagnerss13-afk/Desafio-sistema-bancario-python.git)

   # DIO | Otimizando o Sistema Bancário com Python

[![DIO](https://img.shields.io/badge/DIO-Bootcamp-orange?style=for-the-badge&logo=github)](https://dio.me)
[![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen?style=for-the-badge)](#)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](./LICENSE)

---

## 📌 Sobre o Projeto

Este projeto faz parte dos desafios práticos da **[DIO (Digital Innovation One)](https://dio.me)**, evoluindo o sistema bancário procedural em Python. O código foi expandido com modularização por funções estritas (`/` e `*`), adição de novos serviços bancários modernos e rastreabilidade total das operações.

> *"Codifique o seu futuro global agora."*

---

## 🚀 Novas Funcionalidades e Melhorias

- **Serviço de PIX (`[p]`):** Permite realizar transferências (enviar) e recebimentos utilizando chaves PIX integradas ao saldo e ao cheque especial.
- **Cheque Especial:** Concede limite de crédito adicional automático quando o saldo fica negativo, exibindo relatórios detalhados do uso e do limite restante.
- **Extrato Detalhado com Timestamp:** Todas as transações (Depósitos, Saques e PIX) registram automaticamente a data e a hora exata da operação.
- **Gestão de Usuários e Contas:** Cadastro completo de clientes por CPF único e abertura de contas correntes vinculadas à agência padrão `0001`.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Biblioteca nativa:** `textwrap`, `datetime`
- **Controle de Versão:** Git & GitHub Desktop

---

## ⚙️ Como Executar o Projeto

1. **Clone este repositório:**
   ```bash
   git clone [https://github.com/wagnerss13-afk/Desafio-sistema-bancario-python.git](https://github.com/wagnerss13-afk/Desafio-sistema-bancario-python.git)


