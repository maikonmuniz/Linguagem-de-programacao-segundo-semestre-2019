# Linguagem de Programação II
# AC06 SI2A - ADS2B - Banco
#
# Alunos: maikon.silva@aluno.faculdadeimpacta.com.br
#         catarina.sousa@aluno.faculdadeimpacta.com.br
#         felipe.augusto@aluno.faculdadeimpacta.com.br


from typing import Union, List, Dict

Number = Union[int, float]


class Cliente():
    """
    Classe Cliente do Banco.

    possui os atributos: nome, telefone e email, todos privados
    caso o email não seja um email válido gera um ValueError,
    caso o telefone não seja um número gera um TypeError
    """

    def __init__(self, nome: str, telefone: int, email: str):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email

        if '@' not in self.__email:
            raise ValueError("email inválido")
        if type(self.__telefone) is not int:
            raise TypeError("telefone tem que ser inteiro")

    def get_nome(self) -> str:
        """Acessor do atributo Nome."""
        return self.__nome

    def get_telefone(self) -> int:
        """Acessor do atributo Telefone."""
        return self.__telefone

    def set_telefone(self, novo_telefone: int) -> None:
        """
        Mutador do atributo telefone, caso não receba um número,
        gera um TypeError
        """
        try:
            self.__telefone = int(novo_telefone)
        except TypeError:
            print("Digito errado do telefone, tem que ser um numero")

    def get_email(self) -> str:
        """Acessor do atributo Email."""
        return self.__email

    def set_email(self, novo_email: str) -> None:
        """
        Mutador do atributo Email, caso não receba um email válido
        gera um ValueError.
        """
        if novo_email in "@":
            self.__email = novo_email
        else:
            raise ValueError("email errado")


class Banco():
    """
    A classe Banco deverá receber um nome em sua construção e deverá
    implementar os métodos:
    * abre_contas: abre uma nova conta, atribuindo o numero da conta em ordem
    crescente.
    * lista_contas(): apresenta um resumo de todas as contas do banco
    DICA: mantenha uma variável interna que armazene todas as contas do banco
    DICA2: utilze a variável acima para gerar automaticamente o número das
    contas do banco
    """
    def __init__(self, nome: str):
        self.__nome = nome
        self.num_incrementa_conta = 1
        self.contas = []

    def get_nome(self) -> str:
        """Acessor do Atributo Nome."""
        return self.__nome

    def abre_conta(self, clientes: List[Cliente], saldo_ini: Number) -> None:
        """
        Método para abertura de nova conta, recebe os clientes
        e o saldo inicial.
        Caso o saldo inicial seja menor que 0 devolve um ValueError
        """
        if saldo_ini >= 0:
            self.saldo = saldo_ini
            self.conta = [self.num_incrementa_conta, clientes, self.saldo]
            self.conta = tuple(self.conta)
            self.contas.append(self.conta)
            self.num_incrementa_conta += 1
        else:
            raise ValueError("Valor inicial deve ser maior ou igual a zero")

    def lista_contas(self) -> List['Conta']:
        """Retorna a lista com todas as contas do banco."""
        return self.contas


class Conta():
    """
    Classe Conta.
    * Todas as operações (saque e deposito, e saldo inicial) devem aparecer
    no extrato como tuplas, exemplo ('saque', 100), ('deposito', 200) etc.
    * Caso o saldo inicial seja menor que zero deve lançar um ValueError
    * A criação da conta deve aparecer no extrato com o valor
    do saldo_inicial, exemplo: ('saldo_inicial', 1000)
    DICA: Crie uma variável interna privada para guardar as
    operaões feitas na conta
    """

    def __init__(self, clientes: List[Cliente], numero_conta: int,
                 saldo_inicial: Number):
        self.clientes = clientes
        self.numero_conta = numero_conta
        self.__extrato_op = list()

        if saldo_inicial >= 0:
            self.saldo = saldo_inicial
            tupla = ("saldo_inicial", self.saldo)
            self.__extrato_op.append(tupla)
        else:
            raise ValueError("Valor inválido")

    def get_clientes(self) -> List[Cliente]:
        '''
        Acessor para o atributo Clientes
        '''
        return self.clientes

    def get_saldo(self) -> Number:
        '''
        Acessor para o Atributo Saldo
        '''
        return self.saldo

    def get_numero(self) -> int:
        '''
        Acessor para o atributo Numero
        '''
        return self.numero_conta

    def saque(self, valor: Number) -> None:
        '''
        Método de saque da classe Conta, operação deve aparecer no extrato
        Caso o valor do saque seja maior que o saldo da conta,
        deve retornar um ValueError, e não efetuar o saque
        '''
        tupla_saque = ("saque", valor)

        if valor <= self.get_saldo():
            self.saldo -= valor
            self.__extrato_op.append(tupla_saque)
        else:
            raise ValueError("valor deve ser maior ou igual a zero")

    def deposito(self, valor: Number):
        '''
        Método depósito da classe Conta, operação deve aparecer no extrato
        '''
        self.saldo += valor
        tupla_deposito = ("deposito", valor)
        self.__extrato_op.append(tupla_deposito)

    def extrato(self):
        '''
        Retorna uma lista com as operações (Tuplas) executadas na Conta
        '''
        return self.__extrato_op
