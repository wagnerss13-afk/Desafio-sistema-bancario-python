import datetime

menu = """
================ MENU BANCO DIGITAL ================
[d]  Depositar
[s]  Sacar
[pix] Transferência PIX
[e]  Extrato Detalhado
[inv] Simular Rendimento
[q]  Sair
====================================================
=> """

saldo = 0.0
limite_saque_diario = 500.0
cheque_especial = 1000.0  # Limite de crédito extra
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def obter_data_hora():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


while True:
    opcao = input(menu).strip().lower()

    # ---------------- DEPÓSITO ----------------
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += (
                f"[{obter_data_hora()}] Depósito:          +R$ {valor:.2f}\n"
            )
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    # ---------------- SAQUE ----------------
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: R$ "))
        saldo_total_disponivel = saldo + cheque_especial

        excedeu_saldo_e_limite = valor > saldo_total_disponivel
        excedeu_limite_saque = valor > limite_saque_diario
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo_e_limite:
            print(
                "\n@@@ Operação falhou! Saldo e Cheque Especial insuficientes. @@@"
            )

        elif excedeu_limite_saque:
            print(
                f"\n@@@ Operação falhou! O valor excede o limite por operação (R$ {limite_saque_diario:.2f}). @@@"
            )

        elif excedeu_saques:
            print(
                "\n@@@ Operação falhou! Número máximo de saques diários atingido. @@@"
            )

        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += (
                f"[{obter_data_hora()}] Saque:             -R$ {valor:.2f}\n"
            )
            print("\n=== Saque realizado com sucesso! ===")
            if saldo < 0:
                print(
                    f"⚠️  Atenção: Você está usando R$ {abs(saldo):.2f} do seu Cheque Especial!"
                )

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    # ---------------- PIX ----------------
    elif opcao == "pix":
        chave_pix = input("Informe a chave PIX de destino (CPF/E-mail/Tel): ")
        valor = float(input("Informe o valor da transferência PIX: R$ "))
        saldo_total_disponivel = saldo + cheque_especial

        if valor <= 0:
            print("\n@@@ Operação falhou! Valor inválido. @@@")
        elif valor > saldo_total_disponivel:
            print(
                "\n@@@ Operação falhou! Saldo e Cheque Especial insuficientes. @@@"
            )
        else:
            saldo -= valor
            extrato += f"[{obter_data_hora()}] PIX Enviado ({chave_pix[:10]}...): -R$ {valor:.2f}\n"
            print(
                f"\n=== PIX de R$ {valor:.2f} enviado com sucesso para {chave_pix}! ==="
            )
            if saldo < 0:
                print(
                    f"⚠️  Atenção: Você entrou no Cheque Especial (Uso: R$ {abs(saldo):.2f})!"
                )

    # ---------------- EXTRATO ----------------
    elif opcao == "e":
        print("\n================ EXTRATO BANCÁRIO ================")
        print(
            "Não foram realizadas movimentações."
            if not extrato
            else extrato
        )
        print("--------------------------------------------------")
        print(f"Saldo em conta:          R$ {saldo:.2f}")

        # Exibição inteligente do Cheque Especial
        if saldo < 0:
            usado = abs(saldo)
            restante = cheque_especial - usado
            print(
                f"Cheque Especial Usado:   R$ {usado:.2f} (Limite restante: R$ {restante:.2f})"
            )
        else:
            print(f"Cheque Especial Disp.:   R$ {cheque_especial:.2f}")

        print(f"Total Disponível:        R$ {saldo + cheque_especial:.2f}")
        print("==================================================")

    # ---------------- RENDIMENTO DE POUPANÇA ----------------
    elif opcao == "inv":
        if saldo > 0:
            taxa_rendimento = 0.005  # 0.5% ao mês
            rendimento = saldo * taxa_rendimento
            saldo += rendimento
            extrato += f"[{obter_data_hora()}] Rendimento (0.5%):  +R$ {rendimento:.2f}\n"
            print(
                f"\n=== Rendimento aplicado! Seu dinheiro rendeu R$ {rendimento:.2f}. ==="
            )
        else:
            print(
                "\n@@@ Rendimento não aplicado. É necessário ter saldo positivo na conta. @@@"
            )

    # ---------------- SAIR ----------------
    elif opcao == "q":
        print("\nObrigado por utilizar o nosso Banco Digital. Até logo!")
        break

    else:
        print(
            "\n@@@ Operação inválida, por favor selecione novamente a opção desejada. @@@"
        )