# Funcão para menu input
"""
A função não exige nenhuns argumentos .
Vai imprimir o menu e exige usuário digitar uma opcão
"""


def menu_function():
    print("MENU".center(31, "*"))
    menu = """
    [D] Depositar
    [S] Sacar
    [E] Extrato
    [Q] Sair
    [CU] Criar Usuário
    [CC] Criar Conta (corrente)

    => """
    print(menu)
    return input(menu)


# Funcão para depositar
""" 
A função exige os 3 argumentos (tipo de keyword).
Todos os argumentos estão descritos sob funcão principal.
A função vai aumentar o saldo se o valor (digitado por usuário) for o número positivo.
Caso contrário vai terminar operação e vai mostrar um aviso sobre o valor inválido.
"""


def depositar(saldo, valor, extrato):  # usa argumentos posicionais
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return print(saldo, "\n", extrato)  # retorna valores para saldo e extrato


# Funcão para sacar
""" 
A função exige os 6 argumentos (tipo de keyword).
Todos os argumentos estão descritos sob funcão principal.
A função vai permitir o processo de sacar dinheiro se:
1. Saldo Suficiente
2. Limite de Valor não é mais do que limite permitido
3. Limite de Saques Diários não excedeu.
Se todas as validações passarem e o valor for positivo, 
o saldo é deduzido, o extrato é atualizado com o registro do saque
e a contagem de numero_saques é incrementada.
"""


def sacar(
    *, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES
):  # usa argumentos tipo do keyword
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return print(saldo, "\n", extrato)  # retorna valores para saldo e extrato


# Funcão para extrato
""" 
A função exige os 2 argumentos - o saldo (integer, tipo de posicional) e o extrato (string, tipo de keyword).
Todos os argumentos estão descritos sob funcão principal.
A função vai formatar e imprimir na tela o extrato bancário.
"""


def extrato(saldo, /, *, extrato):  # usa argumentos posicionais e tipo do keyword
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


# Funcão para criar um usuário
""" 
A função exige só um argumento - uma lista de usuários (tuple).
Todos os argumentos estão descritos sob funcão principal.
A função vai coletar dados do usuário, validar se o CPF já existe no sistema 
e, se tudo estiver correto, retornar um novo dicionário de usuário.
"""


def criar_usuário(usuários_tuple):
    cpf = input("Por favor, digite o seu cpf (sem pontos e taço): ")
    usuário_existe = False
    for usuário in usuários_tuple:
        if usuário["cpf"] == cpf:
            usuário_existe = True
            print("Erro: usuário já existe. Você voltará ao menu")
            return None
    data_nasc = input("Por favor, digite a sua data de nascimento: ")
    nome = input("Por favor, digite o seu nome: ")
    print("Por favor, digite o seu endereço em 4 passos: ")
    logradouro = input("1. Logradouro: ")
    número = input("2. Número: ")
    bairro = input("3. Bairro: ")
    cidade_sigla_estado = input("4. Cidade / Sigla Estado: ")
    endereço = {
        "logradouro": logradouro,
        "número": número,
        "bairro": bairro,
        "cidade_sigla_estado": cidade_sigla_estado,
    }
    print(
        f"Confera os seus dados CPF - {cpf}, Data de nascimento - {data_nasc}, Nome - {nome}, Endereço - {endereço}"
    )  # um passo para verificar os dados digitados
    sanity_check = input(
        """
                         Se os dados estão corretos digite - S
                         Se os dados estão errados digite - N
                         """
    )
    if (
        sanity_check.upper() == "S"
    ):  # if loop para cobrir um caso quando os dados foram digitado errado
        return {
            "cpf": cpf,
            "data_nasc": data_nasc,
            "nome": nome,
            "endereço": endereço,
        }
    else:
        return criar_usuário(usuários_tuple)


# Funcão para criar uma conta (corrente).
""" 
A função exige os 3 argumentos - uma lista de usuários (tuple), número da agência e uma lista das contas.
Todos os argumentos estão descritos sob funcão principal.
A função orienta o usuário sobre os passos necessários para abrir uma conta,
verificando primeiro se ele já possui um cadastro de usuário (CPF).
Pergunta ao usuário se ele já é cadastrado ("S/N").
Caso o usuário não seja cadastrado, a função exibe uma mensagem e chama
a função externa criar_usuário() para iniciar o processo de registro do cliente.
Localização de Usuário Existente (Se "S"):
1. Pede o CPF do usuário.
2. Itera sobre a usuários_tuple para encontrar uma correspondência de CPF.
3. Se encontrar o CPF, cria uma nova tupla conta_corrente_usuário contendo a Agência,
um ID sequencial baseado no índice do usuário (i), e o nome do usuário.
A função vai return os detalhes da nova conta e a concatenada à contas_tuple existente.
"""


def criar_conta_corrente(usuários_tuple, Agência, contas_tuple):
    cadastre_flag = input("Tinha cadastre-se (S/N): ")
    if cadastre_flag.upper() == "N":
        print(
            """
              Precisamos criar uma conta pra você!
              Siga as instrucões.
              """
        )
        criar_usuário(usuários_tuple)
    else:
        id = input("Por favor, digite o seu cpf (sem pontos e taço): ")
        for usuário in usuários_tuple:
            if usuário["cpf"] == id:
                i = usuários_tuple.index(usuário) + 1
                conta_corrente_usuário = (Agência, i, usuário["nome"])
                print(
                    f"Aqui estão os seus detalhes da conta criada: {conta_corrente_usuário}"
                )
                return contas_tuple + conta_corrente_usuário
        print("Erro: usuário não existe. Você voltará ao menu")
        return menu_function()


# Funcão para iniciar a programa bancaria .
"""
A função programa - lógica do sistema bancário, 
permitindo que o usuário 6 operações (lançar menu, depositar, 
sacar, pedir extrato, criar novo usuário e nova conta corrente).
"""


def programa():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    Agência = "0001"
    usuários_tuple = ()  # usa tuple para evitar mudança de dados
    contas_tuple = ()  # usa tuple para evitar mudança de dados
    while (
        True
    ):  # Loop Principal: while True executa o menu do programa repetidamente até que o usuário escolha sair.

        opcao = menu_function()
        if opcao.upper() == "D":
            valor = float(input("Informe o valor do depósito: "))
            depositar(saldo, valor, extrato)

        elif opcao.upper() == "S":
            valor = float(input("Informe o valor da retirada: "))
            sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES,
            )

        elif opcao.upper() == "E":
            extrato(saldo, extrato=extrato)
        elif opcao.upper() == "CU":
            novo_usuário = criar_usuário(usuários_tuple)
            if novo_usuário:
                usuários_tuple = usuários_tuple + (novo_usuário,)
        elif opcao.upper() == "CC":
            contas_tuple = criar_conta_corrente(usuários_tuple, Agência, contas_tuple)

        elif opcao.upper() == "Q":
            break

        else:
            print(
                "Operação inválida, por favor selecione novamente a operação desejada."
            )


programa()
