from abc import ABC, abstractmethod
class Conta:
    def __init__(self, id_conta, saldo_conta):
        self._id_conta = id_conta
        self._saldo_conta = saldo_conta

    #get do id_conta
    @property
    def id(self):
        print(f"O id da conta é: {self._id_conta}")
        print("------------------------------------------------------------")
    
    #set do id_conta
    @id.setter
    def id(self, id_conta):
        self._id_conta = id_conta

    #get do saldo
    @property
    def saldo(self):
        print(f"O valor do saldo em conta é: R${self._saldo_conta}")
        print("------------------------------------------------------------")
    
    #set do saldo
    @saldo.setter
    def saldo(self, saldo_conta):
        self._saldo_conta = saldo_conta

    @abstractmethod
    def depositar(self):
        pass
    
    @abstractmethod
    def sacar(self):
        pass
