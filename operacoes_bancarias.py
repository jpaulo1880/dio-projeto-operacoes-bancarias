# Dados da conta bancária do usuário
saldo = 5000
limite_saque_por_sessao = 500
total_saque_por_sessao = 0
lista_de_depositos = []
lista_de_saques = []

# Função depósito


def op_deposito(saldo, lista_de_depositos):
    while True:
        try:

            deposito = float(input("Insira o valor de depósito: R$ "))

            if deposito > 0:
                saldo += deposito
                # Adiciona depósito no registro do extrato
                lista_de_depositos.append(deposito)
                print(f"Depósito realizado com sucesso. Seu saldo é R$ {
                      saldo:.2f}")

            else:
                print("O valor do depósito deve ser positivo. Tente novamente.")
                continue

        # Verifica se o usuário tentou usar um valor que não seja número
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")
            continue

        fim_op_deposito = int(
            input("Tecle 0 para retornar ou 1 para continuar: "))

        if fim_op_deposito == 0:
            return

        elif fim_op_deposito != 1:
            print("Opção inválida. Tente novamente.")
            return

# Função saque


def op_saque(saldo, lista_de_saques, total_saque_por_sessao):
    while True:
        try:

            saque = float(input("Insira o valor do saque: R$ "))

            if saque > saldo:
                print("Saldo insuficiente. Tente novamente")
                continue

            elif saque > 500:
                print("Saque excede o limite. Tente novamente")
                continue

            # Validação se número de saques < 3
            elif total_saque_por_sessao == 3:
                print("Limite de saques atingido.")
                return

            elif saque <= 0:
                print("Não é possivel sacar valores negativos. Tente novamente.")
                continue

            else:
                saldo -= saque
                # Adiciona Op. de saque ao extrato
                lista_de_saques.append(saque)
                total_saque_por_sessao += 1
                print(
                    f"Saque realizado com sucesso. O saldo restante é R$ {
                        saldo:.2f}."
                )

        except ValueError:
            print("Opção inválida. Tente novamente.")
            continue

        fim_op_saque = int(
            input("Tecle 0 para retornar ou 2 para continuar: ")
        )

        if fim_op_saque == 0:
            return

        else:
            continue

# Função extrato


def op_extrato(saldo, lista_de_depositos, lista_de_saques):

    # Verifica se há valores no extrato
    if lista_de_depositos or lista_de_saques:
        print("Lista de depósitos realizados:")

        # Usa loop for para checar se há itens na lista
        for deposito in lista_de_depositos:
            print(f" - R$ {deposito:.2f}")
        print("Lista de saques realizados:")

        for saque in lista_de_saques:
            print(f" - R$ {saque:.2f}")
        print(f"Seu saldo atual é R$ {saldo:.2f}.")

    else:
        print("Sem movimentações no período. Voltando ao menu.")


# Menu principal interativo
while True:
    try:

        menu_opcoes_validas = [0, 1, 2, 3]
        print(
            """
==========================
1 - Depósito
2 - Saque
3 - Extrato
0 - Sair
==========================
  """
        )
        menu_op_selecionada = int(input("Selecione a opção desejada: "))

        if menu_op_selecionada == 1:
            op_deposito(saldo, lista_de_depositos)

        elif menu_op_selecionada == 2:
            op_saque(saldo, lista_de_saques, total_saque_por_sessao)

        elif menu_op_selecionada == 3:
            op_extrato(saldo, lista_de_depositos, lista_de_saques)

        elif menu_op_selecionada not in menu_opcoes_validas:
            print("Opção inválida, tente novamente.")
            continue

        if menu_op_selecionada == 0:
            print(
                """
==================================
Obrigado por usar nossos serviços.
==================================
    """
            )
            break

    except ValueError:
        print("Escolha uma opção válida.")
