from typing import List, Union

Number = Union[int, float]


class Cliente:
    '''
    Classe Cliente do Módulo do Banco
    '''
    def __init__(self, nome: str, telefone: int, email: str) -> None:
        self._nome = nome
        self._tel = telefone
        self._email = email

    def get_nome(self) -> str:
        '''
        Acessor do atributo Nome
        '''
        return self._nome

    def get_telefone(self) -> int:
        '''
        Acessor do atributo Telefone
        '''
        return self._tel

    def set_telefone(self, novo_telefone: int) -> None:
        '''
        Mutador do atributo Telefone
        '''
        if not type(novo_telefone) == int:
            raise TypeError
        elif novo_telefone > 10**10 or novo_telefone <= 10**7:
            raise ValueError
        else:
            self._tel = novo_telefone

    def get_email(self) -> str:
        '''
        Acessor do atributo E-mail
        '''
        return self._email

    def set_email(self, novo_email) -> None:
        '''
        Mutador do atributo E-mail
        '''
        if '@' not in novo_email:
            raise ValueError
        self._email = novo_email


class Conta:
    '''
    Conta básica
    '''
    def __init__(self, clientes: List[Cliente],
                 numero_conta: int, saldo_inicial: Number):
        self._clientes = clientes
        self._numero = numero_conta
        if saldo_inicial < 0:
            raise ValueError
        self._saldo = saldo_inicial

    def get_clientes(self) -> List[Cliente]:
        '''
        Acessor Clientes
        '''
        return self._clientes

    def get_numero_conta(self) -> int:
        '''
        Acessor Número da Conta
        '''
        return self._numero

    def get_saldo(self) -> Number:
        '''
        Acessor Saldo
        '''
        return self._saldo

    def set_saldo(self, novo_saldo: Number) -> None:
        self._saldo = novo_saldo

    def deposito(self, valor: Number) -> None:
        self._saldo += valor

    def saque(self, valor: Number) -> None:
        self._saldo -= valor


class ContaPoupanca(Conta):
    '''
    Conta Poupança
    '''
    def __init__(self, clientes: List[Cliente], numero_conta: int,
                 saldo_inicial: Number, taxa_juros: float):
        super().__init__(clientes, numero_conta, saldo_inicial)
        self._juros = taxa_juros

    def rendimentos(self) -> None:
        self._saldo += self._saldo*self._juros

    def saque(self, valor):
        if valor > self.get_saldo():
            raise ValueError
        super().saque(valor)
