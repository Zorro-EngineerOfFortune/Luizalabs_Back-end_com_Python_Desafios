from abc import ABC, abstractmethod
from datetime import datetime


class Cliente:
    # Classe base para clientes.
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = [] # Armazena uma lista de objetos 'Conta' associados ao cliente.

    def realizar_transacao(self, conta, transacao):
        # O cliente delega o registro da transação ao próprio objeto transação.
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    # Implementação concreta de Cliente para uma pessoa física.
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    # Classe base para contas bancárias.
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001" # Número de agência fixo.
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        # Método de fábrica para criar uma nova instância de conta.
        return cls(numero, cliente)

    @property
    def saldo(self):
        # Propriedade somente leitura para _saldo.
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        # Lógica básica de saque (limites aplicados em subclasses).
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True


class ContaCorrente(Conta):
    # Conta especializada com limites de saque e cheque especial (limite).
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        # Método polimórfico: Sobrescreve Conta.sacar para aplicar limites adicionais.
        # Conta o número de saques ('Saque') no histórico.
        numero_saques = len(
            [
                transacao
                for transacao in self.historico.transacoes
                if transacao["tipo"] == Saque.__name__
            ]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            # Chama o método da classe base (Conta.sacar) para o saque real e verificação de saldo.
            return super().sacar(valor)

        return False

    def __str__(self):
        # Representa o objeto como string para exibição/impressão.
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    # Registra todas as transações de uma conta.
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        # Propriedade somente leitura para a lista de transações.
        return self._transacoes

    def adicionar_transacao(self, transacao):
        # Adiciona uma representação em dicionário da transação à lista.
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                # Observação: O formato de data/hora pode ser não convencional (%s é timestamp).
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )


class Transacao(ABC):
    # Classe Base Abstrata para todas as transações.
    @property
    @abstractmethod
    def valor(self):
        # Força classes concretas a implementarem uma propriedade 'valor'.
        pass

    @classmethod
    @abstractmethod
    def registrar(self, conta):
        # Força classes concretas a implementarem um método 'registrar'.
        # Nota: Está definido como @classmethod e @abstractmethod, mas implementado
        # como método de instância nas classes concretas.
        pass


class Saque(Transacao):
    # Transação concreta: Saque.
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        # Tenta executar o saque na conta.
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            # Só registra a transação se 'conta.sacar' retornar True.
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    # Transação concreta: Depósito.
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        # Tenta executar o depósito na conta.
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            # Só registra a transação se 'conta.depositar' retornar True.
            conta.historico.adicionar_transacao(self)
