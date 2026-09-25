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
   git clone [https://github.com/SEU_USUARIO/Desafio-sistema-bancario-python.git](https://github.com/SEU_USUARIO/Desafio-sistema-bancario-python.git)
