import textwrap
from datetime import datetime


def menu():
    menu_text = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [p]\tPIX (Transferir / Receber)
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu_text))


def obter_data_hora():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"[{obter_data_hora()}] Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques, cheque_especial):
    excedeu_limite_operacao = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    saldo_disponivel_total = saldo + cheque_especial
    excedeu_saldo_total = valor > saldo_disponivel_total

    if excedeu_saldo_total:
        print("\n@@@ Operação falhou! Saldo insuficiente (mesmo considerando o Cheque Especial). @@@")

    elif excedeu_limite_operacao:
        print("\n@@@ Operação falhou! O valor do saque excede o limite por operação. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        numero_saques += 1

        if saldo < 0:
            usado_cheque = abs(saldo)
            extrato += f"[{obter_data_hora()}] Saque:\t\tR$ {valor:.2f} (Uso do Cheque Especial: R$ {usado_cheque:.2f})\n"
        else:
            extrato += f"[{obter_data_hora()}] Saque:\t\tR$ {valor:.2f}\n"

        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato, numero_saques


def realizar_pix(*, saldo, valor, tipo_pix, chave_pix, extrato, cheque_especial):
    saldo_disponivel_total = saldo + cheque_especial

    if tipo_pix == "1":  # Enviar PIX
        if valor > saldo_disponivel_total:
            print("\n@@@ Operação falhou! Saldo e Cheque Especial insuficientes para transferência PIX. @@@")
        elif valor > 0:
            saldo -= valor
            if saldo < 0:
                usado_cheque = abs(saldo)
                extrato += f"[{obter_data_hora()}] PIX Enviado:\tR$ {valor:.2f} para {chave_pix} (Uso Cheque Especial: R$ {usado_cheque:.2f})\n"
            else:
                extrato += f"[{obter_data_hora()}] PIX Enviado:\tR$ {valor:.2f} para {chave_pix}\n"
            print("\n=== PIX enviado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! Valor inválido. @@@")

    elif tipo_pix == "2":  # Receber PIX
        if valor > 0:
            saldo += valor
            extrato += f"[{obter_data_hora()}] PIX Recebido:\tR$ {valor:.2f} de {chave_pix}\n"
            print("\n=== PIX recebido com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! Valor inválido. @@@")

    else:
        print("\n@@@ Opção de PIX inválida! @@@")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato, cheque_especial):
    print("\n================ EXTRATO DETALHADO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print("--------------------------------------------------")
    print(f"Saldo em Conta:\t\tR$ {saldo:.2f}")

    if saldo < 0:
        uso_cheque = abs(saldo)
        limite_restante = cheque_especial - uso_cheque
        print(f"Cheque Especial Utilizado:\tR$ {uso_cheque:.2f}")
        print(f"Cheque Especial Disponível:\tR$ {limite_restante:.2f}")
    else:
        print(f"Cheque Especial Disponível:\tR$ {cheque_especial:.2f}")

    print(f"Saldo Total Disponível:\tR$ {max(0, saldo) + max(0, cheque_especial - abs(min(0, saldo))):.2f}")
    print("==================================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario,
            "cheque_especial": 200.00,  # Limite de Cheque Especial padrão por conta
        }

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    if not contas:
        print("\n@@@ Nenhuma conta cadastrada. @@@")
        return

    for conta in contas:
        linha = f"""\
            Agência:\t\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t\t{conta['usuario']['nome']}
            Cheque Especial:\tR$ {conta['cheque_especial']:.2f}
        """
        print("=" * 50)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0.0
    limite = 500.0
    cheque_especial = 200.00  # Limite concedido de Cheque Especial
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
                cheque_especial=cheque_especial,
            )

        elif opcao == "p":
            print("\n[1] Enviar PIX\n[2] Receber PIX")
            tipo_pix = input("Opção: ")
            chave_pix = input("Informe a Chave PIX / Origem: ")
            valor = float(input("Informe o valor do PIX: "))

            saldo, extrato = realizar_pix(
                saldo=saldo,
                valor=valor,
                tipo_pix=tipo_pix,
                chave_pix=chave_pix,
                extrato=extrato,
                cheque_especial=cheque_especial,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato, cheque_especial=cheque_especial)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


if __name__ == "__main__":
    main()